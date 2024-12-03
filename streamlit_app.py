import streamlit as st

import pandas as pd
from shapely.geometry import Point
import geopandas as gpd


manual_data = [
    {"name": "Главный корпус", "type": "корпус", "latitude": 51.186920 , "longitude": 71.409717},
    {"name": "Био корпус", "type": "корпус", "latitude":51.187944, "longitude": 71.409579},
    {"name": "Старый тех корпус", "type": "корпус", "latitude": 51.187625,  "longitude": 71.411373},
    {"name": "Новый тех корпус", "type": "корпус", "latitude": 51.187086, "longitude":  71.411717},
    {"name": "Военная кафедра", "type": "корпус", "latitude": 51.187306, "longitude": 71.410942},
    {"name": "Управление Земельными Ресурсами Архитектура и Дизайн", "type": "корпус", "latitude": 51.186499, "longitude": 71.415311},
    {"name": "Общежитие 7", "type": "здание", "latitude": 51.186302,  "longitude":71.412643},
    {"name": "Поликлинника/Общежитие 2А", "type": "здание", "latitude": 51.186364, "longitude": 71.413280, },
    {"name": "Агрономический корпус", "type": "корпус", "latitude": 51.185989, "longitude": 71.410354}
]

manual_df = pd.DataFrame(manual_data)


gdf_manual = gpd.GeoDataFrame(
    manual_df,
    geometry=gpd.points_from_xy(manual_df['longitude'], manual_df['latitude']),
    crs="EPSG:4326"
)


st.title("Карта кампуса университета")
st.map(gdf_manual)
