import pandas as pd
import plotly_express as px

df = pd.read_csv("covid_data.csv")

fig = px.scatter(df,x = "Date",y= "Cases",color="Country",size_max=60)
fig.show()