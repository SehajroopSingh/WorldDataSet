# WorldDataSet:     
## Data Set of Big world indicators for each country : A dataset to do analysis of world problems

# TABLE OF CONTENTS

#### 1) Files Summaries

#### 2) How Datasets were Curated

#### 3) Datasets Used to Compile our Datasets






## Different Files Summaries:

### Our Recent Dataset:
####GDIM.csv
Column Names:
[('country', 'region', 'incgroup4', 'parent', 'child', 'MEANp', 'MEANc', 'SDp', 'SDc', 'CAT', 'DIF', 'CAT_ISCED0', 'CAT_ISCED1', 'CAT_ISCED2', 'CAT_ISCED34', 'GEI %', 'Gender Economic Participation and Opportunity Equality %', 'Gender Education Attainment Equality %', 'Gender Health and Survival Equality %', 'Gender Political Empowerment', 'sub-region', 'Political Instability Estimate', 'IQ', 'Average Income (USD)', 'Education expenditure\nper inhabitant (USD)', 'Daily maximum\ntemperature Celsius'])

CSV screenshot:

<img width="811" alt="CleanShot 2022-12-14 at 17 40 54@2x" src="https://user-images.githubusercontent.com/116106229/207668114-ce40bfa7-ae9a-4495-9726-8eea26a2eb8d.png">


#### DatedData.py

Includes all of the code used to create the main dataframe from the original datasets downloaded from the different sources.



#### WDIDCombinedgroupcountryandyear.csv 

This csv contains the datapoints grouped by country to make it easier to understand progress in all columns over the twenty year period that is represented by the main dataset.

CSV screenshot:

<img width="829" alt="CleanShot 2022-12-14 at 16 19 47@2x" src="https://user-images.githubusercontent.com/116106229/207650520-beaa2761-0f1f-4c76-b9ac-e2777c8e2423.png">





#### WDIDCombinedFinalStats.csv

This csv contains the summary statistics for each column in the main dataset

CSV screenshot:

<img width="842" alt="CleanShot 2022-12-14 at 16 19 07@2x" src="https://user-images.githubusercontent.com/116106229/207650305-36deddb4-5a74-4548-be75-eb34d19c339f.png">






# How Our Datasets was Curated:




## Past 20 year Dataset



### GDIM DataSet:
The infomation in the GDIM comes from a variety of surveys offered within each country between 2008 and 2016. This database includes educational mobility estimates from 153 economies and accounts for 97 percent of the world’s population. Except for the Middle East and North Africa, the population coverage in all regions exceeds 90 percent, whilst in the middle east and North africa 83 percent of the population is covered.
https://datacatalog.worldbank.org/search/dataset/0050771/global-database-on-intergenerational-mobility


### Gender Equality Dataset:
The Gender Equality data set provides a few key variables, namely the Gender equality Index GEI, which is an aggregate of a few of the subsets of its variables. The World Economic Forum compiles and releases the Global Gender Gap Index every year. This report measures the extent of gender-based gaps among four key dimensions: Economic Participation and Opportunity, Educational Attainment, Health and Survival, and Political Empowerment, then gives each country a ranking between 0.000 (or 0%, the lowest possible gender equality) and 1.000 (100%, the highest possible gender equality). The analyses of each country are intended to serve as a basis for designing effective measures for reducing gender gaps. The 2021 edition of the Global Gender Gap Index studied and ranked 156 countries and territories around the world.
https://worldpopulationreview.com/country-rankings/gender-equality-by-country


### IQ dataset
The IQ by country dataset contains information about the average IQ of a country along with average income in US dollars and education expenditure per individual. The displayed IQ was averaged out of the results of 9 international studies and compared to the average income and government expenditures on education for the years 1990 to 2010.
https://www.worlddata.info/iq-by-country.php


### Worldwide Governance Indicators (WGI) Dataset:
The Worldwide Governance Indicators (WGI) are a research dataset summarizing the views on the quality of governance provided by a large number of enterprise, citizen and expert survey respondents in industrial and developing countries. These data are gathered from a number of survey institutes, think tanks, non-governmental organizations, international organizations, and private sector firms. The WGI does not reflect the official views of the World Bank, its Executive Directors, or the countries they represent. The WGI is not used by the World Bank Group to allocate resources.” The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
http://info.worldbank.org/governance/wgi/


### Refugees
Refugees are people who are recognized as refugees under the 1951 Convention Relating to the Status of Refugees or its 1967 Protocol, the 1969 Organization of African Unity Convention Governing the Specific Aspects of Refugee Problems in Africa, and people recognized as refugees in accordance with the UNHCR statute, people granted refugee-like humanitarian status, and people provided temporary protection. Asylum seekers--people who have applied for asylum or refugee status and who have not yet received a decision or who are registered as asylum seekers--are excluded. Palestinian refugees are people (and their descendants) whose residence was Palestine between June 1946 and May 1948 and who lost their homes and means of livelihood as a result of the 1948 Arab-Israeli conflict. Country of asylum is the country where an asylum claim was filed and granted. The aggregates refer to World Bank classifications of economies and therefore may differ from those reported by the OECD.
The Dataset was downloaded from World Bank website. It consists two Excel files, one for refugees of origin, and the other for refugees of asylum.

### Regional Code dataset:
The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv

### Cause of Deaths around the World (Historical Data):
This Dataset is created from Our World in Data. This Dataset falls under open access under the Creative Commons BY license. You can check the FAQ for more information about it. Special thanks to Max Roser, Hannah Ritchie, and Fiona Spooner (2021) - "Burden of disease". Published online at OurWorldInData.org. Retrieved from: https://ourworldindata.org/burden-of-disease [Online Resource].

https://www.migrationdataportal.org/themes/environmental_migration_and_statistics#data-strengths-amp-limitations


### Global Health Data 
https://ourworldindata.org/explorers/global-health?facet=none&country=OWID_WRL~CHN~ZAF~BRA~USA~GBR~IND~RWA&Health+Area=Child+health&Indicator=Child+mortality&Metric=Rate&Source=WHO+%28GHO%29
Our World
in Data


### IOM’s Displacement Tracking Matrix 
(DTM) is a system used to track and monitor disaster displacement and population mobility. Data, which can be disaggregated by gender and sex, are regularly captured, processed and disseminated to provide a better understanding of the movements and evolving needs of displaced populations and migrants, whether in situ or en route, before, during and in the aftermath of disasters. The data are presented in the DTM Data Portal. A study on how current DTM practices collect data on human mobility in the context of environmental degradation, climate change and disasters and draws also provides recommendations on how to improve current tools and practices. Recommendations include improving the focus of some DTM questions and increasing the amount of options available for respondents to provide more granular data on the migration, environment and climate nexus (IOM, 2020). 
https://displacement.iom.int



### 
The CLIMIG database of studies on environmental migration, both of qualitative and quantitative nature, was developed by the University of Neuchatel (Switzerland).
https://www.unine.ch/geographie/home/recherche/migration_climate_change_1/bibliographic-database.html


### IDMC_GIDD_disasters_internal_displacement_data_2021-1670350238241:
Internal Displacements from 2008 to 2021
https://www.internal-displacement.org/database/displacement-data

### IDMC_GIDD_conflict_internal_displacement_data_2021-1670350321633:
Internal displacements and total number of IDPs from 2008 to 2021
https://www.internal-displacement.org/database/displacement-data

### Climate change Data
Data from World Development Indicators and Climate Change Knowledge Portal on climate systems, exposure to climate impacts, resilience, greenhouse gas emissions, and energy use.


### Natural Disaster DataSet:
https://ourworldindata.org/natural-disasters









#  Recent Dataset

The data for sourced from The Global Database on Intergenerational Mobility (GDIM), EqualityData, and Politicalstability datasets.

The infomation in the GDIM comes from a variety of surveys offered within each country between 2008 and 2016. This database includes educational mobility estimates from 153 economies and accounts for 97 percent of the world’s population. Except for the Middle East and North Africa, the population coverage in all regions exceeds 90 percent, whilst in the middle east and North africa 83 percent of the population is covered.
https://datacatalog.worldbank.org/search/dataset/0050771/global-database-on-intergenerational-mobility

The Gender Equality data set provides a few key variables, namely the Gender equality Index GEI, which is an aggregate of a few of the subsets of its variables. The World Economic Forum compiles and releases the Global Gender Gap Index every year. This report measures the extent of gender-based gaps among four key dimensions: Economic Participation and Opportunity, Educational Attainment, Health and Survival, and Political Empowerment, then gives each country a ranking between 0.000 (or 0%, the lowest possible gender equality) and 1.000 (100%, the highest possible gender equality). The analyses of each country are intended to serve as a basis for designing effective measures for reducing gender gaps. The 2021 edition of the Global Gender Gap Index studied and ranked 156 countries and territories around the world.
https://worldpopulationreview.com/country-rankings/gender-equality-by-country

The IQ by country dataset contains information about the average IQ of a country along with average income in US dollars and education expenditure per individual. The displayed IQ was averaged out of the results of 9 international studies and compared to the average income and government expenditures on education for the years 1990 to 2010.
https://www.worlddata.info/iq-by-country.php

The Worldwide Governance Indicators (WGI) are a research dataset summarizing the views on the quality of governance provided by a large number of enterprise, citizen and expert survey respondents in industrial and developing countries. These data are gathered from a number of survey institutes, think tanks, non-governmental organizations, international organizations, and private sector firms. The WGI does not reflect the official views of the World Bank, its Executive Directors, or the countries they represent. The WGI is not used by the World Bank Group to allocate resources.” The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
http://info.worldbank.org/governance/wgi/

The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
ttps://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv













