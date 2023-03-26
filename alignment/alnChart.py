import urllib.request as urlreq
from dash import Dash, html
import dash_bio as dashbio

# create a alignment chart using dash
# https://plotly.com/python/alignment-chart/

app = Dash(__name__)

data = urlreq.urlopen('https://git.io/alignment_viewer_p53.fasta').read().decode('utf-8')

app.layout = html.Div([
  dashbio.AlignmentChart(
    id='alignment-viewer',
    data=data
  )
])

if __name__ == '__main__' :
  app.run_server(debug=True)