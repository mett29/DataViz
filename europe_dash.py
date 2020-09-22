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
colors = ['Oranges', 'Reds', 'Greens', 'Blues', 'RdPu']
dimensions_descr = ['calculated as the weighted average of the five sub-dimensions: 1a Fixed Broadband take-up (25%), 1b Fixed broadband coverage (25%), 1c Mobile broadband (35%) and 1d Broadband price index (15%)',
                        'calculated as the weighted average of the two sub-dimensions: 2a Internet User Skills (50%) and 2b Advanced Skills and Development (50%)]',
                        'calculated as the weighted average of the three sub-dimensions: 3a Internet Use (25%), 3b Activities Online (50%), 3c Transactions (25%)',
                        'calculated as the weighted average of the two sub-dimensions: 4a Business digitisation (60%) and 4b e-Commerce (40%)',
                        'calculated by taking the score for 5a e-Government']

years = list(map(int, desi_r.time_period.unique()))


dimensions_min_val = []
dimensions_max_val = []
for dim in dimensions:
    dimensions_min_val.append(desi_r.loc[(desi_r['breakdown'] == dim)].value.min())
    dimensions_max_val.append(desi_r.loc[(desi_r['breakdown'] == dim)].value.max())

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
                value='1 DESI Connectivity Dimension',
                clearable=False
                )
        ])
    ],
    style={'margin': '35px 50px 0px', 'float': 'right', 'display': 'inline-block'}),

    html.Div([

        html.Div([
            html.H5('Indicator',
                id='indicator')
        ]),

        html.Div([
            dcc.Markdown('Description',
                id='indicator-descr')
        ]),
    ],
    style={'margin': 'auto', 'width': '60%', 'height': '120px', 'text-align': 'center', 'display': 'block'}),


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
    [Output('choropleth', 'figure'),
    Output('indicator', 'children'),
    Output('indicator-descr', 'children')],
    [Input('dimension-selector', 'value'),
     Input('year-slider', 'value')])
def update_graph(dimension,
                 year_value):
    
    dimension_index=dimensions.index(dimension)
    
    # Trim the DESI dimension number
    indicator = dimension[2:]

    indicator_descr = dimensions_descr[dimension_index]

    year = str(year_value)
    data = desi_r.loc[(desi_r['breakdown'] == dimension) & (desi_r['time_period'] == year)]


    fig = px.choropleth(data,
        locations='ref_area',
        locationmode='country names',
        featureidkey='properties.wb_a2',
        labels={'time_period':'Year', 'ref_area':'Country', 'breakdown':'Indicator',
       'value':'Score', 'ref_area_id':'Country ID'},
        color='value',
        color_continuous_scale=colors[dimension_index],
        hover_name='ref_area',
        hover_data=['breakdown', 'time_period'])


    fig.update_geos(
        resolution=50,
        showlakes=False,
        scope='europe'
    )
    
    fig.update_layout(width=1200, height=900,
        coloraxis=dict(colorbar_len=0.9, 
                    colorbar_thickness=25,
                    colorbar_outlinewidth=1,
                    cmin=dimensions_min_val[dimension_index],
                    cmax=dimensions_max_val[dimension_index]),
        dragmode=False,
        margin={'l': 0, 'b': 0, 't': 0, 'r': 0, 'pad': 0}
    )

    return fig, indicator, indicator_descr


if __name__ == '__main__':
    app.run_server(debug=True)