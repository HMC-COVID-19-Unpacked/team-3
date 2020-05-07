import plotly.graph_objects as go
import addfips 
import json
import pandas as pd

other_FIPS = {}

# Reading stuff, cleaning it up to just 2012 data
df = pd.read_csv('/Users/daniela/Desktop/IHME_US_COUNTY_TOTAL_AND_DAILY_SMOKING_PREVALENCE_1996_2012/IHME_US_COUNTY_TOTAL_AND_DAILY_SMOKING_PREVALENCE_1996_2012.csv', usecols = ["state", "county", "sex", "year", "total_mean"])
df = df[df['state'] != 'National']
df = df[df['sex'] == 'Both']
df = df[df['year'] == 2012]
del df['sex']
del df['year']
df.dropna(subset = ['county'], inplace=True)
df = df[df['county'].str.contains('/') == False] # getting rid of the / counties 


# Adding FIPS
af = addfips.AddFIPS()
FIPS = []
statesList = list(df['state'])
countiesList = list(df['county'])
for i in range(len(statesList)):
    state = statesList[i]
    county = countiesList[i]
    FIP = af.get_county_fips(county, state)
    FIPS.append(FIP)

with open('/Users/daniela/Desktop/counties_locations.json') as response:
    counties = json.load(response)

# Create map
fig = go.Figure(data=go.Choropleth(
    locations = FIPS, # Spatial coordinates
    z = df['total_mean'], # Data to be color-coded
    geojson = counties, # # set of locations 
    colorscale = 'Blues',
    colorbar_title = "Average smoking prevalence",
    text = countiesList # give county names
))

# Metadata
fig.update_layout(
    title_text = 'Average smoking prevalence per county',
    geo_scope = 'usa',
)

fig.show()