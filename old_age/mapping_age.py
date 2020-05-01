import plotly.graph_objects as go
import pandas as pd
import json
import plotly.express as px

# data source: U.S. Census Bureau, Population Division

df = pd.read_excel('age.xlsx', usecols=['FIPS', 'OVER65', 'CTYNAME'], dtype={'FIPS': str})
#make df dict
# dfDict = dict(zip(df['Fips_text'], df['Mortality']))
# print(dfDict)
#make covid dict
# covid = pd.read_excel('./04-22-2020COVIDC.xls', usecols=['Province_State', 'ConfirmedText', 'FIPS_Text'], dtype={'FIPS_Text': str})
# covidDictName = dict(zip(covid['Province_State'], covid['ConfirmedText']))
# covidDictFIPS = dict(zip(covid['FIPS_Text'], covid['ConfirmedText']))



with open('counties_locations.json') as response:
    counties = json.load(response)


fig = go.Figure(data=go.Choropleth(
    locations=df['FIPS'], # Spatial coordinates
    z = df['OVER65'], # Data to be color-coded
    geojson = counties, # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "Proportion of population over 65 in 2018",
    text = df['CTYNAME'], # give county names
))

fig.update_layout(
    title_text = "USA by proportion of population over 65 in 2018", 
    geo_scope = 'usa'
)


fig.show()