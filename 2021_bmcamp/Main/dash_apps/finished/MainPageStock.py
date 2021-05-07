import plotly.express as px
df = px.data.stocks()
fig = px.line(df, x="date", y=df.columns,
              hover_data={"date": "|%B %d, %Y"},
              title='')
config = {'displayModeBar': False}
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
fig.update_xaxes(
    color = 'rgba(0, 0, 0, 0)',
    dtick="M1",
    tickformat="%b\n%Y",
    showgrid = False
)
fig.update_yaxes(
    color = 'rgba(0, 0, 0, 0)',
    showgrid = False
)
import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

app = DjangoDash('MainPageStock')
app.layout = html.Div([
    dcc.Graph(figure=fig,config = config)
])

