import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

desi = pd.read_csv("data/DESI.csv")

# Drop useless columns
desi = desi.drop(['observation', 'flag', 'note'], axis=1)

# Mapping between 'ref_area' and the name of the country
countries_mapping =  { 'EE' : 'Estonia',
                        'EL' : 'Greece',
                        'ES' : 'Spain',
                        'FI' : 'Finland',
                        'FR' : 'France',
                        'HR' : 'Croatia',
                        'HU' : 'Hungary',
                        'IE' : 'Ireland',
                        'IS' : 'Iceland',
                        'DE' : 'Germany',
                        'CZ' : 'Czech Rep.',
                        'DK' : 'Denmark',
                        'IT' : 'Italy',
                        'LT' : 'Lithuania',
                        'LU' : 'Luxembourg',
                        'LV' : 'Latvia',
                        'MT' : 'Malta',
                        'NL' : 'Netherlands',
                        'NO' : 'Norway',
                        'PT' : 'Portugal',
                        'PL' : 'Poland',
                        'EU' : 'Europe',
                        'RO' : 'Romania',
                        'SE' : 'Sweden',
                        'SI' : 'Slovenia',
                        'SK' : 'Slovakia',
                        'UK' : 'United Kingdom',
                        'AT' : 'Austria',
                        'BE' : 'Belgium',
                        'BG' : 'Bulgaria',
                        'CY' : 'Cyprus',
                        'CH' : 'Switzerland'
                     }
desi['ref_area_id'] = desi['ref_area']
desi['ref_area'] = desi['ref_area'].replace(countries_mapping)

# Drop the index column
desi.reset_index(drop=True, inplace=True)

# In some cases the types in 'time_period' are mixed ==> cast all to strings 
desi['time_period'] = desi['time_period'].apply(lambda j: str(j))

# Map the indicators' codes to the corresponding name
desi_r = desi[desi.breakdown.isin(['desi_1_conn', 'desi_2_hc', 'desi_3_ui', 'desi_4_idt', 'desi_5_dps'])]
desi_r = desi_r[desi_r.indicator.isin(['desi_sliders'])]

indicators_mapping = {'desi_1_conn' : '1 DESI Connectivity Dimension',
           'desi_2_hc' : '2 DESI Human Capital Dimension',
           'desi_3_ui' : '3 DESI Use of Internet Dimension',
           'desi_4_idt' : '4 DESI Integration of Digital Technology Dimension',
           'desi_5_dps' : '5 DESI Digital Public Services Dimension',
          }
desi_r['breakdown'] = desi_r['breakdown'].replace(indicators_mapping)

# Visualization parameters
dimensions = ['1 DESI Connectivity Dimension',
           '2 DESI Human Capital Dimension',
           '3 DESI Use of Internet Dimension',
           '4 DESI Integration of Digital Technology Dimension',
           '5 DESI Digital Public Services Dimension']
years = list(map(int, desi_r.time_period.unique()))
colors = ['Oranges', 'Reds', 'Greens', 'Blues', 'RdPu']

# Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Markdown('## **DESI** Choropleth map')
            ]),   
    ],
    style={'width': '30%', 'margin': '12px 40px', 'display': 'inline-block'}),

    html.Div([     

        html.Div([
            dcc.Markdown('Select an **indicator** and compare countries:')
        ]),

        html.Div([
            dcc.Dropdown(
                id='dimension-selector',
                options=[{'label': i, 'value': i} for i in dimensions],
                value='1 DESI Connectivity Dimension'
                )
        ])
    ],
    style={'margin': '35px 50px 0px', 'float': 'right', 'display': 'inline-block'}),


    dcc.Graph(id='choropleth',
            figure=dict(
                        data=[],
                        layout={},
                    )
    ),

    html.Div([

        html.Div([
            dcc.Markdown('Select a **year**:')
        ],
        style={'text-align':'center'}),

        dcc.Slider(
            id='year-slider',
            min=min(years),
            max=max(years),
            value=max(years),
            marks={str(year): str(year) for year in years},
            step=None,
            included=False,
            updatemode='drag'
            )         
    ],
    style={'margin': '0px 300px'}),

    
],
style={'width': '1200px'})


@app.callback(
    Output('choropleth', 'figure'),
    [Input('dimension-selector', 'value'),
     Input('year-slider', 'value')])
def update_graph(dimension,
                 year_value):
    
    year = str(year_value)
    data = desi_r.loc[(desi_r['breakdown'] == dimension) & (desi_r['time_period'] == year)]

    color_index=dimensions.index(dimension)

    fig = px.choropleth(data,
        locations='ref_area',
        locationmode='country names',
        featureidkey='properties.wb_a2',
        labels={'time_period':'Year', 'ref_area':'Country', 'breakdown':'Indicator',
       'value':'Value', 'ref_area_id':'Country ID'},
        color='value',
        color_continuous_scale=colors[color_index],
        hover_name='ref_area',
        hover_data=['breakdown', 'time_period'])


    fig.update_geos(
        #visible=False,
        resolution=50,
        showlakes=False,
        scope='europe'
    )
    
    fig.update_layout(width=1200, height=900,
    coloraxis=dict(colorbar_len=0.9, 
                colorbar_thickness=25,
                colorbar_outlinewidth=1)
    #margin={'l': 40, 'b': 40, 't': 10, 'r': 0}
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)