import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots(1, 2, )
def Plot_Missing_Data(dataFrame):
    sns.barplot(data=dataFrame, x=dataFrame.isnull(by="rows"), y=dataFrame.isnull().nunique())