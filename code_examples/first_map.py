from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', lat_0=0, lon_0=0,
              resolution='l', area_thresh=1000.0)
 
map.drawcoastlines()
 
plt.show()