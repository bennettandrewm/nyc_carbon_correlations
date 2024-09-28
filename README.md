# NYC Carbon Correlations

<p align="center">
<img src="image_files/nyc_exhaust.jfif" width="400" height="400" />
</p>

## Overview
This project is currently under construction. But when complete, it will examine correlations between NYC emissions data and other social and economic data from the city.
<br />

## Quick Links
Click here for a [Video Demo](). 
Click here for [POWER BI Report]().


## Table of Contents TOC
[Google Colab Instruction](#google-colab-instructions)<br />
[Business Case](#business-case)<br />
[Data Understanding](#data-understanding)<br />
[Data Preparation](#data-preparation)<br />
[Modeling](#modeling)<br />
[Evaluation](#evaluation)<br />
[Key Findings](#key-findings)<br />
[Summary](#summary)<br />
[Github Repository](#github-repository)<br />


## Google Colab Instructions
To run this notebook, you'll need a Kaggle log-in and web access to [Google Colab and link to this notebook](). Google Colab is a free, user-friendly platform to run software, specifically data models. Kaggle is a [website](https://www.kaggle.com/) popular with the data industry that hosts databases and runs data analytics competition. To access the [database]() for this model, you
will need to create a Kaggle account and follow the instructions to download your 'token' and 'key'. This
model will prompt you to have that information.
<br />[return to TOC](#table-of-contents-TOC)


## Business Case

<br />[return to TOC](#table-of-contents-TOC)

## Data Understanding

Greenhouse Gas Emissions from Commerical and Industrial Buildings have decreased by XX% since 2005, according to the [NYC Greenhouse Gas Inventory](https://climate.cityofnewyork.us/initiatives/nyc-greenhouse-gas-inventories/). But what's driving this reduction? This study reviews annual weather, transit volumes, and building's energy and fuel sources to determined key factors. 

### Data Sources
#### Emissions  
Emissions data was taken from the [NYC Greenhouse Gas Inventory](https://climate.cityofnewyork.us/initiatives/nyc-greenhouse-gas-inventories/) which can be found [here](https://data.cityofnewyork.us/Environment/NYC-Greenhouse-Gas-Emissions-Inventory/wq7q-htne/about_data) through the [Open NY](https://opendata.cityofnewyork.us/) website. The inventory uses entities reported fuel and electricity consumption and, based on an emissions factor, reports on a metric ton of CO2.

#### Weather - HDD & CDD
Weather - Annual heating degree days (HDD) and Cooling Degree Days (CDD) as listed on NYSERDA's website to determine how building systems would react. Data extracted from [NYSERDA](https://www.nyserda.ny.gov/About/Publications/Energy-Analysis-Reports-and-Studies/Weather-Data/Monthly-Cooling-and-Heating-Degree-Day-Data) website

#### Transit volumes
Transit volumes are used as a proxy for human activity and not transportation emissions sources. While this doesn't cover every location where people would enter the city to conduct C%I activity (NJTransit and Amtrak entry in Penn Station, for instance), it serves as a proxy for this activity.

MTA Bridge & Tunnels - Toll data was used to quantify volume taken from the [MTA hourly bridges and tunnels traffic rates](https://data.ny.gov/Transportation/MTA-Bridges-Tunnels-Hourly-Traffic-Rates-Beginning/qzve-kjga/about_data). This set can be found through [Data.NY.gov](https://data.ny.gov/). Data taken through API Token

Port Authority PATH Train - Total ridership data for NYC stations

MTA Ridership - 

#### Fuel Sources 
Fuel source data was also taken from the [NYC Greenhouse Gas Inventory](https://climate.cityofnewyork.us/initiatives/nyc-greenhouse-gas-inventories/). Data taken through API Token

### Annual Sums Limitations
The limits with annual data are the smaller quantity of total data points. Monthly, weekly, or daily numbers would provide additional granulate to strengthen trends, inferences, or other observations. The benefit of annual data is the elimination of seasonal variations. The long term trends become easier to spot.

<br />[return to TOC](#table-of-contents-TOC)

* [Kaggle]()
* [THis Repository]()

## Data Preparation

<br />[return to TOC](#table-of-contents-TOC)

## Modeling

<br />[return to TOC](#table-of-contents-TOC)

## Evaluation

<br />[return to TOC](#table-of-contents-TOC)

## Key Findings

<br />[return to TOC](#table-of-contents-TOC)

## Summary

### Next Steps:
#### Additional Data

#### Test UI Prompts

#### Try Calorie Counting

<br />[return to TOC](#table-of-contents-TOC)

## Github Repository

To execute this project, a github repository is utilized for public viewing and collaboration. The source file for the original data is not available.

You can see the following files stored in the github repository.


* *Images* - Folder containing the image files used in the Notebook, Presentation, and README file

* *PDFs* - Folder containing the pdf versions of the Slides, the Notebook, and Presentation
            
* [README](README.md) the currently file you're reading with descriptions about the coding file

* [.gitignore](.gitignore) - git ignore file 

* [notebook]() - Notebook with Python analysis

<br />[return to TOC](#table-of-contents-TOC)
