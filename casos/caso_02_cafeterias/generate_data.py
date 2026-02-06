"""Genera datos simulados para el caso 2: Café Volado: ¿cómo crecer sin colapsar?.

Variables:
- kpi_1, kpi_2, kpi_3, kpi_4: indicadores mensuales (unidades según el caso).
- segmento: grupo de clientes o contexto.
- metrico_principal: indicador principal por segmento.
- costo_mensual: S/ por rubro.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from common.utils import set_seed, month_range, save_csv

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'


def main() -> None:
    seed = 202601 + 2
    set_seed(seed)

    months = month_range('2023-01-01', 18)
    kpi_1 = np.linspace(1.0, 1.35, len(months)) * np.random.normal(1.0, 0.03, len(months))
    kpi_2 = np.linspace(0.9, 1.1, len(months)) * np.random.normal(1.0, 0.04, len(months))
    kpi_3 = np.linspace(0.8, 1.05, len(months)) * np.random.normal(1.0, 0.05, len(months))
    kpi_4 = np.linspace(1.1, 0.95, len(months)) * np.random.normal(1.0, 0.04, len(months))

    ts_df = pd.DataFrame({
        'mes': months,
        'kpi_1': (kpi_1 * 1000).round(0),
        'kpi_2': (kpi_2 * 100).round(1),
        'kpi_3': (kpi_3 * 100).round(1),
        'kpi_4': (kpi_4 * 100).round(1),
    })

    segments = ['Mañana', 'Tarde', 'Noche']
    seg_df = pd.DataFrame({
        'segmento': segments,
        'metrico_principal': np.random.uniform(60, 140, len(segments)).round(1),
        'satisfaccion': np.random.uniform(3.2, 4.6, len(segments)).round(2),
    })

    costos = ['Personal', 'Tecnologia', 'Marketing', 'Logistica', 'Otros']
    cost_df = pd.DataFrame({
        'rubro': costos,
        'costo_mensual': np.random.uniform(8000, 28000, len(costos)).round(0),
        'ingreso_alt_a': np.random.uniform(22000, 52000, len(costos)).round(0),
        'ingreso_alt_b': np.random.uniform(24000, 56000, len(costos)).round(0),
    })

    save_csv(ts_df, DATA_DIR / 'serie_tiempo.csv')
    save_csv(seg_df, DATA_DIR / 'segmentos.csv')
    save_csv(cost_df, DATA_DIR / 'costos_ingresos.csv')


if __name__ == '__main__':
    main()
