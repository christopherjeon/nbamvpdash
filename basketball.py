import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_excel('NBAmvptracker.xlsx', sheet_name='Sheet1')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

stats = ['FG%', '3P%', '2P%', 'FT%', 'PTS']

colors = {
    'background': '#ffffff',
    'text': '#000000'
}

players = []

for i in df.index:
    players.append(df['Player'][i])
    print df['Player'][i]


app.layout = html.Div([
    html.H1(
        children='NBA Most Valuable Player Tracker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(
        children='A Closer Look at the Top 10 Players in MVP Contention ', 
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),

    html.Div([
        dcc.Dropdown(
            id="stat-column",
            options=[{'label': i, 'value': i} for i in stats],
            value="FG%"
        ),
        dcc.Graph(id='model-graphic')
    ])
])

@app.callback(
    dash.dependencies.Output('model-graphic', 'figure'),
    [dash.dependencies.Input('stat-column', 'value')]
     
)
def update_model(variable_column):
    
    return {
        'data': [go.Scatter(
            x=players,
            y=df[variable_column],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],

        'layout': go.Layout(
            xaxis={
                'title': 'MVP Candidates'
                
            },
            yaxis={
                'title': variable_column
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )


    }







if __name__ == '__main__':
    app.run_server(debug=True)
