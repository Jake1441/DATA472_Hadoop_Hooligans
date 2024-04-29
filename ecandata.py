"""Run this as a module"""

import pandas as pd
import requests
#################
import json

import requests
from graphql import build_client_schema, GraphQLSchema, print_schema, parse, execute

url = "https://gis.ecan.govt.nz/arcgis/rest/services/Public/Groundwater/MapServer/19/query?outFields=*&where=1%3D1&f=geojson"

def get_ecan_data():
    """Function to call the Ecan api. Returns a pandas dataframe"""
    response = requests.get(url)
    data = response.json()

    extracted_data = []
    for feature in data['features']:
        properties = feature['properties']
        longitude, latitude = feature['geometry']['coordinates']
        extracted_data.append({
            'ID': properties['ID'],
            'Well_No': properties['Well_No'],
            'Primary_Use': properties['Primary_Use'],
            'WGS84_LONGITUDE': longitude,
            'WGS84_LATITUDE': latitude
        })
    df = pd.DataFrame(extracted_data)
    return df


print(get_ecan_data())