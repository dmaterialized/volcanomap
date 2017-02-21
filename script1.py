#creates volcano map
import folium
import pandas

# initialize pandas
df=pandas.read_csv("Volcanoes-USA.txt")

    #initialize folium


map=folium.Map(location=[45.362,-121.697],zoom_start=12,tiles='Stamen Terrain')

# add markers
#map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows', marker_color='red')
#map.simple_marker(location=[45.3311,-121.7311],popup='Timberlake Lodge', marker_color='green')


# add Portland for fun
map.simple_marker(location=[45.5231,-122.6765],popup='Portland, OR', marker_color='white')

for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
    map.simple_marker(location=[lat,lon],popup=name, marker_color='blue')


# build the file
map.create_map(path='pymap.html')
