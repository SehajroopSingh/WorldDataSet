# WorldDataSet:     
## Data Set of Big world indicators for each country : A dataset to do analysis of world problems

## Two Curated Datasets: 100 + hours of curation

### Recent Data = RecentData.csv

### 20 Year Data = WDIDCombinedfinal.csv




# TABLE OF CONTENTS

#### 1) Files Summaries

#### 2) How Datasets were Curated

#### 3) Datasets Used to Compile our Datasets






## Different Files Summaries:

### Our Recent Dataset:

#### RecentData.csv

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

## 20 Years Data:

#### WDIDCombinedFinal.csv

Curated dataset of various attributed measured over a 20 year period in order to draw conclusions from the coorelations and causations of different varaibles with each other.


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










# Discussions:

These datasets are curated for use in analysis and possibly machine learning prediction algorithms. Please feel free to use the datasets. 


### 20 Years Data:




### Recent Data:






Table: a parameter estimate table of the fitted linear regression model. the coefficient estimates and coefficient standard errors for the intercept and each variable are shown in the two columns, with rows indexed by parameter name. The estimate for the error variance parameter is in the last row.
![image](https://user-images.githubusercontent.com/116106229/207688153-6bf04080-0fa2-44f8-a84c-81dfea1bdbb3.png)
The regression shows that a 1 unit increase in parental education results in a 0.671677 increase in child education. The standard error is .03 which leads us to conclude that it is a decent estimate as zero is not within a SDE. The estimates for all variables except the expenditure variable are all not within SDE of zero thus viable estimates, suggesting that the expenditure variable may not be significant. The GEI estimate is 10.179138 but since each increase in GEI is .01 up to 1 max, it has less of an impact then an initial brief observation of the model suggests. IQ and political instability seem to also have big impacts with each unit increase. An R^2 value of 0.8264603491332505 suggests a high amount of variance in the education can be explained by these variables.

We analyzed the correlation between education numbers and a few social, political, and economical factors. The analysis focused on different factors that influence average education of a countries residents. The analysis showed the main coorelations between education levels and daily maximum temperature of your country, average income and education exepnditure per inhabitant, and also Gender Equality. These seemed to be some of the major contributers to the success of a countries education levels. Further, linear regression model quantified the relationship between these variables and the education attainment.

![image](https://user-images.githubusercontent.com/116106229/207689143-6baf7b1f-79ce-435e-a4d3-57f6e8e85788.png)

There are a few surprising effects of specific factors that influence the overall education prospect of the people that are effected by them.

There seemed to be a unusual negative correlation between the mean years educated in a country and the average daily maximum temperature. Further research and data needs to be compiled in order to understand why this is the case. Mean temperature also seems to have a correlation with average income and political instability thus more reasearch would need to be done to understand this issue.

Another surprising find is that there seems to be an increase in likelihood of higher education for men when gender equality is higher (Figure 4). This is shown by an increase in the slope of the regression line when education is plotted against GEI % for all, males and females. Whilst a higher GEI % increases the overall effect of higher GEI % for men, it does the exact opposite for women. This is inline with current studies stating that as Gender equality index increases, the biological differences between men and women tend to manifest themselves more so, possibly resulting in different educational attainment goals for the different sexes.






# How Our Datasets was Curated:



## Curated Past 20 year Dataset

#### WDID data set:

The primary World Bank collection of development indicators, compiled from officially-recognized international sources. It presents the most current and accurate global development data available, and includes national, regional and global estimates.This is a dataset that has originated from the World Bank. The organisation has an open data platform found here and they update their information according the amount of data that is brought in. 
https://datacatalog.worldbank.org/dataset/world-development-indicators


![__results___3_0](https://user-images.githubusercontent.com/116106229/207693620-5257f1da-3705-465a-972e-6170ce33cd05.png)
Visulaization reated to ascertain the emissions levels of each of the top 10 countries, in terms of GDP.


<img width="656" alt="CleanShot 2022-12-14 at 19 27 47@2x" src="https://user-images.githubusercontent.com/116106229/207695741-86a366b7-6db6-4403-bc06-771cd957ca71.png">
72.560976% of Countries have increased CO2 emissions (metric ton per capita) (1970-2016)	
58.536585% of Countries that have increased CO2 emissions (metric ton per capita) (2006-2016)


<img width="506" alt="CleanShot 2022-12-14 at 19 30 05@2x" src="https://user-images.githubusercontent.com/116106229/207696613-ce505282-3e7b-4d7f-92d3-76823845ef7c.png">

Decreasing emmitions trends amongst some of the top poluting countries which is great news. Lets slowly get everyone onboard!


#### Refugees
Refugees are people who are recognized as refugees under the 1951 Convention Relating to the Status of Refugees or its 1967 Protocol, the 1969 Organization of African Unity Convention Governing the Specific Aspects of Refugee Problems in Africa, and people recognized as refugees in accordance with the UNHCR statute, people granted refugee-like humanitarian status, and people provided temporary protection. Asylum seekers--people who have applied for asylum or refugee status and who have not yet received a decision or who are registered as asylum seekers--are excluded. Palestinian refugees are people (and their descendants) whose residence was Palestine between June 1946 and May 1948 and who lost their homes and means of livelihood as a result of the 1948 Arab-Israeli conflict. Country of asylum is the country where an asylum claim was filed and granted. The aggregates refer to World Bank classifications of economies and therefore may differ from those reported by the OECD.
The Dataset was downloaded from World Bank website. It consists two Excel files, one for refugees of origin, and the other for refugees of asylum.

Dataset Structure:
<img width="823" alt="CleanShot 2022-12-14 at 19 37 52@2x" src="https://user-images.githubusercontent.com/116106229/207698002-bcb09dd5-ed99-468f-a469-86ba4c21e0e7.png">


#### Regional Code dataset:
The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv

#### Cause of Deaths around the World (Historical Data):
This Dataset is created from Our World in Data. This Dataset falls under open access under the Creative Commons BY license.  https://ourworldindata.org/burden-of-disease [Online Resource].

Columns:
01. Country/Territory - Name of the Country/Territory
02. Code - Country/Territory Code
03. Year - Year of the Incident
04. Meningitis - No. of People died from Meningitis
05. Alzheimer's Disease and Other Dementias - No. of People died from Alzheimer's Disease and Other Dementias
06. Parkinson's Disease - No. of People died from Parkinson's Disease
07. Nutritional Deficiencies - No. of People died from Nutritional Deficiencies
08. Malaria - No. of People died from Malaria
09. Drowning - No. of People died from Drowning
10. Interpersonal Violence - No. of People died from Interpersonal Violence
11. Maternal Disorders - No. of People died from Maternal Disorders
12. Drug Use Disorders - No. of People died from Drug Use Disorders
13. Tuberculosis - No. of People died from Tuberculosis
14. Cardiovascular Diseases - No. of People died from Cardiovascular Diseases
15. Lower Respiratory Infections - No. of People died from Lower Respiratory Infections
16. Neonatal Disorders - No. of People died from Neonatal Disorders
17. Alcohol Use Disorders - No. of People died from Alcohol Use Disorders
18. Self-harm - No. of People died from Self-harm
19. Exposure to Forces of Nature - No. of People died from Exposure to Forces of Nature
20. Diarrheal Diseases - No. of People died from Diarrheal Diseases
21. Environmental Heat and Cold Exposure - No. of People died from Environmental Heat and Cold Exposure
22. Neoplasms - No. of People died from Neoplasms
23. Conflict and Terrorism - No. of People died from Conflict and Terrorism
24. Diabetes Mellitus - No. of People died from Diabetes Mellitus
25. Chronic Kidney Disease - No. of People died from Chronic Kidney Disease
26. Poisonings - No. of People died from Poisoning
27. Protein-Energy Malnutrition - No. of People died from Protein-Energy Malnutrition
28. Chronic Respiratory Diseases - No. of People died from Chronic Respiratory Diseases
29. Cirrhosis and Other Chronic Liver Diseases - No. of People died from Cirrhosis and Other Chronic Liver Diseases
30. Digestive Diseases - No. of People died from Digestive Diseases
31. Fire, Heat, and Hot Substances - No. of People died from Fire or Heat or any Hot Substances
32. Acute Hepatitis - No. of People died from Acute Hepatitis


Dataset structure
<img width="1015" alt="CleanShot 2022-12-14 at 19 36 18@2x" src="https://user-images.githubusercontent.com/116106229/207697722-25f633e3-a02c-4e9b-9d55-2290ba3bba70.png">





https://www.migrationdataportal.org/themes/environmental_migration_and_statistics#data-strengths-amp-limitations


#### Global Health Data 
The Global Health Estimates are primarily calculated using cause-of-death statistics that are reported to the WHO by individual countries. WE used their what we believe is an important indicator of health within the country. Child mortality under the age of 5.
https://ourworldindata.org/explorers/global-health?facet=none&country=OWID_WRL~CHN~ZAF~BRA~USA~GBR~IND~RWA&Health+Area=Child+health&Indicator=Child+mortality&Metric=Rate&Source=WHO+%28GHO%29

Dataset Structure:
<img width="781" alt="CleanShot 2022-12-14 at 19 46 14@2x" src="https://user-images.githubusercontent.com/116106229/207699489-ee79cf3f-a340-4ffc-b900-585b2a9ccdf3.png">


#### IOM’s Displacement Tracking Matrix 
(DTM) is a system used to track and monitor disaster displacement and population mobility. Data, which can be disaggregated by gender and sex, are regularly captured, processed and disseminated to provide a better understanding of the movements and evolving needs of displaced populations and migrants, whether in situ or en route, before, during and in the aftermath of disasters. The data are presented in the DTM Data Portal. A study on how current DTM practices collect data on human mobility in the context of environmental degradation, climate change and disasters and draws also provides recommendations on how to improve current tools and practices. Recommendations include improving the focus of some DTM questions and increasing the amount of options available for respondents to provide more granular data on the migration, environment and climate nexus (IOM, 2020). 
https://displacement.iom.int

##### IDMC_GIDD_conflict_internal_displacement_data_2021-1670350321633:
Internal displacements and total number of IDPs from 2008 to 2021
https://www.internal-displacement.org/database/displacement-data

Conflict Internal Displacement Structure:
<img width="629" alt="CleanShot 2022-12-14 at 19 54 08@2x" src="https://user-images.githubusercontent.com/116106229/207700853-f7c5fa45-2a73-402b-a215-ab3e9a420330.png">



##### IDMC_GIDD_disasters_internal_displacement_data_2021-1670350238241:
Internal Displacements from 2008 to 2021
https://www.internal-displacement.org/database/displacement-data

Disaster Internal Displacement Dataset Structure:
<img width="780" alt="CleanShot 2022-12-14 at 19 53 37@2x" src="https://user-images.githubusercontent.com/116106229/207700764-99c9abb9-8b8c-42ce-aabb-e64c791854e2.png">

#### Natural Disaster DataSet:
https://ourworldindata.org/natural-disasters





##  Curated Recent Dataset

The data for sourced from The Global Database on Intergenerational Mobility (GDIM), EqualityData, and Politicalstability datasets.

#### GDIM DataSet:
The infomation in the GDIM comes from a variety of surveys offered within each country between 2008 and 2016. This database includes educational mobility estimates from 153 economies and accounts for 97 percent of the world’s population. Except for the Middle East and North Africa, the population coverage in all regions exceeds 90 percent, whilst in the middle east and North africa 83 percent of the population is covered.
https://datacatalog.worldbank.org/search/dataset/0050771/global-database-on-intergenerational-mobility


#### Gender Equality Dataset:
The Gender Equality data set provides a few key variables, namely the Gender equality Index GEI, which is an aggregate of a few of the subsets of its variables. The World Economic Forum compiles and releases the Global Gender Gap Index every year. This report measures the extent of gender-based gaps among four key dimensions: Economic Participation and Opportunity, Educational Attainment, Health and Survival, and Political Empowerment, then gives each country a ranking between 0.000 (or 0%, the lowest possible gender equality) and 1.000 (100%, the highest possible gender equality). The analyses of each country are intended to serve as a basis for designing effective measures for reducing gender gaps. The 2021 edition of the Global Gender Gap Index studied and ranked 156 countries and territories around the world.
https://worldpopulationreview.com/country-rankings/gender-equality-by-country


#### IQ dataset
The IQ by country dataset contains information about the average IQ of a country along with average income in US dollars and education expenditure per individual. The displayed IQ was averaged out of the results of 9 international studies and compared to the average income and government expenditures on education for the years 1990 to 2010.
https://www.worlddata.info/iq-by-country.php


#### Worldwide Governance Indicators (WGI) Dataset:
The Worldwide Governance Indicators (WGI) are a research dataset summarizing the views on the quality of governance provided by a large number of enterprise, citizen and expert survey respondents in industrial and developing countries. These data are gathered from a number of survey institutes, think tanks, non-governmental organizations, international organizations, and private sector firms. The WGI does not reflect the official views of the World Bank, its Executive Directors, or the countries they represent. The WGI is not used by the World Bank Group to allocate resources.” The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
http://info.worldbank.org/governance/wgi/


#### Regional Code Dataset:
The regional code dataset was used to provide a variable with more specific sub-region locations for each country in order to better facilitate our understanding of how different parts of the world are affected by the other variables.
https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv







