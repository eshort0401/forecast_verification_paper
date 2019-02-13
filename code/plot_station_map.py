import numpy as np
import pandas as pd
# ma is "masked array" - this is what the netCDF4 module uses
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib import rcParams
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import pickle
import cartopy.feature as cfeature

input_file = open("station_df.pkl","rb")
station_df = pickle.load(input_file)

(
    nt_coastal_df, qld_coastal_df, nsw_coastal_df, vic_coastal_df, 
    sa_coastal_df, wa_coastal_south_df, wa_coastal_west_df, 
    wa_coastal_north_df, darwin_ap_stations_df, brisbane_ap_stations_df, 
    sydney_ap_stations_df, canberra_ap_stations_df, 
    melbourne_ap_stations_df, hobart_ap_stations_df,
    adelaide_ap_stations_df, perth_ap_stations_df
) = station_df

rcParams.update({'font.size': 10})
rcParams.update({'font.weight': 'normal'})
rcParams['font.family'] = 'serif'
rcParams.update({'font.serif': 'Times New Roman'})

plt.close('all')

fig = plt.figure(figsize=(4,3))
#fig.set_tight_layout(True)

ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.coastlines(resolution='50m', zorder=0)

ax.set_extent([109, 158, -41, -7], crs=ccrs.LambertCylindrical())
grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.4, linestyle='--',
                  )

colour_list = plt.cm.Set3(np.linspace(0,1,11))

states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')

ax.add_feature(states_provinces, edgecolor='black', zorder=0)

coastal_stations = [
    nt_coastal_df, qld_coastal_df, nsw_coastal_df, vic_coastal_df, 
    wa_coastal_west_df, sa_coastal_df
    ] 

airport_stations = [
    darwin_ap_stations_df, brisbane_ap_stations_df, 
    sydney_ap_stations_df, melbourne_ap_stations_df, 
    perth_ap_stations_df, adelaide_ap_stations_df,
    hobart_ap_stations_df, canberra_ap_stations_df,
    ]

airports = [
    darwin_ap_stations_df.loc[14015], brisbane_ap_stations_df.loc[40842],
    sydney_ap_stations_df.loc[66037], melbourne_ap_stations_df.loc[86282], 
    perth_ap_stations_df.loc[9021], adelaide_ap_stations_df.loc[23034],       
    hobart_ap_stations_df.loc[94008], canberra_ap_stations_df.loc[70351],
    ]

labels = [
        'NT', 'QLD', 'NSW', 
        'VIC', 'SA', 'West WA',  
        ]

#wa_coastal_south_df,
#hobart_ap_stations_df
#canberra_ap_stations_df 

for i in np.arange(0,len(coastal_stations)):
    ax.scatter(
            coastal_stations[i].LONGITUDE.values, coastal_stations[i].LATITUDE.values, 
            marker='o', color=colour_list[i], transform=ccrs.PlateCarree(),
            edgecolor='black', s=20, linewidth=.5, label=labels[i]
            )
    
    ax.scatter(
            airports[i].LONGITUDE, airports[i].LATITUDE, 
            marker='*', color=colour_list[i], transform=ccrs.PlateCarree(),
            edgecolor='black', s=140, linewidth=.75, 
            )

ax.scatter(
        wa_coastal_south_df.LONGITUDE.values, wa_coastal_south_df.LATITUDE.values, 
        marker='o', color=colour_list[6], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.5, label='South WA'
        )    

ax.scatter(
        wa_coastal_north_df.LONGITUDE.values, wa_coastal_north_df.LATITUDE.values, 
        marker='o', color=colour_list[9], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.5, label='North WA'
        )

ax.scatter(
        hobart_ap_stations_df.LONGITUDE.values, hobart_ap_stations_df.LATITUDE.values, 
        marker='o', color=colour_list[7], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.5, label='TAS'
        )    

ax.scatter(
        canberra_ap_stations_df.LONGITUDE.values, canberra_ap_stations_df.LATITUDE.values, 
        marker='o', color=colour_list[6], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.5, label='ACT'
        )

ax.scatter(
        hobart_ap_stations_df.loc[94008].LONGITUDE, 
        hobart_ap_stations_df.loc[94008].LATITUDE, 
        marker='*', color=colour_list[7], transform=ccrs.PlateCarree(),
        edgecolor='black', s=140, linewidth=.75,
        )    

ax.scatter(
        canberra_ap_stations_df.loc[70351].LONGITUDE,
        canberra_ap_stations_df.loc[70351].LATITUDE, 
        marker='*', color=colour_list[6], transform=ccrs.PlateCarree(),
        edgecolor='black', s=140, linewidth=.75,
        )

fig.legend()

grid.xlabels_top = False
grid.ylabels_right = False
grid.xformatter = LONGITUDE_FORMATTER
grid.yformatter = LATITUDE_FORMATTER

plt.savefig('./station_map.svg')

plt.show()
