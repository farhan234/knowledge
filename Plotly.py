# Import plotting library from Python
import plotly.graph_objects as go

# Load data frame and tidy it by converting to list
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

# Create the heat map outline
fig = go.Figure(data=go.Choropleth(
    locations=df['code'],  # Spatial coordinates
    z=df['total exports'].astype(float),  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    colorbar_title="Millions USD",
))

# Produce title and scope for map
fig.update_layout(
    title_text='2011 US Agriculture Exports by State',
    geo_scope='usa',  # limit map scope to USA
)

# Display the graph
fig.show()
