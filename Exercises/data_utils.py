import seaborn as sns

def plot_missing_data(dataFrame):
    dataFrame_nullSeris = dataFrame.isnull().sum()
    dataFrame_Clean_Series=dataFrame_nullSeris[dataFrame_nullSeris>0]
    sns.barplot(x=dataFrame_Clean_Series.index, y=dataFrame_Clean_Series.values)