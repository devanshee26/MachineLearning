# -*- coding: utf-8 -*-
"""NatLanPro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b0kBsp9RkUk_uNWvD5WrUvAjNAI26CDj
"""

from textblob import TextBlob

sent1 ="I m Myself"

result =TextBlob(sent1).sentiment.polarity

print(result)

from google.colab import files

files.upload()

import pandas as pd

df=pd.read_excel('ClothingReviews.xlsx')

df.shape

df.columns.to_list()

x=df['Review Text']

type(x)

result =TextBlob(str(x)).sentiment.polarity

print(result)

