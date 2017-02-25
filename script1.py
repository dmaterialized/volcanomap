#creates volcano map
import folium
import pandas
# initialize pandas
df=pandas.read_csv("Volcanoes-USA.txt")
#initialize folium
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Stamen Terrain')
def color(elev):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col="green"
    elif elev in range(minimum+step,minimum+step*2):
        col="white"
    elif elev in range(minimum+step*2,minimum+step*3):
        col='orange'
    else:
        col='red'
    return col

#create all markers
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon],popup=name,marker_color=color(elev))

# add Portland for fun
map.simple_marker(location=[45.5231,-122.6765],popup='Portland, OR', marker_color='white')

# build the file
map.create_map(path='pymap.html')
