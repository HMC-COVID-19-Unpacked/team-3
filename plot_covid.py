import pandas as pd
import plotly.graph_objects as go
import numpy as np
import json
import math

DATA_DIR = 'overall_data/'

# Make sure fips has five digits by adding leading 0s
def add0s(fips):
    if (len(str(fips)) < 5):
        return '0' + str(fips)
    else:
        return str(fips)

def get_covid_data(fname=DATA_DIR+'covid_by_county.csv'):
    # Get covid data
    covid = pd.read_csv(fname)
    # Get last column
    most_recent_cases = covid[covid.columns[-1]]
    # Use only relevant columns
    covid = covid[['countyFIPS', 'County Name']]
    # Rename columns
    covid = covid.rename(columns={'countyFIPS': 'fips', 'County Name': 'name'})
    # Add cases back in
    covid['cases'] = most_recent_cases
    # Remove state data
    states = covid['fips'] > 10
    covid = covid[states]
    # Clean FIPS
    covid['fips'] = covid['fips'].apply(add0s)
    # Sort
    covid = covid.sort_values(by=['fips'])
    covid = covid.reset_index()
    return covid

def get_population_data(fname=DATA_DIR+'county_populations.csv'):
    # Get population data
    pop = pd.read_csv(fname)
    # Use only relevant columns
    pop = pop[['countyFIPS', 'County Name', 'population']]
    # Rename columns
    pop = pop.rename(columns={'countyFIPS': 'fips', 'County Name': 'name'})
    states = pop['fips'] > 10
    pop = pop[states]
    # Clean FIPS
    pop['fips'] = pop['fips'].apply(add0s)
    # Sort
    pop = pop.sort_values(by=['fips'])
    pop = pop.reset_index()
    return pop

def plot(locations, data, geojson, county_names, scale_label, title):
    # Create a graph object to plot the new data
    fig = go.Figure(data=go.Choropleth(
        locations = locations, # Spatial coordinates
        z = data, # Data to be color-coded
        geojson = geojson, # set of locations match entries in 'locations'
        text = county_names,
        colorscale = 'Viridis',
        colorbar_title = scale_label
    ))
    fig.update_layout(
        title_text = title, 
        geo_scope = 'usa'
    )
    fig.show()

# Getting all fips codes from json
with open(DATA_DIR + 'counties_locations.json') as response:
    counties = json.load(response)

# Get data
covid = get_covid_data()
pop = get_population_data()

# Normalize covid data by population
covid['freq'] = covid['cases']/pop['population']
covid['freq_log'] = covid['freq'].apply(lambda x: math.log(x + .001, 10))

plot(   locations=covid['fips'], 
        data=covid['freq_log'], 
        geojson=counties, 
        county_names=covid['name'],
        scale_label='Coronavirus frequency (log10 %)',
        title = 'USA by COVID-19 frequency (log10)')