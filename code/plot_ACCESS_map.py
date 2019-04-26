#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:07:08 2019

@author: Ewan
"""

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

ax.set_extent([65, 184.57, -65, -916.95], crs=ccrs.PlateCarree())
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

# Plot ACCESS grid map
tMin = -15
tMax = 2228
tStep = 200

tStepOcean = 1000
tMinOcean = -15000
tMaxOcean = 0

csetLand = ax.contourf(
        X_coarse, Y_coarse, elav_coarse, cmap='pink_r', levels=np.arange(-tStep,tMax+tStep,tStep), zorder=0
        )
# fig.colorbar(csetLand)
csetWater = ax.contourf(
        X_coarse, Y_coarse, elav_coarse, cmap='Blues_r',
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

#plt.show()

plt.savefig('./ACCESS_map' + '.png', format='png', dpi=300)