# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
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
df[df['year'] == "2014*"]

# %% [markdown]
# CLEANING:
# 
# %% [markdown]
# renaming the columns and picking the important:

# %%
df.columns = ['move', 'date', 'year', 'num', 'purpose', 'Q', 'status', 'id']


# %%
df = df[['move', 'year', 'num', 'purpose', 'Q', 'status']]

# %% [markdown]
# Finding and changing some values in the purpose column

# %%
df.loc[df['purpose'] == 'Visitors on Holiday', 'purpose'] = 'holiday'
df.loc[df['purpose'] == 'Visitors on Business', 'purpose'] = 'business'
df.loc[df['purpose'] == 'Visitors in Transit', 'purpose'] = 'transit'

# %% [markdown]
# Confirming the changes

# %%
df.head()


# %%
df.tail()


# %%
df[df['purpose'] == "business"]


# %%
df[df['purpose'] == "transit"]

# %% [markdown]
# Checking for duplicate entries

# %%
df.duplicated().sum()

# %% [markdown]
# There are none
# %% [markdown]
# ANALYSIS:
# %% [markdown]
# a) UNIVARIATE ANALYSIS:
# 
# Analysis of the num variable, which is the number of visitors:

# %%
descr = df['num'].describe()
descr


# %%
df['num'].var()


# %%
df['num'].std()


# %%
df['num'].skew()


# %%
df['num'].kurt()

# %% [markdown]
# b) BIVARIATE ANALYSIS:

# %%
yearly = df['num'].groupby(df['year']).sum()
yearly = yearly.sort_values(ascending = False)
yearly


# %%



# %%
quat = df['num'].groupby(df['Q']).sum().sort_values(ascending = False)
quat


# %%
pup = df['num'].groupby(df['purpose']).sum().sort_values(ascending = False)
pup

# %% [markdown]
# c) MULTIVARIATE ANALYSIS:

# %%
yr_pup = df['num'].groupby([df['year'], df['purpose']]).sum()
yr_pup


# %%
yr_quat = df['num'].groupby([df['year'], df['Q']]).sum()
yr_quat


# %%
q_pup = df['num'].groupby([df['Q'], df['purpose']]).sum()
q_pup.columns = ['Q', 'purpose', 'num']
q_pup

# %% [markdown]
# VISUALIZATION:
# 

# %%



