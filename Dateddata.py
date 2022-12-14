
# %%
import numpy as np
import pandas as pd

# %%
import altair as alt
# from sklearn.decomposition import PCA

# %%
from pathlib import Path
import os


# %%
CausesofDeath=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/cause_of_deaths.csv')
CausesofDeath
# %%
RefugeePop=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/RefugeePop.csv')
RefugeePop
# %%
# %%
Healthexpense=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/global-health-expendature.csv')
Healthexpense
# %%
Healthchild=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/global-health.csv')
Healthchild
# %%
Conflict_Internal_Displacement=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/conflict_internal_displacement_data_2021.csv')
Conflict_Internal_Displacement
# %%
Disaster_Internal_Displacement=pd.read_csv('//Users/sehaj/Documents/GitHub/DS-project/Dated Data/disasters_internal_displacement_data_2021.csv')
Disaster_Internal_Displacement
# %%
Healthcombined=Healthchild.merge(Healthexpense, on=['Year', 'Code', 'Country'], how='outer')
Healthcombined
# %%
HealthcombinedwRefugee=Healthcombined.merge(RefugeePop, on=['Year', 'Code', 'Country'], how='outer')
HealthcombinedwRefugee
# %%
HealthcombinedwRefugeeCofD=HealthcombinedwRefugee.merge(CausesofDeath, on=['Year', 'Code', 'Country'], how='outer')
HealthcombinedwRefugeeCofD
# %%
NaturalDisasters=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/natural-disasters.csv')
NaturalDisasters
# %%
my_list = list(NaturalDisasters)
my_list
# %%
y=NaturalDisasters.isnull().sum()/len(NaturalDisasters)
y
# %%
NaturalDisasters=NaturalDisasters[['Total economic damages from disasters as a share of GDP','Death rates from disasters','Injury rates from disasters' , 'Number of people affected by disasters per 100,000',
 'Country',
 'Year']]
# %%
HealthcombinedwRefugeeCofDandDisasters=HealthcombinedwRefugeeCofD.merge(NaturalDisasters, on=['Year', 'Country'], how='outer')
HealthcombinedwRefugeeCofDandDisasters
# %%
HealthcombinedwRefugeeCofDandDisasters.to_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/Combineddf.csv', index=False)
# %%
HealthcombinedwRefugeeCofDandDisasters['Indicator Code'].nunique()
# %%
HealthcombinedwRefugeeCofDandDisasters['Indicator Name'].nunique()
# %%
HealthcombinedwRefugeeCofDandDisasters=HealthcombinedwRefugeeCofDandDisasters.drop(columns=['Indicator Name', 'Indicator Code'])
# %%
HealthcombinedwRefugeeCofDandDisasters.to_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/Combineddf.csv', index=False)
# %%
values = [1954, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967,
       1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978,
       1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,954, 1955,
       1956, 1949, 1950, 1951, 1952, 1953, 1945, 1946, 1947, 1948, 1934,
       1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1932,
       1933, 2021, 1905, 1920, 1930, 1931, 1910, 1927, 1919, 1902, 1926,
       1929, 1904, 1909, 1911, 1922, 1923, 1906, 1928, 1903, 1908, 1912,
       1915, 1900, 1907, 1913, 1917, 1918, 1924, 1925, 1914, 1916, 1901,
       1921]
HealthcombinedwRefugeeCofDandDisasters = HealthcombinedwRefugeeCofDandDisasters[HealthcombinedwRefugeeCofDandDisasters.Year.isin(values) == False]
# %%
HealthcombinedwRefugeeCofDandDisasters
# %%
HealthcombinedwRefugeeCofDandDisasters.to_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/Combineddf.csv', index=False)

# %%

# %%
# sns.heatmap(HealthcombinedwRefugeeCofDandDisasters)
# %%
WDID=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/WDIData_T.csv')
WDID
# %%
WDID = WDID[WDID.Year.isin(values) == False]
WDID
# %%
WDID=WDID.pivot (index = ['Year'] , columns = ['Country Code','Indicator Name'], values = ['Value'])
WDID
# %%
WDID=WDID.stack(level=['Country Code'])
WDID
# %%
WDIDreset=WDID.reset_index()
# %%
WDIDreset
# %%

# %%
# %%
y=WDIDreset.isnull().sum()/len(WDIDreset)
y
missing_features =y[y > 0.20].index
WDIDdropped=WDIDreset.drop(missing_features, axis=1)
# %%
WDIDdropped.head()

# %%
WDIDlevels=WDIDdropped
WDIDlevels.columns=WDIDlevels.columns.droplevel(0)
WDIDlevels
# %%
WDIDlevels.columns.values[0] = "Year"
WDIDlevels.columns.values[1] = "Code"

WDIDlevels
# %%
WDIDlevels.to_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/WDIDreset.csv', index=False)
# %%
WDIDlevelreset=pd.read_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/WDIDreset.csv')
# %%
WDIDlevelreset

# %%
HealthcombinedwRefugeeCofDandDisasters

# %%
WDIDCombined=HealthcombinedwRefugeeCofDandDisasters.merge(WDIDlevelreset, on=['Year', 'Code'], how='outer')
WDIDCombined
# %%
WDIDCombined.to_csv('/Users/sehaj/Documents/GitHub/DS-project/Dated Data/WDIDCombined.csv', index=False)
# %%
y=WDIDCombined.isnull().sum()/len(WDIDreset)
y
# %%
