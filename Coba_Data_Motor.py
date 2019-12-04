import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dfhonda = pd.read_excel('Penjualan_Motor_20052018.xlsx', index_col = 0)

def generate_table(dataframe, page_size = 10):
     return dash_table.DataTable(
                    id = 'dataTable',
                    columns = [{"name": i, "id": i} for i in dataframe.columns],
                    data=dataframe.to_dict('records'),
                    page_action="native",
                    page_current= 0,
                    page_size= page_size,
                )

app.layout = html.Div([
        html.H1('Ini Coba Data Motor'),
        html.P('Disuruh Sama Mas Cornellius, wkwkwkwkkw'),
        html.Div([html.Div(children =[
        dcc.Tabs(value = 'tabs', id = 'tabs-1', children = [
            dcc.Tab(value = 'Tabel', label = 'DataFrame Table', children =[
                html.Center(html.H1('DATAFRAME PENJUALAN MOTOR 2005 - 2018')),
                html.Div(children =[
                    html.Div(children =[
                        html.P('Penjualan:'),
                        dcc.Dropdown(value = '', id='filter-penjualan', options = [
                                                                                    {'label':'Honda','value':'Honda'},
                                                                                    {'label':'Yamaha', 'value':'Yamaha'},
                                                                                    {'label':'Suzuki', 'value':'Suzuki'},
                                                                                    {'label':'Kawasaki', 'value':'Kawasaki'},
                                                                                    {'label':'Others', 'value':'Others'},
                                                                                    {'label':'Total', 'value':'Total'},
                                                                                    {'label':'ALL', 'value':''}

                    ], className = 'col-3')
                ], className = 'row'),
                html.Div([
                    html.P('Max Rows : '),
                    dcc.Input(
                        id='filter-row',
                        type='number',
                        value=10,
                    )
                ], className = 'row col-3'),
                html.Br(),
                html.Div(children =[
                        html.Button('cari dong bos',id = 'filter')
                    ],className = 'col-4'),
                html.Br(),    
                html.Div(id = 'div-table', children =[generate_table(dfhonda)])
                ])
            ])
        ], 
        ## Tabs Content Style
        content_style = {
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
        })
        ])
], style ={
        'maxWidth': '1800px',
        'margin': '0 auto'
    })
])

@app.callback(
    Output(component_id = 'div-table', component_property = 'children'),
    [Input(component_id = 'filter', component_property = 'n_clicks')],
    [State(component_id = 'filter-penjualan', component_property = 'value'),
    State(component_id = 'filter-row', component_property = 'value')]
)

def update_table(n_clicks, penjualan, row):
    if penjualan == '':
        children = [generate_table(dfhonda, page_size = row)]
    else:
        children = [generate_table(dfhonda[dfhonda['Honda'] == penjualan], page_size = row)]            
    return children


if __name__ == '__main__':
    app.run_server(debug=True)