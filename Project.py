#phase 3
# Import required libraries

 import folium
 import pandas as pd
 from IPython.display import IFrame, display
 import random
 from cryptography.fernet import Fernet
# Subtitle: 1. Urban Data Modeling (AI Model Equivalent)
# Sample urban data
 city_data = {
 "City": "Chennai",
 "Population": 1000000,
 "Traffic Level": "Moderate",
 "Green Space (%)": 22
 }
 # Zone assignment logic based on simple rules (simulated AI)
 def assign_zone(pop_density, green_space):
 if green_space > 30:
 return "Green"
 elif pop_density > 10000:
 return "Residential"
 elif 5000 < pop_density <= 10000:
 return "Commercial"
 else:
 return "Industrial"
# Subtitle: 2. Chatbot Interaction (Chatbot Equivalent)
def urban_chatbot(user_input):
 user_input = user_input.lower()
 if "green" in user_input:
 return "Green zones are crucial for improving air quality and urban 
aesthetics. Chennai has 22% green cover."
 elif "residential" in user_input or "blue" in user_input:
 return "Residential zones are expanding. Consider population density and 
proximity to green space."
 elif "commercial" in user_input or "green" in user_input:
 return "Commercial zones need easy access and good traffic flow. Focus on 
public transport integration."
 elif "industrial" in user_input or "gray" in user_input:
 return "Industrial zones should be placed away from residential areas to 
reduce pollution impact."
 elif "traffic" in user_input:
 return f"Current traffic condition is '{city_data['Traffic Level']}'. 
Infrastructure upgrades are recommended."
 elif "population" in user_input:
 return f"The current population is around {city_data['Population']}. Plan 
for future growth."
else:
 return "I can help with zone types like Residential, Commercial, Industrial,
Green, or with traffic/population info."
# Subtitle: 3. IoT Integration (Optional)
# Simulated Smart City Sensors
def get_extended_sensor_data():
 return {
 "Traffic Congestion": random.choice(["Low", "Moderate", "High"]),
 "Air Quality Index": random.randint(50, 150),
 "Noise Level (dB)": random.randint(40, 90),
 "Temperature (°C)": round(random.uniform(28.0, 38.0), 2)
 }
sensor_data = get_extended_sensor_data()
print("IoT Sensor Data Feed:", sensor_data)
# Subtitle: 4. Data Security Implementation
key = Fernet.generate_key()
 cipher = Fernet(key)
 city_info = f"{city_data['City']}, Population: {city_data['Population']}, Green 
Space: {city_data['Green Space (%)']}%"
 encrypted_data = cipher.encrypt(city_info.encode())
 print("Encrypted City Data:", encrypted_data)
# Subtitle: 5. Testing and Feedback
assert assign_zone(12000, 20) == "Residential"
 assert assign_zone(8000, 15) == "Commercial"
 assert assign_zone(2000, 35) == "Green"
 print("Zone assignment logic passed all tests.")
# Subtitle: Urban Zone Mapping (Map Visualization)
start_lat = 13.0827
 start_lon = 80.2707
 city_map = folium.Map(location=[start_lat, start_lon], zoom_start=13)
 zones = ["Residential", "Commercial", "Industrial", "Green"]
 zone_colors = {
 "Residential": "blue",
 "Commercial": "green",
 "Industrial": "gray",
 "Green": "darkgreen"
 }
 for i in range(4):
 for j in range(4):
 lat = start_lat + (i * 0.01)
     lon = start_lon + (j * 0.01)
 zone_type = zones[(i + j) % 4]
 folium.Marker(
 [lat, lon],
 popup=f"Zone: {zone_type}",
 icon=folium.Icon(color=zone_colors[zone_type])
 ).add_to(city_map)
 map_file = "urban_map_jupyter.html"
 city_map.save(map_file)
 print(" Urban Planning Stats:")
 for key, value in city_data.items():
 print(f"{key}: {value}")
 display(IFrame(map_file, width='100%', height='500'))
# Basic text-based chatbot
user_query = input("Ask about urban planning (e.g., green, traffic, population): ")
response = urban_chatbot(user_query)
print("Assistant:", response)


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
