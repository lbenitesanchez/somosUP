"""Helpers de gráficos con Plotly."""
from __future__ import annotations
import plotly.express as px
import pandas as pd


def line_chart(df: pd.DataFrame, x: str, y: list[str], title: str):
    fig = px.line(df, x=x, y=y, markers=True, title=title)
    fig.update_layout(legend_title_text='Indicador')
    return fig


def bar_chart(df: pd.DataFrame, x: str, y: str, title: str, color: str | None = None):
    fig = px.bar(df, x=x, y=y, color=color, title=title)
    return fig


def pie_chart(df: pd.DataFrame, names: str, values: str, title: str):
    fig = px.pie(df, names=names, values=values, hole=0.4, title=title)
    return fig


def decision_chart(df: pd.DataFrame, x: str, y: str, color: str, title: str):
    fig = px.bar(df, x=x, y=y, color=color, barmode='group', title=title)
    return fig
