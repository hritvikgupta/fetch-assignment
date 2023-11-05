import pandas as pd
brand = pd.read_csv("/Users/hritvikgupta/fetch-assignment/dataset/brand_category.csv")
categories = pd.read_csv("/Users/hritvikgupta/fetch-assignment/dataset/categories.csv")
offers = pd.read_csv("/Users/hritvikgupta/fetch-assignment/dataset/offer_retailer.csv")
brand['BRAND'] = brand['BRAND'].fillna("")
offers['OFFER'] = offers['OFFER'].fillna("")
offers['RETAILER'] = offers['RETAILER'].fillna("")

