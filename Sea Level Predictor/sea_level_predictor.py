import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file.
    df = pd.read_csv('Sea Level Predictor\epa-sea-level.csv')

    # Create scatter plot.
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
   
    # Create first line of best fit.
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series(range(df["Year"].min(), 2051))
    plt.plot(x_pred, res.intercept + res.slope * x_pred, 'r', label='fitted line')

    # Create second line of best fit.
    df2 = df[(df["Year"] >= 2000)]
    res2 = linregress(df2['Year'], y=df2["CSIRO Adjusted Sea Level"])
    x_2000 = pd.Series(range(2000, 2051))
    plt.plot(x_2000, res2.intercept + res2.slope * x_2000, 'b', label='fitted line')
    
    # Add labels and title.
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data.
    plt.savefig('Sea Level Predictor\sea_level_plot.png')
    return plt.gca()