import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

connection_string = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)
engine = create_engine(connection_string)


# Cargar datos desde la base de datos
def cargar_datos():
    query = "SELECT sentiment, created_at FROM tweets"
    df = pd.read_sql(query, engine)
    df["created_at"] = pd.to_datetime(df["created_at"])
    return df


# Crear la app Dash
app = dash.Dash(__name__)
data = cargar_datos()

fig_sentimientos = px.pie(data, names="sentiment", title="Distribución de Sentimientos")
fig_tiempo = px.histogram(
    data,
    x="created_at",
    color="sentiment",
    title="Sentimientos a lo largo del tiempo",
    nbins=30,
)

app.layout = html.Div(
    [
        html.H1("Análisis de Sentimientos de Twitter", style={"textAlign": "center"}),
        dcc.Graph(figure=fig_sentimientos),
        dcc.Graph(id="graph-2", figure=fig_tiempo),  # Aquí se le asigna el id 'graph-2'
        html.Div(
            [
                html.Label("Filtrar por fechas:"),
                dcc.DatePickerRange(
                    id="date-picker-range",
                    start_date=data["created_at"].min().date(),
                    end_date=data["created_at"].max().date(),
                    display_format="YYYY-MM-DD",  # formato de fecha
                ),
            ],
            style={"textAlign": "center", "margin": "20px"},
        ),
    ]
)


# Callback para actualizar el gráfico con el filtro de fechas
@app.callback(
    [
        dash.dependencies.Output("date-picker-range", "end_date"),
        dash.dependencies.Output("date-picker-range", "start_date"),
        dash.dependencies.Output("graph-2", "figure"),
    ],  # Se actualiza el gráfico con id 'graph-2'
    [dash.dependencies.Input("date-picker-range", "start_date")],
)
def update_graph(start_date):
    filtered_data = data[data["created_at"] >= pd.to_datetime(start_date)]
    end_date = filtered_data["created_at"].max().date()
    fig_tiempo = px.histogram(
        filtered_data,
        x="created_at",
        color="sentiment",
        title="Sentimientos a lo largo del tiempo",
        nbins=30,
    )

    return str(end_date), str(start_date), fig_tiempo


if __name__ == "__main__":
    app.run_server(debug=True)
