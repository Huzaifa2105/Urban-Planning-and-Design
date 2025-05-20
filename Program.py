#phase 4
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Data
data = {
    'District': ['Central', 'North', 'East', 'West', 'South'],
    'Population Density (per sq.km)': [12000, 8500, 7000, 5000, 6500],
    'Green Cover (%)': [15, 30, 25, 40, 20],
    'Infrastructure Score (0-10)': [8, 6, 5, 7, 6]
}
df = pd.DataFrame(data)

# Line Plot
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=df['District'], y=df['Population Density (per sq.km)'],
                              mode='lines+markers', name='Population Density', line=dict(color='red')))
fig_line.add_trace(go.Scatter(x=df['District'], y=df['Green Cover (%)'],
                              mode='lines+markers', name='Green Cover', line=dict(color='green')))
fig_line.add_trace(go.Scatter(x=df['District'], y=df['Infrastructure Score (0-10)'],
                              mode='lines+markers', name='Infrastructure Score', line=dict(color='blue')))
fig_line.update_layout(title='Line Plot: Urban Metrics by District')

# Bar Chart
fig_bar = go.Figure(data=[
    go.Bar(name='Population Density', x=df['District'], y=df['Population Density (per sq.km)'], marker_color='red'),
    go.Bar(name='Green Cover', x=df['District'], y=df['Green Cover (%)'], marker_color='green'),
    go.Bar(name='Infrastructure Score', x=df['District'], y=df['Infrastructure Score (0-10)'], marker_color='blue')
])
fig_bar.update_layout(barmode='group', title='Grouped Bar Chart: Urban Metrics by District')

# Pie Chart
fig_pie = px.pie(df, values='Green Cover (%)', names='District', title='Green Cover Share by District', color_discrete_sequence=px.colors.sequential.Greens)


# Show in browser (or export individually)
fig_line.show()
fig_bar.show()
fig_pie.show()


#phase 5
import matplotlib.pyplot as plt
import pandas as pd

# Simulated data for urban planning
years = list(range(2015, 2025))
population = [10000, 11000, 12000, 13000, 14000, 15200, 16500, 17900, 19300, 20800]

land_use = {
    'Zone': ['Residential', 'Commercial', 'Industrial', 'Green Space', 'Institutional'],
    'Area (%)': [45, 20, 15, 10, 10]
}

# Create line chart: Population Growth
plt.figure(figsize=(10, 5))
plt.plot(years, population, marker='o', color='teal', linestyle='--')
plt.title('Population Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.tight_layout()
plt.show()

# Create bar chart: Land Use Distribution
land_df = pd.DataFrame(land_use)
plt.figure(figsize=(8, 5))
plt.bar(land_df['Zone'], land_df['Area (%)'], color='skyblue', edgecolor='black')
plt.title('Land Use Distribution')
plt.xlabel('Land Use Zone')
plt.ylabel('Area (%)')
plt.tight_layout()
plt.show()
