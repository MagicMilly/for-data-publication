For data publication with UA Library Data Repo
==============================

This project contains source code, other related files, and small, derived datasets for the NSF-funded [GenoPhenoEnvo](https://github.com/genophenoenvo) project. This repo supports one of our goals to provide open data and reproducible code in order to follow [FAIR](https://www.go-fair.org/fair-principles/) data principles and contribute to open science.

### Getting Started
The scripts and instructions for accessing data on betydb can be found in [David LeBauer's](https://github.com/dlebauer) Google [drive](https://drive.google.com/drive/folders/1uiHKZDTeYERBkyqHEuzrptCB7Wz0sp5w?usp=sharing) for his data publication.

### Additional Metadata
- More comprehensive metadata for MAC Seasons 4 and 6 include germplasms, methods, and variables, and can also be found in the same Google [drive](https://drive.google.com/drive/folders/16ZJcvwHV96_20BuuhhhnlCYF_mnkSjSl?usp=sharing).
- The cultivar lookup [table](https://github.com/MagicMilly/for-data-publication/blob/main/data/processed/cultivar_lookup_table_2020-06-12T104808.csv) has a list of all cultivars from MAC Seasons 4 and 6, the KSU Experiment, and those described in the Brenton et al. 2016 [paper](https://www.genetics.org/content/204/1/21). 


### Raw Data
The raw input trait data queried from betydb live on [CyVerse](https://cyverse.org/), in addition to environmental data downloaded from weather stations. All links will start an **automatic download** from CyVerse of the selected dataset. 
- Clemson 2014 trait [data](https://de.cyverse.org/dl/d/E5B8AC50-B1D1-4254-932D-F04CA0D1DF3E/clemson_data_2020-06-01.csv)
- Clemson 2014 weather [data](https://de.cyverse.org/dl/d/B6FF28EF-ACA0-4CA7-89EA-30F624003607/clemson_weather_daily_2014.csv) from Florence Regional Airport, SC 
- Maricopa Agricultural Center (MAC) Season 4 trait [data](https://de.cyverse.org/dl/d/D3168AC5-82BE-436E-B8B5-AB8DD78CAF28/mac_season_four_2020-04-22.csv)
- MAC Weather Station daily [values](https://de.cyverse.org/dl/d/6FAC2D4E-BD63-4801-95BB-C4FD4031104A/mac_weather_station_raw_daily_2017.csv) for 2017 (Season 4)
- MAC Season 6 trait [data](https://de.cyverse.org/dl/d/C14BF1DE-9FD3-4559-AC3E-7858CE392E3A/mac_season_six_2020-04-22.csv)
- MAC Weather Station daily [values](https://de.cyverse.org/dl/d/8A15BCF5-6A57-412B-AE46-22DE18CE730C/mac_weather_station_raw_daily_2018.csv) for 2018 (Season 6)
- KSU Ashland Bottoms Season 6 trait [Data](https://de.cyverse.org/dl/d/018B11DA-28E7-46B8-88D9-4481904FFBA7/ksu_data_2020-06-11.csv) (2016)
- KSU Ashland Bottoms Daily Weather [data](https://de.cyverse.org/dl/d/7DDD1490-C380-4512-96E9-FE7E24251506/ashland_bottoms_daily_weather_2016.csv) for 2016

#### Environmental Data
To download raw weather data from the original source:
- Maricopa Agricultural Center [Weather Station](https://cals.arizona.edu/azmet/06.htm)
- Ashland Bottoms Weather Station [Data](https://mesonet.k-state.edu/weather/historical/) (for KSU Ashland Bottoms Season 6 Experiment)
- Brenton et al. 2016 Clemson Weather [Data](https://www.ncdc.noaa.gov/cdo-web/datasets#GHCND) - collected from Florence, SC Regional Airport. Note: this NOAA climate data must be requested from the site, which is then sent to the provided e-mail address once processed. 

### Metadata

#### Licenses
Data and other documents are licensed under CC-By. All software is licensed under MIT.

### Folder and File Structures

#### data/
- raw/
  - data downloaded from betydb and MAC weather station and used for transformation and curation
- interim/
  - cleaned and formatted environmental data that were used to process final data products
- processed/
  - final curated data products

#### data/raw/

The raw input trait data used in the notebooks were queried from betydb and live in [CyVerse](https://cyverse.org/), in addition to environmental data downloaded from weather stations. All links will start an **automatic download** from CyVerse of the selected dataset.

- Clemson 2014 trait [data](https://de.cyverse.org/dl/d/E5B8AC50-B1D1-4254-932D-F04CA0D1DF3E/clemson_data_2020-06-01.csv)
- Clemson 2014 weather [data](https://de.cyverse.org/dl/d/B6FF28EF-ACA0-4CA7-89EA-30F624003607/clemson_weather_daily_2014.csv) from Florence Regional Airport, SC - these data will be updated to reflect a location closer to the Pee Dee Research Center with additional environmental variables
- Maricopa Agricultural Center (MAC) Season 4 trait [data](https://de.cyverse.org/dl/d/D3168AC5-82BE-436E-B8B5-AB8DD78CAF28/mac_season_four_2020-04-22.csv)
- MAC Weather Station daily [values](https://de.cyverse.org/dl/d/6FAC2D4E-BD63-4801-95BB-C4FD4031104A/mac_weather_station_raw_daily_2017.csv) for 2017 (Season 4)
- MAC Season 6 trait [data](https://de.cyverse.org/dl/d/C14BF1DE-9FD3-4559-AC3E-7858CE392E3A/mac_season_six_2020-04-22.csv)
- MAC Weather Station daily [values](https://de.cyverse.org/dl/d/8A15BCF5-6A57-412B-AE46-22DE18CE730C/mac_weather_station_raw_daily_2018.csv) for 2018 (Season 6)
- KSU Ashland Bottoms Season 6 trait [Data](https://de.cyverse.org/dl/d/018B11DA-28E7-46B8-88D9-4481904FFBA7/ksu_data_2020-06-11.csv) (2016)
- KSU Ashland Bottoms Daily Weather [data](https://de.cyverse.org/dl/d/7DDD1490-C380-4512-96E9-FE7E24251506/ashland_bottoms_daily_weather_2016.csv) for 2016

#### Environmental Data
To download raw weather data from the original source:
- Maricopa Agricultural Center [Weather Station](https://cals.arizona.edu/azmet/06.htm)
- Ashland Bottoms Weather Station [Data](https://mesonet.k-state.edu/weather/historical/) (for KSU Ashland Bottoms Season 6 Experiment)
- Brenton et al. 2016 Clemson Weather [Data](https://www.ncdc.noaa.gov/cdo-web/datasets#GHCND) (_which will be updated, using a different source_) - collected from Florence, SC Regional Airport. Note: this NOAA climate data must be requested from the site, which is then sent to the provided e-mail address once processed. 

#### Description of raw data files

- mac_season_four: Non-null columns include 
	- result type
	- id
	- citation id
	- site id
	- treatment id
	- sitename
	- city
	- latitude
	- longitude
	- scientific name
	- common name
	- genus
	- species id
	- cultivar id
	- author
	- citation year
	- treatment
	- date (AZ)
	- time
	- raw date (UTC)
	- month
	- year
	- dateloc
	- trait
	- trait description
	- mean (value of particular trait, not an average)
	- units
	- notes
	- access level
	- cultivar
	- entity
	- method name
	- view url
	- edit url

- mac_weather_station_raw_daily_2017 (season 4): Columns include 
	- year
	- day of year
	- station number
	- daily min, max, and average values for 
		- air temperature in Celsius
		- relative humidity (rh)
		- 4 inch soil temperature in Celsius
		- 20 inch soil temperature in Celsius
	- average values for 
		- vapor pressure deficit (vpd)
		- wind speed
		- vapor pressure
		- dew point 
	- solar radiation total
	- precipitation total
	- wind vector magnitude
	- wind vector direction
	- wind direction standard deviation (wind_direction_std)
	- max wind speed
	- heat units
	- original AZMET evapotranspiration (eto_azmet)
	- Penman-Monteith evapotranspiration (eto_pm)
    
- mac_season_six: Non-null columns include 
	- result type
	- id
	- citation id
	- site id
	- treatment id
	- sitename
	- city
	- latitude
	- longitude
	- scientific name
	- common name
	- genus
	- species id
	- cultivar id
	- author
	- citation year
	- treatment
	- date (AZ)
	- time
	- raw date (UTC)
	- month
	- year
	- dateloc
	- trait
	- trait description
	- mean (value of particular trait, not an average)
	- units
	- notes
	- access level
	- cultivar
	- entity
	- method name
	- view url
	- edit url

- mac_weather_station_raw_daily_2018: Columns include 
	- year
	- day of year
	- station number
	- daily min, max, and average values for 
		- air temperature in Celsius
		- relative humidity (rh)
		- 4 inch soil temperature in Celsius
		- 20 inch soil temperature in Celsius
	- average values for 
		- vapor pressure deficit (vpd)
		- wind speed
		- vapor pressure
		- dew point 
	- solar radiation total
	- precipitation total
	- wind vector magnitude
	- wind vector direction
	- wind direction standard deviation (wind_direction_std)
	- max wind speed
	- heat units
	- original AZMET evapotranspiration (eto_azmet)
	- Penman-Monteith evapotranspiration (eto_pm)

- ksu_data: Non-null columns include
    - result type
    - id
    - citation id
    - site id
    - treatment id
    - sitename
    - city
    - latitude
    - longitude
    - scientific name
    - common name
    - genus
    - species id
    - cultivar id
    - author
    - citation year
    - treatment
    - date
    - time
    - raw date
    - month
    - year
    - dateloc
    - trait
    - trait description
    - mean (value for that particular trait, not an average)
    - units (measurements used for the "mean" value in the previous column)
    - notes
    - access level
    - cultivar
    - method name
    - view url
    - edit url

- ashland_bottoms_daily_weather_2016 (for ksu data): Columns for daily values include
    - timestamp
    - station
    - air temperature max - Celsius
    - air temperature min - Celsius
    - average relative humidity - percentage
    - precipitation - mm
    - average wind speed - m/s
    - max wind speed - m/s
    - max soil temperature at 5 cm - Celsius
    - min soil temperature at 5 cm - Celsius
    - max soil temperature at 10 cm - Celsius
    - min soil temperature at 10 cm - Celsius
    - total solar radiation - MJ/m²
    - evapotranspiration for grass - mm
    - evapotranspiration for alfalfa - mm

- clemson_data: Non-null columns include
    - result type
    - id
    - citation id
    - site id
    - treatment id
    - sitename
    - city
    - latitude
    - longitude
    - scientific name
    - common name
    - genus
    - species id
    - cultivar id
    - author
    - citation year
    - treatment
    - date (UTC)
    - raw date
    - month
    - year
    - dateloc
    - trait
    - trait description
    - mean (value for a particular trait, not an average)
    - units (for the "mean" value in the previous column)
    - access level
    - cultivar
    - view url
    - edit url

- clemson_weather_daily_2014 - these data will be replaced and updated

#### data/processed/
This section includes descriptions of how raw data were transformed and the resulting data products. One common change to the raw data includes dropping columns that only contain a single value (i.e., author, redundant date columns). Currently, the traits we are focused on for a machine learning model include aboveground dry biomass, days to flowering, days to flag leaf emergence, and canopy height. 

- aboveground_dry_biomass_mac_season_4
    - Null columns dropped
        - n
        - statname
        - stat
    - Columns dropped with only one value
        - result type: `trait`
        - city: `Maricopa`
        - scientific name: `Sorghum bicolor`
        - common name: `sorghum`
        - genus: `Sorghum`
        - species id: `2588`
        - year: `2017`
        - dateloc: `5.`
    - Columns dropped due to having a small number of unique values
        - citation id: `6000000008`, `6000000016`, `6000000011`
        - treatment id: `6000000024`, `6000000026`
        - author: `Zongyang, Li`, `Zeyu Zhang`, `Newcomb, Maria`
        - citation year: `2016`, `2017`, `2019`
        - access level (to the data, before publication): `2`, `4`
    - Columns dropped which are currently not relevant to analysis and / or redundant:
        - Unnamed: 0
        - checked
        - id
        - site id
        - cultivar id
        - time
        - raw date
        - month
        - notes
        - entity
        - view url
        - edit url
    - Columns which were kept and/or modified
        - date: converted from string to datetime object
        - sitename: indicates the location of the plant within the field
        - range: location identifier also found in the sitename
        - column: location identifier also found in the sitename
        - lat
        - lon
        - treatment: indicates date ranges for water-deficit stress
        - cultivar
        - aboveground dry biomass: this column contains the values
        - units: kg/ha
- aboveground_dry_biomass_season_6
- canopy_height_season_6
- canopy_height_season_4
- clemson_aboveground_dry_biomass
- clemson_canopy_heights
- clemson_days_to_flowering
- cultivar_lookup_table
- days_gdd_to_flag_leaf_emergence_season_4
- days_gdd_to_flowering_season_4
- ksu_canopy_heights
- ksu_flowering

    








Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
