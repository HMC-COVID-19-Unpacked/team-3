import plotly.graph_objects as go
import pandas as pd
import json
import plotly.express as px

df = pd.read_excel('DiabetesAtlasCountyData_excel.xlsx', usecols=['Fips', 'Percentage'], dtype={'Fips': str})

with open('counties_locations.json') as response:
    counties = json.load(response)

fig = go.Figure(data=go.Choropleth(
    locations=df['Fips'], # Spatial coordinates
    z = df['Percentage'], # Data to be color-coded
    geojson = counties, # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Diabetes %"
))

fig.update_layout(
    title_text = "USA by Diabetes %", 
    geo_scope = 'usa'
)

fig.show()