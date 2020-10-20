# %% [markdown]
# Libraries:

# %%
import pandas as pd 
import matplotlib as plt
import numpy as numpy
import seaborn as sns

# %% [markdown]
# Loading the dataset and viewing a few columns:

# %%
df = pd.read_csv("visitors_to_kenya.csv")
df.head()


# %%
df.info()

# %% [markdown]
# Viewing what entries there are for each dpecific year

# %%
df[df['Year_Text'] == "2014*"]

# %% [markdown]
# # CLEANING:
# 
# %% [markdown]
#  Removing string characters from the Year_Text column so as to be able to change its data type to integer

# %%
years = df['Year_Text'].apply(lambda x:pd.Series([i for i in (x.lower().split("*"))]))
years.columns = ['yr', 'x']


# %%
years = years['yr'].apply(lambda x:pd.Series([i for i in (x.lower().split("'"))]))
years[:5]


# %%
conc = pd.concat([df, years], axis =1, ignore_index = 'False')
conc[:3]

# %% [markdown]
# renaming the columns and picking the important:

# %%
conc.columns = ['move', 'date', 'Year_Text', 'num', 'purpose', 'Q', 'status', 'id', 'year', 'x']


# %%
conc = conc[['move', 'year', 'num', 'purpose', 'Q', 'status']]

# %% [markdown]
# Converting the year column to numeric and confirming the convertion:

# %%
conc['year'] = pd.to_numeric(conc['year'])


# %%
conc.info()

# %% [markdown]
# The year column was succesfully converted to integer.
# 
# %% [markdown]
# Finding and changing some values in the purpose column

# %%
conc.loc[conc['purpose'] == 'Visitors on Holiday', 'purpose'] = 'holiday'
conc.loc[conc['purpose'] == 'Visitors on Business', 'purpose'] = 'business'
conc.loc[conc['purpose'] == 'Visitors in Transit', 'purpose'] = 'transit'

# %% [markdown]
# Confirming the changes

# %%
conc.head()


# %%
conc.tail()


# %%
conc[conc['purpose'] == "business"]


# %%
conc[conc['purpose'] == "transit"]

# %% [markdown]
#  Picking entries with actual values and not preliminaries:
# 

# %%
actl = conc[conc['status'].map(lambda status: 'Actual' in status)]
actl

# %% [markdown]
# The remaining entries are 672, meaning 160 were preliminary
# %% [markdown]
# From the conc data frame we can directly select the rows whose status is 'Actual' and year above 2001.
# This is the data set to be used for analysis:

# %%
fin = conc[(conc['year']>2001) & (conc['status'] == 'Actual')]
fin

# %% [markdown]
# The data set has reduced from 832 entries to 336 entries
# %% [markdown]
# Checking for duplicate entries

# %%
fin.duplicated().sum()

# %% [markdown]
# There are none
# %% [markdown]
# Checking for outliers:
# %% [markdown]
# a) In relation to quarters

# %%
q_bplot = sns.stripplot(x='year', y='num', hue='Q', data=fin, jitter= True)
q_bplot


# %%
qup_bplot = sns.stripplot(x='Q', y='num', data=actl)
qup_bplot

# %% [markdown]
# b) In relation to purposes

# %%
purpose_bplot = sns.stripplot(x='year', y='num', hue='purpose', data=fin)
purpose_bplot


# %%
pup_bplot = sns.stripplot(x='purpose', y='num', data=fin)
pup_bplot

# %% [markdown]
# # ANALYSIS:
# %% [markdown]
# # a) Univariate analysis:
# 
# Analysis of the num variable, which is the number of visitors:

# %%
descr = fin['num'].describe()
descr


# %%
fin['num'].var()


# %%
fin['num'].std()


# %%
fin['num'].skew()


# %%
fin['num'].kurt()
# %% [markdown]
# # b) Bivariate analysis:

# %%
sns.lineplot(x='year', y='num', data=fin)


# %%
yearly = fin['num'].groupby(fin['year']).sum().sort_values(ascending = False)
yearly


# %%
sns.lineplot(x='Q', y='num', data=fin)


# %%
quat = fin['num'].groupby(fin['Q']).sum().sort_values(ascending = False)
quat


# %%
sns.lineplot(x='purpose', y='num', data=fin)


# %%
pup = fin['num'].groupby(fin['purpose']).sum().sort_values(ascending = False)
pup
# %% [markdown]
# # c) Multivariate analysis:

# %%
sns.barplot(x='year', y='num',hue='purpose', data=fin)


# %%
yr_pup = fin['num'].groupby([fin['year'], fin['purpose']]).sum()
yr_pup


# %%
sns.barplot(x='year', y='num', hue='Q', data=fin)


# %%
yr_quat = fin['num'].groupby([fin['year'], fin['Q']]).sum()
yr_quat


# %%
sns.barplot(x='Q', y='num', hue='purpose', data=fin)


# %%
q_pup = fin['num'].groupby([fin['Q'], fin['purpose']]).sum()
q_pup


