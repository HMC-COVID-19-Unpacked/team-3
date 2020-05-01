import plotly.graph_objects as go
import pandas as pd
import json
import plotly.express as px

df = pd.read_excel('Cardiovascular2014-.xlsx', usecols=['Fips_text', 'Mortality', 'Location'], dtype={'Fips_text': str})
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
    locations=df['Fips_text'], # Spatial coordinates
    z = df['Mortality'], # Data to be color-coded
    geojson = counties, # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "Cardiovascular Death per 10,000",
    text = df['Location'], # give county names
))

fig.update_layout(
    title_text = "USA by cardiovascular mortality (Death per 10,000 population)", 
    geo_scope = 'usa'
)


fig.show()