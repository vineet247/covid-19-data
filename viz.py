import pandas as pd
import numpy as np
import plotly as pl
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

pd.set_option('display.max_rows', None)
df = pd.read_csv("us-counties.csv")
#print(df)

latest_df = df.loc[df['date'] == "2020-04-04"]
latest_df = latest_df.dropna()
latest_df.astype({'fips': 'int64'}).dtypes
#print(latest_df)

latest_df.plot(column = "cases")
