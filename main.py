import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

#print(data["language_code"])

sns.scatterplot(x="ratings_count", y="average_rating", hue="average_rating", data=data)

plt.title("Average GoodReads Rating and Number of Ratings")

plt.savefig("avg_rtg_rtg_count.png")