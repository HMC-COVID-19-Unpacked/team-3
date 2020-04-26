import plotly.graph_objects as go
import pandas as pd
import json

BASE_DIR = 'obesity/'

# Make sure fips has five digits by adding leading 0s
def add0s(fips):
    if (len(str(fips)) < 5):
        return '0' + str(fips)
    else:
        return str(fips)

## Making a dataframe of all the data found in the csv
df = pd.read_csv(BASE_DIR + 'Obesity_Data.csv', usecols=['fips', 'Outcome', 'Prevalence 2011 (%)'], dtype={'fips': str})

## Getting all fips codes from json
with open(BASE_DIR + 'counties_locations.json') as response:
    counties = json.load(response)

## Filter out all of the non-obesity columns from the data frame, then remove Obesity column
locations = df[df['Outcome']=='Obesity'].filter(items=['fips', 'Prevalence 2011 (%)'])

## Making two new series, one with unique fips formatted properly and one with mean obesity
uniqueFips = locations.fips.map(add0s).unique()[:-1] ## Last value is NaN
meanLocationSeries = locations.groupby(by=locations.fips, sort=False).mean()

## Putting together all the information
compiled = pd.DataFrame(data={'fips': uniqueFips, 'Prevalence': meanLocationSeries["Prevalence 2011 (%)"].tolist()})

# compiled = compiled.sort_values(by=['fips'])
# compiled = compiled.rename(columns={'Prevalence': 'freq'})
# compiled['freq'] = compiled['freq'].apply(lambda x: x/100)
# compiled.to_csv('overall_data/obesity_compiled.csv')

## Create a graph object to plot the new data
fig = go.Figure(data=go.Choropleth(
    locations = compiled['fips'], # Spatial coordinates
    z = compiled['Prevalence'], # Data to be color-coded
    geojson = counties, # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Obesity %"
))

fig.update_layout(
    title_text = "USA by Obesity %", 
    geo_scope = 'usa'
)

fig.show()