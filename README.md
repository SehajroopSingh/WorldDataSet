# WorldDataSet:     
## Data Set of Big world indicators for each country : A dataset to do analysis of world problems

# TABLE OF CONTENTS

#### 1) Files Summaries

#### 2) How Datasets were Curated

#### 3) Datasets Used to Compile our Datasets






## Different Files Summaries:

### Our Recent Dataset:
#### GDIM.csv

In our data preprocessing stage,the initial dataset did not include details on on Gender equality, government instability, IQ, income, and temperature. Since, this additional data information would help with our analysis, we added the additional information by merging EqualityData and Politicalstability dataset with our GDIM dataset grouping by and country and sub-region. The variables included in the final dataset are displayed in Table 1 while the first few rows of the final dataset are shown in Table 2.


Column Names:

Name | Variable description | Type | Units of measurement
---|---|---|---
country| Name of country| categorical|none
region_noHICgroup |Region (with high-income economies among the regions)|categorical|none
sub-region| | |none
incgroup4 |Income groups (4 categories) as of July 1, 2020|categorical|none
year |Survey year|categorical| none 
parent| Mothers/Fathers/Max/Average|categorical|none
child |Sons/Daughters/All|categorical|none
MEANp| Mean of parents' years of schooling||none
MEANc| Mean of children's years of schooling||none
SDp| Standard deviation of parents' years of education||none
SDc |Standard deviation of children’s years of education||none
CAT| is the share of respondents that have attained a higher educational category than their parents, conditional on the parents not having obtained tertiary education, such that all included individuals have a chance of surpassing their parents. For this measure, we categorize individuals and parents according to their highest educational attainment in the following categories (see Section 4 for more details): (i) less than primary, (ii) primary, (iii) lower-secondary, (iv) upper-secondary, or (v) tertiary. | numeric|range 0-1
CAT_ISCED0| Absolute mobility when parents have ISCED0 pr(c>p,p=ISCED0)| numeric|range 0-1
CAT_ISCED1| Absolute mobility when parents have ISCED0,pr(c>p, p=ISCED1)| numeric|range 0-1
CAT_ISCED2 |Absolute mobility when parents have ISCED0, pr(c>p, p=ISCED2)| numeric|range 0-1
CAT_ISCED34| Absolute mobility when parents have ISCED0, pr(c>p, p=ISCED3-4)| numeric|range 0-1
GEI % | | numeric | 
Gender Economic Participation and Opportunity Equality % |  |numeric| 
Gender Health and Survival Equality %| |numeric  |
Gender Education Attainment Equality %| |numeric | 
Gender Health and Survival Equality % | |numeric |
Gender Political Empowerment | |numeric |
Political Instability Estimate | | numeric|
IQ |  | numeric |
Average Income (USD) | | numeric| Dollar
Education expenditure\nper inhabitant (USD)	 |  | numeric| Dollar
Daily maximum\ntemperature Celsius|  | | Celcius - C



CSV screenshot:

<img width="811" alt="CleanShot 2022-12-14 at 17 40 54@2x" src="https://user-images.githubusercontent.com/116106229/207668114-ce40bfa7-ae9a-4495-9726-8eea26a2eb8d.png">



|    | country     | region     | incgroup4   | parent   | child    |   MEANp |   MEANc |     SDp |     SDc |      CAT |      DIF |   CAT_ISCED0 |   CAT_ISCED1 |   CAT_ISCED2 |   CAT_ISCED34 |   GEI % |   Gender Economic Participation and Opportunity Equality % |   Gender Education Attainment Equality % |   Gender Health and Survival Equality % |   Gender Political Empowerment | sub-region    |   Political  |   |  ) |   |    |
|    |             |            |             |          |          |         |         |         |         |          |          |              |              |              |               |         |                                                            |                                          |                                    Instability Estimate     |                        IQ         |          Average Income (USD)     |                 Education expenditure                  |      |  Daily maximum                       |    per inhabitant (USD) |   temperature Celsius |
|---:|:------------|:-----------|:------------|:---------|:---------|--------:|--------:|--------:|--------:|---------:|---------:|-------------:|-------------:|-------------:|--------------:|--------:|-----------------------------------------------------------:|-----------------------------------------:|----------------------------------------:|-------------------------------:|:--------------|---------------------------------:|-----:|-----------------------:|------------------------:|----------------------:|
|  0 | Afghanistan | South Asia | Low income  | avg      | all      | 2.48016 | 5.5824  | 3.80978 | 5.85776 | 0.414355 | 3.2033   |     0.329975 |     0.633108 |     0.584747 |      0.542553 |   0.444 |                                                       0.18 |                                    0.514 |                                   0.952 |                          0.132 | Southern Asia |                             -2.5 |   80 |                    340 |                      13 |                    24 |
|  1 | Afghanistan | South Asia | Low income  | avg      | daughter | 2.98999 | 4.33173 | 4.01038 | 5.90269 | 0.283075 | 1.43339  |     0.174239 |     0.509354 |     0.445407 |      0.47483  |   0.444 |                                                       0.18 |                                    0.514 |                                   0.952 |                          0.132 | Southern Asia |                             -2.5 |   80 |                    340 |                      13 |                    24 |
|  2 | Afghanistan | South Asia | Low income  | avg      | son      | 2.35398 | 5.89194 | 3.74849 | 5.80614 | 0.446874 | 3.64172  |     0.364921 |     0.664005 |     0.630444 |      0.563892 |   0.444 |                                                       0.18 |                                    0.514 |                                   0.952 |                          0.132 | Southern Asia |                             -2.5 |   80 |                    340 |                      13 |                    24 |
|  3 | Afghanistan | South Asia | Low income  | dad      | all      | 3.75605 | 5.53828 | 5.49376 | 5.84203 | 0.350244 | 2.11022  |     0.342107 |     0.731783 |     0.366321 |      0.260787 |   0.444 |                                                       0.18 |                                    0.514 |                                   0.952 |                          0.132 | Southern Asia |                             -2.5 |   80 |                    340 |                      13 |                    24 |
|  4 | Afghanistan | South Asia | Low income  | dad      | daughter | 4.52088 | 4.27777 | 5.80478 | 5.86974 | 0.230126 | 0.128818 |     0.189864 |     0.81914  |     0.233389 |      0.202416 |   0.444 |                                                       0.18 |                                    0.514 |                                   0.952 |                          0.132 | Southern Asia |                             -2.5 |   80 |                    340 |                      13 |   


Table: a parameter estimate table of the fitted linear regression model. the coefficient estimates and coefficient standard errors for the intercept and each variable are shown in the two columns, with rows indexed by parameter name. The estimate for the error variance parameter is in the last row.
![image](https://user-images.githubusercontent.com/116106229/207688153-6bf04080-0fa2-44f8-a84c-81dfea1bdbb3.png)
The regression shows that a 1 unit increase in parental education results in a 0.671677 increase in child education. The standard error is .03 which leads us to conclude that it is a decent estimate as zero is not within a SDE. The estimates for all variables except the expenditure variable are all not within SDE of zero thus viable estimates, suggesting that the expenditure variable may not be significant. The GEI estimate is 10.179138 but since each increase in GEI is .01 up to 1 max, it has less of an impact then an initial brief observation of the model suggests. IQ and political instability seem to also have big impacts with each unit increase. An R^2 value of 0.8264603491332505 suggests a high amount of variance in the education can be explained by these variables.

## 20 Years Data:

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










# Discussion:



### 20 Years Data:







### Recent Data:

We analyzed the correlation between education numbers and a few social, political, and economical factors. The analysis focused on different factors that influence average education of a countries residents. The analysis showed the main coorelations between education levels and daily maximum temperature of your country, average income and education exepnditure per inhabitant, and also Gender Equality. These seemed to be some of the major contributers to the success of a countries education levels. Further, linear regression model quantified the relationship between these variables and the education attainment.

![image](https://user-images.githubusercontent.com/116106229/207689143-6baf7b1f-79ce-435e-a4d3-57f6e8e85788.png)

There are a few surprising effects of specific factors that influence the overall education prospect of the people that are effected by them.

There seemed to be a unusual negative correlation between the mean years educated in a country and the average daily maximum temperature. Further research and data needs to be compiled in order to understand why this is the case. Mean temperature also seems to have a correlation with average income and political instability thus more reasearch would need to be done to understand this issue.

Another surprising find is that there seems to be an increase in likelihood of higher education for men when gender equality is higher (Figure 4). This is shown by an increase in the slope of the regression line when education is plotted against GEI % for all, males and females. Whilst a higher GEI % increases the overall effect of higher GEI % for men, it does the exact opposite for women. This is inline with current studies stating that as Gender equality index increases, the biological differences between men and women tend to manifest themselves more so, possibly resulting in different educational attainment goals for the different sexes.






# How Our Datasets was Curated:



## Past 20 year Dataset

WDID data set:

![__results___3_0](https://user-images.githubusercontent.com/116106229/207693620-5257f1da-3705-465a-972e-6170ce33cd05.png)
Visulaization reated to ascertain the emissions levels of each of the top 10 countries, in terms of GDP.


<img width="656" alt="CleanShot 2022-12-14 at 19 27 47@2x" src="https://user-images.githubusercontent.com/116106229/207695741-86a366b7-6db6-4403-bc06-771cd957ca71.png">
72.560976% of Countries have increased CO2 emissions (metric ton per capita) (1970-2016)	
58.536585% of Countries that have increased CO2 emissions (metric ton per capita) (2006-2016)




![__results___10_0](https://user-images.githubusercontent.com/116106229/207694518-f6f05a90-d7d2-4b1b-9244-c643b310f7cc.png)
Decreasing emmitions trends amongst some of the top poluting countries


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


### Regional Code Dataset:
The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
ttps://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv







