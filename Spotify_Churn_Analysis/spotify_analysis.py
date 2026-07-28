print("Spotify Churn Analysis") # prints the title of the analysis to the console.
# This script analyzes Spotify dataset to generate visualizations and insights.
# First, I will import the necessary libraries. Libraries are pre-written code that we can use to perform specific tasks.
import numpy as np 
# performs fast numerical calculations.
import pandas as pd 
# used to read, organize, clean and analyze data.
import matplotlib.pyplot as plt 
# used to create graphs and charts to visualize data.
import seaborn as sns
# used to create more advanced visualizations and heatmaps.
# I will use the functions from pandas library to read and filter the dataset. 
df = pd.read_csv('spotify_churn_dataset.csv') 
# this functions reads the dataset and stores it in a variable called df.
print(df.head())  # show the first 5 rows.
print(df.columns) # show the column names.
print(df.info())  # show information about the dataset.
print(df.isnull().sum())  # show the number of missing values in each column.
print(df['is_churned'].value_counts())  # show the count of each category in the 'is_churned' column.

churn_counts = df['is_churned'].value_counts()
# selects the is churned column from the dataset and counts the number of occurrences of each unique value (0 or 1) in that column.

# First, I will create a histogram to visualize the distribution of listening time among users.
plt.figure(figsize=(8,6))
plt.grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.3, zorder=0.5) # adds a grid to the graph for better readability.
plt.hist(df['listening_time'], bins=30, color='purple', edgecolor='black', alpha=0.9, zorder=2)
plt.yticks(range(0, 600, 50)) # sets the y-axis ticks to range from 0 to 600 with a step of 50.
plt.title("Distribution of Listening Time", fontsize=16, fontweight='bold', pad=20) # title of the graph.
plt.xlabel("Listening Time (minutes)", fontsize=10, fontweight='bold') # label for the x-axis of the graph.
plt.ylabel("Number of Users", fontsize=10, fontweight='bold') # label for the y-axis of the graph.
plt.savefig("listening time.png", dpi=300, bbox_inches="tight") #saves the chart as high resolution png images.
plt.show() # displays the graph on the screen.


# now, I will create a bar chart to visualize the churn rate by subscription type.
churn_rate = df.groupby('subscription_type')['is_churned'].mean() * 100
# groups the dataset by subscription type and calculates the mean of the 'is churned' column for each group, then multiplies by 100 to get the churn rate as a percentage.
plt.figure(figsize=(8,6))
churn_rate.plot(kind='bar', color=['cornflowerblue'], edgecolor='black', alpha=0.9, width=0.8, zorder=2)
for i, v in enumerate(churn_rate):
    plt.text(i, v + 1, f"{v:.2f}%", ha='center', fontsize=10, fontweight='bold') # adds the churn rate value on top of each bar in the bar chart.
plt.title("Churn Rate by Subscription Type", fontsize=16, fontweight='bold', pad=20) # title of the graph.
plt.xlabel("Subscription Type", fontsize=10, fontweight='bold') # label for the x-axis of the graph.
plt.ylabel("Churn Rate (%)", fontsize=10, fontweight='bold') # label for the y-axis of the graph.
plt.xticks(rotation=0) # rotates the x-axis labels to be horizontal.
plt.ylim(0, 35) # sets the y-axis limits from 0 to 35.
plt.grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.5, zorder=0.5) # adds a grid to the graph for better readability.
plt.tight_layout() # adjusts the layout of the graph to prevent labels and titles getting cut off.
plt.savefig("churn_by_subscription.png", dpi=300, bbox_inches="tight") #saves the chart as high resolution png images.
plt.show() # displays the graph on the screen.


# Now, I will create a heatmap to visualize the churn rate by subscription type and offline listening. 
# A heatmap is a graphical representation of data where individual values are represented as colors.
heatmap_data = df.pivot_table(index='subscription_type', columns='offline_listening', values='is_churned', aggfunc='mean') * 100
# creates a pivot table that shows the mean churn rate for each combination of subscription type and offline

plt.figure(figsize=(8,6))
sns.heatmap(heatmap_data, annot=True, annot_kws={"size": 10}, fmt=".2f", cmap="YlOrRd", linewidths=0.5, cbar_kws={'label': 'Churn Rate (%)'},zorder=2)
# annot stands for annotation i.e it displays the actual values in each cell, fmt specifies the format of the annotations, '.2F' Means two decimal places.
# cmap specifies the color map to use, YlOrRd stands for Yellow-Orange-ReD.
# linewidths specifies the width of the lines that will divide each cell in the heatmap.
# cbar_kws specifies the label for the color bar.
plt.grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.5, zorder=0.5)
plt.title("Churn Rate by Subscription Type and Offline Listening", fontsize=16, fontweight='bold', pad=20) # title of the graph.
plt.xlabel("Offline Listening", fontsize=10, fontweight='bold') # label for the x-axis of the graph.
plt.ylabel("Subscription Type", fontsize=10, fontweight='bold') # label for the y-axis of the graph.
plt.show() # displays the graph on the screen.
plt.savefig("churn rate by subscription type and offline listening.png", dpi=300, bbox_inches="tight") #saves the chart as high resolution png images.
plt.tight_layout() # adjusts the layout of the graph to prevent labels and titles getting cut off.