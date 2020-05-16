import pandas as pd 
ecom = pd.read_csv("Ecommerce Purchases")

# print(ecom)
# print(ecom.head())


# How many rows and columns are there?
# len(ecom.columns)
# len(ecom.index)

# What is the average purchase price?
# print(ecom["Purchase Price"].mean())

# What were the highest and lowest purchase Prices?
# Highest?
# print(ecom["Purchase Price"].max())
# Lowest?
# print(ecom["Purchase Price"].min())

# How many people have English 'en' as their language on their website
# print(ecom[ecom["Language"] == "en"].count())


# how many people have job title of lawyer
# print(ecom[ecom["Job"] == "Lawyer"].count()["Job"])

# How many people made the purchase during the AM and how many people made the purchase during PM? 
#PM
# print(ecom[ecom["AM or PM"] == "PM"].count()["AM or PM"])
#AM
# print(ecom[ecom["AM or PM"] == "AM"].count()["AM or PM"])

# 5 most common JOb Titles
# print(ecom["Job"].value_counts().head(5))

# Someone made a puchase from lot "90 WT", what was the purchase price
# print(ecom[ecom['Lot']=='90 WT']["Purchase Price"])

# How many people have a credit card that expires in 2025
# print(sum(ecom["CC Exp Date"].apply(lambda exp: exp[3:] == "25")))

# top 5 most popular email providers
# print(ecom["Email"].apply(lambda email: email.split("@")[1]).value_counts().head(5))