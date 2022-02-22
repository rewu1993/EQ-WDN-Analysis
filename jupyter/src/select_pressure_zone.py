import json
import pandas as pd
import geocoder
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkt
import shapely.speedups
from shapely.ops import nearest_points

shapely.speedups.enable()

# select zone 
def select_pressure_zone(df,zone_codes):
    df = df[df['OBJECTID'].isin(zone_codes)]
    dummy = len(zone_codes)*[1]
    df['dummy'] = dummy
    selected_zone = df.dissolve(by='dummy')
    return selected_zone


def plot_geometries(geom1,geom2):
    fig, ax = plt.subplots(figsize = (8,8))
    geom1.plot(ax = ax,facecolor='red')
    geom2.plot(ax = ax)

    
def nearest(row, geom_union, df1, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
    """Find the nearest point and return the corresponding value from specified column."""
    # Find the geometry that is closest
    nearest = df2[geom2_col] == nearest_points(row[geom1_col], geom_union)[1]
    # Get the corresponding value from df2 (matching is based on the geometry)
    value = df2[nearest][src_column].get_values()[0]
    return value