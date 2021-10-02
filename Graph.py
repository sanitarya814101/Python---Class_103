import pandas as pd
import plotly.express as px

df = pd.read_csv('line_chart.csv')
df2 = pd.read_csv('data.csv')

print(df)

# Line Graph
# fig = px.line(df, x="Year", y="Per capita income",
#              color='Country', title="Per Capita Income")

# fig.show()

# Bar Graph
# fig = px.bar(df, x="Year", y="Per capita income",
#             color='Country', title="Per Capita Income")
# fig.show()

# Scatter Graph
# fig = px.scatter(df2, x="Population", y="Per capita",
#                 size="Percentage", color="Country", size_max=60)
# fig.show()

# Bar Graph
fig = px.bar(df2, x="Country", y="InternetUsers",
             color="Country", barmode="group", title="Bar Graph")
fig.show()
