import plotly.graph_objects as go

asthma_data = {
    'AL': 10.5, 'AK': 9.2, 'AZ': 10.0, 'AR': 9.8, 'CA':	8.5, 'CO': 9.1, 'CT': 10.3, 'DE': 10.1, 
    'DC': 11.6, 'FL': 8.7, 'GA': 8.9, 'HI': 9.3, 'ID': 8.6, 'IL': 8.7, 'IN': 10.0, 'IA': 7.9, 
    'KS': 9.8, 'KY': 11.5, 'LA': 8.9, 'ME': 12.3, 'MD': 9.3, 'MA': 10.2, 'MI': 11.2, 'MN': 8.3,
    'MS': 9.7, 'MO': 9.4, 'MT': 10.0, 'NE': 8.9, 'NV': 8.0, 'NH': 11.8, 'NJ': 8.4, 'NM': 9.9,
    'NY': 10.1, 'NC': 9.4, 'ND': 8.2, 'OH': 9.4, 'OK': 10.3, 'OR': 11.6, 'PA': 10.0, 'RI': 11.9, 
    'SC': 9.1, 'SD': 7.9, 'TN': 9.8, 'TX': 7.4, 'UT': 9.3, 'VT': 12.0, 'VA': 8.5, 'WA': 9.6,
    'WV': 12.3, 'WI': 9.0, 'WY': 8.7
}

# Compile data into two lists
codes = list(asthma_data.keys())
percents = list(asthma_data.values())

# Create map
fig = go.Figure(data=go.Choropleth(
    locations=codes, # Spatial coordinates
    z = percents, # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Population diagnosed with asthma (%)",
))

# Metadata
fig.update_layout(
    title_text = 'Asthma frequency by state',
    geo_scope='usa', # limite map scope to USA
)

def get_html():
    return fig.to_html()

# fig.show()