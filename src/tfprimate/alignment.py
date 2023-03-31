import urllib.request as urlreq
from dash import Dash, html
import dash_bio as dashbio
import sys

# create a alignment chart using dash
# https://plotly.com/python/alignment-chart/

def alignChart(alignment):
  with open(alignment, "r") as f:
    d = f.read()

  fig = dashbio.AlignmentChart(
    id='alignment-viewer',
    data=d
    )
  
  return fig

if __name__ == "__main__":
  app = Dash(__name__)
  alignment_input = input("Please enter a alignment file name(path): ")
  aln_fig = alignChart(alignment_input)
  app.layout = html.Div([aln_fig])
  app.run_server()
