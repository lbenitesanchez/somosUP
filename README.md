# Casos de Administración UP (simulados)

Este repositorio contiene 10 casos ficticios para estudiantes de colegio. Cada caso incluye datos simulados, visualizaciones y un dashboard interactivo en Streamlit.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Generar datos

En cada carpeta `casos/caso_XX_*` ejecuta:

```bash
python generate_data.py
```

Los CSV se guardan en `data/`.

## Ejecutar dashboard

```bash
streamlit run dashboard.py
```

## Nota

Todas las empresas y cifras son ficticias y referenciales.

> Nota: si ejecutas los scripts desde una subcarpeta `casos/caso_XX_*`, asegúrate de hacerlo desde la raíz del repo o mantener la estructura para que se encuentre el módulo `common/`.
