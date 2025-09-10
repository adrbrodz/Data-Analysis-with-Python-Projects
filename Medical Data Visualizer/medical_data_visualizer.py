import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('Medical Data Visualizer\medical_examination.csv')

# Add an overweight column to the data.
df['overweight'] = (df['weight']/((df['height']/100)**2)>25).astype(int)

# Normalize data.
df['gluc'] = (df['gluc'] !=1).astype(int)
df['cholesterol'] = (df['cholesterol'] !=1).astype(int)

# Draw the Categorical Plot.
def draw_cat_plot():
    # Create a DataFrame for the cat plot.
    df_cat = pd.melt(
        df, id_vars=["cardio"], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
        )
    
    # Group and reformat the data.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Get the figure for the output.
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )

    fig.savefig('Medical Data Visualizer\catplot.png')
    return fig


# Draw the Heat Map.
def draw_heat_map():

    # Clean the data.
    df_heat = df[(df['ap_lo'] < df['ap_hi'])]
    df_heat = df_heat[(df['height'] >= df['height'].quantile(0.025))]
    df_heat = df_heat[(df['height'] <= df['height'].quantile(0.975))]
    df_heat = df_heat[(df['weight'] >= df['weight'].quantile(0.025))]
    df_heat = df_heat[(df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix.
    corr = df_heat.corr()

    # Generate a mask for the upper triangle.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure.
    fig, ax = plt.subplots()
    sns.heatmap(corr, ax=ax, mask=mask, annot=True, center=0, robust=True, fmt='.1f')

    fig.savefig('Medical Data Visualizer\heatmap.png')
    return fig