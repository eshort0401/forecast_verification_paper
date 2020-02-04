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
    sydney_ap_stations_df,
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
colour_list_alt = plt.cm.Set3(np.linspace(0,1,11))
colour_list_alt[6:8] = colour_list_alt[8:10]

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

# Coarsen elavation dataset
coarsen_step_coarse = 10
coarsen_step_fine = 2

elav = xr.open_dataset('etopo1.nc')
lon = elav.lon.values
lat = elav.lat.values
elav = elav.Band1.values

nLon_coarse = len(lon)//coarsen_step_coarse
nLat_coarse = len(lat)//coarsen_step_coarse

nLon_fine = len(lon)//coarsen_step_fine
nLat_fine = len(lat)//coarsen_step_fine

elav_coarse = np.empty((nLat_coarse, nLon_coarse))
elav_fine = np.empty((nLat_fine, nLon_fine))

for i in np.arange(0, nLat_coarse):
    for j in np.arange(0, nLon_coarse):
        elav_coarse[i,j] = np.mean(elav[i * coarsen_step_coarse : (i+1) * coarsen_step_coarse,
                                   j * coarsen_step_coarse : (j+1) * coarsen_step_coarse])

for i in np.arange(0, nLat_fine):
    for j in np.arange(0, nLon_fine):
        elav_fine[i,j] = np.mean(elav[i * coarsen_step_fine : (i+1) * coarsen_step_fine,
                                   j * coarsen_step_fine : (j+1) * coarsen_step_fine])

lon_coarse = np.mean(lon[:(len(lon)//coarsen_step_coarse)*coarsen_step_coarse].reshape(-1,coarsen_step_coarse), axis=1)
lat_coarse = np.mean(lat[:(len(lat)//coarsen_step_coarse)*coarsen_step_coarse].reshape(-1,coarsen_step_coarse), axis=1)

lon_fine = np.mean(lon[:(len(lon)//coarsen_step_fine)*coarsen_step_fine].reshape(-1,coarsen_step_fine), axis=1)
lat_fine = np.mean(lat[:(len(lat)//coarsen_step_fine)*coarsen_step_fine].reshape(-1,coarsen_step_fine), axis=1)

[X_coarse, Y_coarse] = np.meshgrid(lon_coarse, lat_coarse)
[X_fine, Y_fine] = np.meshgrid(lon_fine, lat_fine)

coastal_stations = [
    nt_coastal_df, qld_coastal_df, nsw_coastal_df, vic_coastal_df,
    wa_coastal_west_df, sa_coastal_df
    ]

airport_stations = [
    darwin_ap_stations_df, brisbane_ap_stations_df,
    sydney_ap_stations_df, melbourne_ap_stations_df,
    perth_ap_stations_df, adelaide_ap_stations_df,
    hobart_ap_stations_df,
    ]

airports = [
    darwin_ap_stations_df.loc[14015], brisbane_ap_stations_df.loc[40842],
    sydney_ap_stations_df.loc[66037], melbourne_ap_stations_df.loc[86282],
    perth_ap_stations_df.loc[9021], adelaide_ap_stations_df.loc[23034],
    hobart_ap_stations_df.loc[94008],
    ]

labels = [
        'NT', 'QLD', 'NSW',
        'VIC', 'West WA', 'SA',
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
        marker='o', color=colour_list[6], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.75, label='South WA'
        )

ax.scatter(
        wa_coastal_north_df.LONGITUDE.values, wa_coastal_north_df.LATITUDE.values,
        marker='o', color=colour_list[7], transform=ccrs.PlateCarree(),
        edgecolor='black', s=20, linewidth=.75, label='North WA'
        )

# ax.scatter(
#         hobart_ap_stations_df.LONGITUDE.values, hobart_ap_stations_df.LATITUDE.values,
#         marker='o', color=colour_list[8], transform=ccrs.PlateCarree(),
#         edgecolor='black', s=20, linewidth=.75, label='TAS'
#         )
#
# ax.scatter(
#         canberra_ap_stations_df.LONGITUDE.values, canberra_ap_stations_df.LATITUDE.values,
#         marker='o', color=colour_list[9], transform=ccrs.PlateCarree(),
#         edgecolor='black', s=20, linewidth=.75, label='ACT'
#         )
#
# ax.scatter(
#         hobart_ap_stations_df.loc[94008].LONGITUDE,
#         hobart_ap_stations_df.loc[94008].LATITUDE,
#         marker='*', color=colour_list[8], transform=ccrs.PlateCarree(),
#         edgecolor='black', s=140, linewidth=.75,
#         )
#
# ax.scatter(
#         canberra_ap_stations_df.loc[70351].LONGITUDE,
#         canberra_ap_stations_df.loc[70351].LATITUDE,
#         marker='*', color=colour_list[9], transform=ccrs.PlateCarree(),
#         edgecolor='black', s=140, linewidth=.75,
#         )

tMin = -15
tMax = 2228
tStep = 200

tStepOcean = 1000
tMinOcean = -15000
tMaxOcean = 0

csetLand = ax.contourf(
        X_fine, Y_fine, elav_fine, cmap='pink_r', levels=np.arange(-tStep,tMax+tStep,tStep), zorder=0
        )
# fig.colorbar(csetLand)
csetWater = ax.contourf(
        X_fine, Y_fine, elav_fine, cmap='Blues_r',
        levels=np.arange(tMinOcean,tMaxOcean+tStepOcean,tStepOcean),
        zorder=0
        )
# fig.colorbar(csetWater)
ax.add_feature(lakes_50m, edgecolor='black', linewidth = 0.5, zorder=0)
ax.add_feature(states_provinces_50m, edgecolor='black', zorder=0)

# fig.legend()

grid.xlocator = mticker.FixedLocator(
    np.arange(100, 180, 5)
)
grid.ylocator = mticker.FixedLocator(
    np.arange(-60, 20, 5)
)

grid.xlabels_top = False
grid.ylabels_right = False

grid_labels=True

if grid_labels:
    grid.xformatter = LONGITUDE_FORMATTER
    grid.yformatter = LATITUDE_FORMATTER
else:
    grid.xlabels_bottom = False
    grid.ylabels_left = False

# plt.show()

plt.savefig('./station_map' + '.png', format='png', dpi=300)
# plt.savefig('./station_map' + '.svg', format='svg')

lat_min = [-13.25, -28.25, -34.375, -38.5, -32.5, -35.5, -43.75, -36.75]
lat_max = [-11.25, -26.25, -33.375, -37, -31.5, -34, -42.25, -34.25]
lon_min = [130, 152, 150.5, 144.25, 115.25, 137.5, 146.75, 148.125]
lon_max = [132.0, 154, 151.5, 145.75, 116.25, 139, 148.25, 150.625]

scale = [2, 2, 1.0, 1.5, 1, 1.5, 1.5, 2.5]

tick = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

# # Create Airport Station Maps
# for i in np.arange(0,0):
#
#    fig = plt.figure(figsize=(scale[i], scale[i]))
#
#    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#
#    ax.set_extent([lon_min[i], lon_max[i], lat_min[i], lat_max[i]], crs=ccrs.PlateCarree())
#    grid = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
#                      linewidth=1, color='gray', alpha=0.4, linestyle='--',
#                      )
#    grid.xlocator = mticker.FixedLocator(
#            np.arange(np.floor(lon_min[i])-tick[i], np.ceil(lon_max[i])+tick[i], tick[i])
#            )
#    grid.ylocator = mticker.FixedLocator(
#            np.arange(np.floor(lat_min[i])-tick[i], np.ceil(lat_max[i])+tick[i], tick[i])
#            )
#    grid.xlabels_top = False
#    grid.ylabels_right = False
#    if grid_labels:
#        grid.xformatter = LONGITUDE_FORMATTER
#        grid.yformatter = LATITUDE_FORMATTER
#    else:
#        grid.xlabels_bottom = False
#        grid.ylabels_left = False
#
#    colour_list = plt.cm.Set3(np.linspace(0,1,11))
#
# #    ax.add_feature(land_10m, edgecolor='black', linewidth = 0.75, zorder=0)
# #    ax.add_feature(ocean_10m, edgecolor='black', linewidth = 0.75, zorder=0)
#    ax.add_feature(lakes_10m, edgecolor='black', linewidth = 0.75, zorder=0)
#
#    ax.scatter(
#            airport_stations[i].LONGITUDE.values, airport_stations[i].LATITUDE.values,
#            marker='o', color=colour_list_alt[i], transform=ccrs.PlateCarree(),
#            edgecolor='black', s=20, linewidth=.75, label='Melbourne'
#            )
#
#    ax.scatter(
#            airports[i].LONGITUDE,
#            airports[i].LATITUDE,
#            marker='*', color=colour_list_alt[i], transform=ccrs.PlateCarree(),
#            edgecolor='black', s=140, linewidth=.75,
#            )
#
#    cset = ax.contourf(
#        X_fine,Y_fine,elav_fine, cmap='pink_r', levels=np.arange(-tStep,tMax+tStep,tStep), zorder=0
#        )
#    csetWater = ax.contourf(
#        X_fine,Y_fine,elav_fine, cmap='Blues_r',
#        levels=np.arange(tMinOcean,tMaxOcean+tStepOcean,tStepOcean),
#        zorder=0
#        )
#    ax.coastlines(resolution='10m', zorder=0, edgecolor='black', linewidth = 0.75)
#    ax.add_feature(states_provinces_10m, edgecolor='black', linewidth = 0.75, zorder=0)
#
#    plt.savefig('./station_map_' + str(i) + '.png', format='png', dpi=300)
