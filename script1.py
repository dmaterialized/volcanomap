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
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev))))

# add Portland for fun
map.add_child(folium.Marker(location=[45.5231,-122.6765],popup='Portland, OR', icon=folium.Icon(color=color(elev))))

# build the file
map.save(outfile='pymap.html')

# all done - confirm!
print("file saved!")
