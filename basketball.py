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


app.layout = html.Div([
    html.H1(
        children='NBA Most Valuable Player Tracker',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(
        children='A Closer Look at the Top 5 Players in MVP Contention ', 
        style={
            'textAlign': 'center',
            'color': colors['text']
        }   
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
               {
                'x': ['FG%', '3P%', '2P%', 'FT%', 'eFG%'],
                'y': [df['FG%'][0], df['3P%'][0], df['2P%'][0], df['FT%'][0], df['eFG%'][0]],
                'type': 'bar',
                'name': players[0]
                },
                {
                'x': ['FG%', '3P%', '2P%', 'FT%', 'eFG%'],
                'y': [df['FG%'][1], df['3P%'][1], df['2P%'][1], df['FT%'][1], df['eFG%'][1]],
                'type': 'bar',
                'name': players[1]
               },
               {
                'x': ['FG%', '3P%', '2P%', 'FT%', 'eFG%'],
                'y': [df['FG%'][2], df['3P%'][2], df['2P%'][2], df['FT%'][2], df['eFG%'][2]],
                'type': 'bar',
                'name': players[2]
               },
               {
                'x': ['FG%', '3P%', '2P%', 'FT%', 'eFG%'],
                'y': [df['FG%'][3], df['3P%'][3], df['2P%'][3], df['FT%'][3], df['eFG%'][3]],
                'type': 'bar',
                'name': players[3]
               },
               {
                'x': ['FG%', '3P%', '2P%', 'FT%', 'eFG%'],
                'y': [df['FG%'][4], df['3P%'][4], df['2P%'][4], df['FT%'][4], df['eFG%'][4]],
                'type': 'bar',
                'name': players[4]
               }


            ],
            'layout': {
                'title': 'Comparison of Field Goal %, 3-Point %, 2-Point%, Free Throw %, and Effective FG%'
            }
        }
    )
    
    #dcc.Slider(
        #id='stat-slider',
        #min=1,
        #max=5,
        #value=1,
        #marks={
           # 1: stats[0],
            #2: stats[1],
            #3: stats[2],
            #4: stats[3],
            #5: stats[4]
        #}
    #)
    
])







if __name__ == '__main__':
    app.run_server(debug=True)
