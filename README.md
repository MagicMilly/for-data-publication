For data publication with UA Library Data Repo
==============================

This project contains source code, other related files, and small, derived datasets for the NSF-funded [GenoPhenoEnvo](https://github.com/genophenoenvo) project. This repo supports one of our goals to provide open data and reproducible code in order to follow [FAIR](https://www.go-fair.org/fair-principles/) data principles and contribute to open science.

### Raw Data
The raw input trait data queried from betydb live on [CyVerse](https://cyverse.org/), in addition to environmental data downloaded from weather stations. All links will start an **automatic download** from CyVerse of the selected dataset. 
- Clemson 2014 trait [data](https://de.cyverse.org/dl/d/E5B8AC50-B1D1-4254-932D-F04CA0D1DF3E/clemson_data_2020-06-01.csv)
- Clemson 2014 weather [data](https://de.cyverse.org/dl/d/B6FF28EF-ACA0-4CA7-89EA-30F624003607/clemson_weather_daily_2014.csv) from Florence Regional Airport, SC 
- Maricopa Agricultural Center (MAC) Season 4 trait [data](https://de.cyverse.org/dl/d/D3168AC5-82BE-436E-B8B5-AB8DD78CAF28/mac_season_four_2020-04-22.csv)
- MAC Weather Station daily [values](https://de.cyverse.org/dl/d/6FAC2D4E-BD63-4801-95BB-C4FD4031104A/mac_weather_station_raw_daily_2017.csv) for 2017 (Season 4)
- MAC Season 6 trait [data](https://de.cyverse.org/dl/d/C14BF1DE-9FD3-4559-AC3E-7858CE392E3A/mac_season_six_2020-04-22.csv)
- MAC Weather Station daily [values](https://de.cyverse.org/dl/d/8A15BCF5-6A57-412B-AE46-22DE18CE730C/mac_weather_station_raw_daily_2018.csv) for 2018 (Season 6)

#### Environmental Data
To download raw weather data from the original source:
- Maricopa Agricultural Center [Weather Station](https://cals.arizona.edu/azmet/06.htm)
- Manhattan Weather [Data](https://mesonet.k-state.edu/weather/historical/) (for KSU Ashland Bottoms Experiment)
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
Used for input data

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
	- mean (value of particular trait)
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
	- mean (value of particular trait)
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
