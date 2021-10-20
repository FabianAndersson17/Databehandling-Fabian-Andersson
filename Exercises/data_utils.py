import seaborn as sns
import pandas as pd

def Plot_Missing_Data(dataFrame):
    sns.barplot(data=dataFrame, x=dataFrame.isnull(), y=dataFrame.isnull().nunique())