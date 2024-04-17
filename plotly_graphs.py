import plotly_express as px
import pandas as pd
df_wind = px.data.wind()
df_bird = pd.read_csv('birds.csv')
print (df_bird.info())
#df = px.data.tips()
fig = px.pie(df_bird, values='Deaths', names='Bldg #',color='Side',hole=0.25)
fig.update_traces(textinfo="label+value",insidetextfont_color="white")
fig.update_layout(legend_itemclick=False)
#fig.update_layout()
fig.show()