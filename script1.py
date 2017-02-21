#creates volcano map
import folium
import pandas

# initialize pandas
df=pandas.read_csv("Volcanoes-USA.txt")

#initialize folium
map=folium.Map(location=[45.362,-121.697],zoom_start=4,tiles='Stamen Terrain')

#create all markers
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon],popup=name, marker_color='green' if elev in range(0,1000) else 'white' if elev in range(1000,2000) else 'orange' if elev in range(2000,3000) else 'red')

# add Portland for fun
map.simple_marker(location=[45.5231,-122.6765],popup='Portland, OR', marker_color='white')

# build the file
map.create_map(path='pymap.html')
