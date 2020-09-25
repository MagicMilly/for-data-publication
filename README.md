# Weather data README for the [GenoPhenoEnvo](https://genophenoenvo.github.io/) Project

_trait data and metadata are still being updated and have been removed temporarily from this README_

==============================

This repository contains source code and processed climate data for the [GenoPhenoEnvo](https://github.com/genophenoenvo) project. This repository supports one of our goals to provide open data and reproducible code in order to follow [FAIR](https://www.go-fair.org/fair-principles/) data principles and contribute to open science.

### Weather Data

Contains the weather data during season dates for sorghum experiments at these locations

- Maricopa Agricultural Center, University of Arizona, Season 4
    - Coordinates: 33.069, -111.972
    - Elevation: 362 meters
    - Planting: 2017-04-20, Day 110
    - Last Day of Harvest: 2017-09-16, Day 259
- Maricopa Agricultural Center, University of Arizona, Season 6
    - Coordinates: 33.068941, -111.972244
    - Elevation: 362 meters
    - Planting: 2018-04-25, Day 115
    - Harvest: 2018-08-01, Day 213
- Kansas State University, Ashland Bottoms
    - Coordinates: 39.126, -96.677
    - Elevation: 325 meters
    - Planting: 2016-06-17, Day 169
    - Harvest: 2016-10-21, Day 295
- Clemson University Pee Dee Research and Education Center, South Carolina
    - Coordinates: 34.289, -79.737 
    - Elevation: 42 meters
    - Planting: 2014-05-06, Day 126
    - Latest date in Clemson trait data: 2014-10-15, Day 288

#### Parameters and Units

- Date: YYYY-MM-DD format
- Day of year
- Minimum temperature: Celsius
- Maximum temperature: Celsius
- Mean temperature: Celsius
- Accumulated growing degree days (gdd): heat units
    - 10 degrees Celsius is base temperature for sorghum
    - Daily gdd value = ``((max temp + min temp) / 2) - 10 (base temperature)``
    - Accumulated growing degree days = cumulative sum of daily gdd values
- Minimum relative humidity: percentage
- Maximum relative humidity: percentage
- Mean relative humidity: percentage
- Vapor pressure deficit: Kilopascals
    ```
    es = (6.11 * np.exp((2500000/461) * (1/273 - 1/(273 + temp_avg))))
    vpd = (((100 - rh_avg)/1000) * es)
    ```
- Precipitation: millimeters
- Cumulative precipitation: millimeters
- First water deficit treatment: boolean value
    - `True` values only found in MAC Season 4
- Second water deficit treatment: boolean value
    - `True` values only found in MAC Season 4

Information about MAC season 4 water deficit treatments can be found [here](https://terraref.ncsa.illinois.edu/bety/api/v1/experiments?name=~MAC+Season+4:+All+BAP+With+Late+Season+Drought)

#### Raw weather data CyVerse downloads

These urls will start an **automatic** download, which were used in the weather data cleaning code

- [MAC season 4 weather](https://de.cyverse.org/dl/d/7D6C8FD6-EF77-437C-89E6-412EA8C3EEC6/mac_weather_station_raw_daily_2017.csv)
- [MAC season 6 weather](https://de.cyverse.org/dl/d/233C21D5-1306-4028-9CF9-FF4AF0EAC405/mac_weather_station_raw_daily_2018.csv)
- [KSU hourly weather](https://de.cyverse.org/dl/d/D80C07D7-5F68-4C86-B15A-9BAAF472D3A4/ksu_hourly_weather.csv)
- [KSU daily weather](https://de.cyverse.org/dl/d/64805E3B-0460-4AA1-8D8A-2D7246E05B35/ashland_bottoms_daily_weather_2016.csv)
- [Clemson daily temperatures](https://de.cyverse.org/dl/d/19836AB5-9223-4CBA-B56E-46272CACF5A3/clemson_temps_daily.csv)
- [Clemson daily relative humidity](https://de.cyverse.org/dl/d/353F5386-4D88-45A9-A4F6-6FC66C64C7E8/clemson_rh_daily.csv)

#### Raw weather data sources
- [Maricopa (Arizona) Agricultural Center](https://cals.arizona.edu/azmet/06.htm)
- [Kansas Mesonet](http://mesonet.k-state.edu/)
- NASA [Daymet](https://daymet.ornl.gov/) - can search by coordinates
- [Climate Engine](http://climateengine.org/data) - can search by coordinates

#### Data Processing

- Weather data that could not be found in all four seasons were dropped during processing, but can be accessed in the raw data 
- The Python3 code used to process weather data can be found in the Jupyter notebook `weather_data_cleaning.ipynb`. All cells can be run to produce the processed output files:
    - `mac_season_4_weather.csv`
    - `mac_season_6_weather.csv`
    - `ksu_weather.csv`
    - `clemson_weather.csv`
- These processed data can also be downloaded directly from CyVerse using these automatic download links
    - MAC season 4 https://de.cyverse.org/dl/d/6D959379-0442-41FE-8BEE-890866ACF037/mac_season_4_weather.csv
    - MAC season 6 https://de.cyverse.org/dl/d/C6219045-8114-4068-B924-8C2CD54AB9FD/mac_season_6_weather.csv
    - KSU https://de.cyverse.org/dl/d/F53F6574-CE80-408E-B8C8-8983CB287F96/ksu_weather.csv
    - Clemson https://de.cyverse.org/dl/d/1EB28C81-10A1-4E1B-A406-1D0C6A20AF2D/clemson_weather.csv
