import numpy as np
import pandas as pd
# ma is "masked array" - this is what the netCDF4 module uses
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib import rcParams
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import pickle
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import xarray as xr

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

fig = plt.figure(figsize=(5,4))
#fig.set_tight_layout(True)

ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.coastlines(resolution='50m', zorder=0)

ax.set_extent([110, 156, -46, -9], crs=ccrs.PlateCarree())
grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.4, linestyle='--',
                  )

colour_list = plt.cm.Set3(np.linspace(0,1,11))

c_land = tuple(np.array([249.0, 246.0, 216.0])/256)
c_water = tuple(np.array([220.0, 240.0, 250.0])/256)

land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m',
                                        edgecolor='face',
                                        facecolor=c_land)

ocean_50m = cfeature.NaturalEarthFeature('physical', 'ocean', '50m',
                                        edgecolor='face',
                                        facecolor=c_water)

lakes_50m = cfeature.NaturalEarthFeature('physical', 'lakes', '50m',
                                        edgecolor='face',
                                        facecolor=c_water)

states_provinces_50m = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')

land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m',
                                        edgecolor='face',
                                        facecolor=c_land)

ocean_10m = cfeature.NaturalEarthFeature('physical', 'ocean', '10m',
                                        edgecolor='face',
                                        facecolor=c_water)

lakes_10m = cfeature.NaturalEarthFeature('physical', 'lakes', '10m',
                                        edgecolor='face',
                                        facecolor=c_water)

states_provinces_10m = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')

#ax.add_feature(land_50m, edgecolor='black', linewidth = 0.5, zorder=0)
#ax.add_feature(ocean_50m, edgecolor='black', linewidth = 0.5, zorder=0)

elav = xr.open_dataset('etopo1.nc')
lon = elav.lon.values
lat = elav.lat.values



[X, Y] = np.meshgrid(elav.lon, elav.lat)

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
            edgecolor='black', s=20, linewidth=.75, label=labels[i]
            )

    ax.scatter(
            airports[i].LONGITUDE, airports[i].LATITUDE,
            marker='*', color=colour_list[i], transform=ccrs.PlateCarree(),
            edgecolor='black', s=140, linewidth=.75,
            )

ax.scatter(
        wa_coastal_south_df.LONGITUDE.values, wa_coastal_south_df.LATITUDE.values,
        marker='o', color=colour_list[8], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.75, label='South WA'
        )

ax.scatter(
        wa_coastal_north_df.LONGITUDE.values, wa_coastal_north_df.LATITUDE.values,
        marker='o', color=colour_list[9], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.75, label='North WA'
        )

ax.scatter(
        hobart_ap_stations_df.LONGITUDE.values, hobart_ap_stations_df.LATITUDE.values,
        marker='o', color=colour_list[7], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.75, label='TAS'
        )

ax.scatter(
        canberra_ap_stations_df.LONGITUDE.values, canberra_ap_stations_df.LATITUDE.values,
        marker='o', color=colour_list[6], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.75, label='ACT'
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

tMin = -15
tMax = 2228
tStep = 200

tStepOcean = 1000
tMinOcean = -15000
tMaxOcean = 0

csetLand = ax.contourf(
        X,Y,elav.Band1, cmap='pink_r', levels=np.arange(-tStep,tMax+tStep,tStep), zorder=0
        )
fig.colorbar(csetLand)
csetWater = ax.contourf(
        X,Y,elav.Band1, cmap='Blues_r',
        levels=np.arange(tMinOcean,tMaxOcean+tStepOcean,tStepOcean),
        zorder=0
        )
fig.colorbar(csetWater)
ax.add_feature(lakes_50m, edgecolor='black', linewidth = 0.5, zorder=0)
ax.add_feature(states_provinces_50m, edgecolor='black', zorder=0)


fig.legend()

grid.xlocator = mticker.FixedLocator(
    np.arange(100, 180, 10)
)
grid.ylocator = mticker.FixedLocator(
    np.arange(-60, 20, 10)
)

grid.xlabels_top = False
grid.ylabels_right = False
grid.xformatter = LONGITUDE_FORMATTER
grid.yformatter = LATITUDE_FORMATTER

plt.show()

plt.savefig('./station_map.svg')

lat_min = [-13.4, -28.2, -34.2, -38.7, -32.4, -35.4, -43.6, -37]
lat_max = [-11, -26.2, -33.7, -37.5, -31.6, -34.35, -42.4, -34]
lon_min = [129.7, 152, 150.6, 144.2, 115.2, 138, 146.8, 147.5]
lon_max = [132.1, 154, 151.4, 145.5, 116.5, 139, 148.2, 151]

tick = [1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
#
## Create Victorian Station Map
#for i in np.arange(0,len(airport_stations)):
#
#    fig = plt.figure(figsize=(4,3))
#
#    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#
#    ax.set_extent([lon_min[i], lon_max[i], lat_min[i], lat_max[i]], crs=ccrs.PlateCarree())
#    grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
#                      linewidth=1, color='gray', alpha=0.4, linestyle='--',
#                      )
#    grid.xlocator = mticker.FixedLocator(
#            np.arange(np.floor(lon_min[i])-1, np.ceil(lon_max[i])+1, tick[i])
#            )
#    grid.ylocator = mticker.FixedLocator(
#            np.arange(np.floor(lat_min[i])-1, np.ceil(lat_max[i])+1, tick[i])
#            )
#    grid.xlabels_top = False
#    grid.ylabels_right = False
#    grid.xformatter = LONGITUDE_FORMATTER
#    grid.yformatter = LATITUDE_FORMATTER
#
#    colour_list = plt.cm.Set3(np.linspace(0,1,11))
#
##    ax.add_feature(land_10m, edgecolor='black', linewidth = 0.75, zorder=0)
##    ax.add_feature(ocean_10m, edgecolor='black', linewidth = 0.75, zorder=0)
#    ax.add_feature(lakes_10m, edgecolor='black', linewidth = 0.75, zorder=0)
#
#    ax.scatter(
#            airport_stations[i].LONGITUDE.values, airport_stations[i].LATITUDE.values,
#            marker='o', color=colour_list[i], transform=ccrs.PlateCarree(),
#            edgecolor='black', s=20, linewidth=.75, label='Melbourne'
#            )
#
#    ax.scatter(
#            airports[i].LONGITUDE,
#            airports[i].LATITUDE,
#            marker='*', color=colour_list[i], transform=ccrs.PlateCarree(),
#            edgecolor='black', s=140, linewidth=.75,
#            )
#
#    cset = ax.contourf(
#        X,Y,elav.Band1, cmap='pink_r', levels=np.arange(-tStep,tMax+tStep,tStep), zorder=0
#        )
#    fig.colorbar(cset)
#    csetWater = ax.contourf(
#        X,Y,elav.Band1, cmap='Blues_r',
#        levels=np.arange(tMinOcean,tMaxOcean+tStepOcean,tStepOcean),
#        zorder=0
#        )
#    fig.colorbar(csetWater)
#    ax.coastlines(resolution='10m', zorder=0, edgecolor='black', linewidth = 0.75)
#    ax.add_feature(states_provinces_10m, edgecolor='black', linewidth = 0.75, zorder=0)
#
#    plt.savefig('./station_map_' + str(i) + '.svg')
#    plt.show()
