from pathlib import Path
import pandas as pd
import streamlit as st
from common.plotting import line_chart, bar_chart, pie_chart, decision_chart

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'

st.set_page_config(page_title="Café Volado: ¿cómo crecer sin colapsar?", layout='wide')

st.title("Café Volado: ¿cómo crecer sin colapsar?")
st.caption("Empresa ficticia y cifras referenciales. Caso didáctico para estudiantes.")

serie = pd.read_csv(DATA_DIR / 'serie_tiempo.csv', parse_dates=['mes'])
segmentos = pd.read_csv(DATA_DIR / 'segmentos.csv')
costos = pd.read_csv(DATA_DIR / 'costos_ingresos.csv')

with st.sidebar:
    st.header('Controles')
    alternativa = st.radio('Alternativa', ['A', 'B'])
    precio = st.slider('Precio promedio (S/)', 5, 50, 20)
    conversion = st.slider('Conversión (%)', 1, 10, 3)
    churn = st.slider('Churn (%)', 1, 15, 6)
    segmentos_sel = st.multiselect('Segmentos', segmentos['segmento'].tolist(), default=segmentos['segmento'].tolist())

kpi_1 = serie['kpi_1'].iloc[-1]
kpi_2 = serie['kpi_2'].iloc[-1]
kpi_3 = serie['kpi_3'].iloc[-1]

col1, col2, col3, col4 = st.columns(4)
col1.metric('KPI 1 (último mes)', f"{kpi_1:,.0f}")
col2.metric('KPI 2 (último mes)', f"{kpi_2:,.1f}")
col3.metric('KPI 3 (último mes)', f"{kpi_3:,.1f}")
col4.metric('Precio simulado', f"S/ {precio}")

st.markdown('## 1) Así va el negocio')
st.write('Observa tendencias y posibles cambios de ritmo. ¿Hay meses atípicos?')
fig_line = line_chart(serie, 'mes', ['kpi_1', 'kpi_2', 'kpi_3'], 'Tendencias principales')
st.plotly_chart(fig_line, use_container_width=True)

st.markdown('## 2) ¿Quiénes son los clientes?')
st.write('Compara segmentos y busca quién aporta más al indicador principal.')
seg_filtrado = segmentos[segmentos['segmento'].isin(segmentos_sel)]
fig_bar = bar_chart(seg_filtrado, 'segmento', 'metrico_principal', 'Indicador por segmento')
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown('## 3) Costos e ingresos')
st.write('Revisa la estructura de costos: ¿qué rubro pesa más?')
fig_pie = pie_chart(costos, 'rubro', 'costo_mensual', 'Composición de costos')
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown('## 4) Simulador de decisión')
st.write('Ajusta supuestos para comparar alternativas. Observa la utilidad esperada.')

base_volumen = serie['kpi_1'].iloc[-1] * (conversion / 3)
util_a = base_volumen * precio * 0.12 - costos['costo_mensual'].sum() * 0.4
util_b = base_volumen * (precio + 2) * 0.14 - costos['costo_mensual'].sum() * 0.35

decision_df = pd.DataFrame({
    'Alternativa': ['A', 'B'],
    'Utilidad estimada': [util_a, util_b],
    'Escenario': ['Actual', 'Actual'],
})
fig_dec = decision_chart(decision_df, 'Alternativa', 'Utilidad estimada', 'Escenario', 'Comparación de utilidad')
st.plotly_chart(fig_dec, use_container_width=True)

st.markdown('## 5) Recomendación')
reco = 'La alternativa A luce más estable.' if util_a >= util_b else 'La alternativa B parece más rentable, pero revisa riesgos.'
st.write(reco)
st.write('Qué mirar: si la diferencia es pequeña, los riesgos operativos pueden inclinar la decisión.')
