import seaborn as sns
import matplotlib.pyplot as plt  
import pandas as pd

# df = sns.load_dataset("tips")
# sns.histplot(df["total_bill"], bins=20, kde=True, color='green')
# plt.title("Histogram + KDE")
# plt.show()

# data = pd.DataFrame({
#     "category": ['A', 'B', 'C', 'D'],
#     "value": [4, 7, 2, 9]
# })

# sns.barplot(x="category", y="value", data=data)
# plt.title("Normal Bar Chart (Seaborn)")
# plt.show()

df=sns.load_dataset('tips')
sns.boxplot(x="day",y="total_bill",data=df,palette="pastel")
plt.title("box plot")
plt.show()
