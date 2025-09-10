import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data.
df = pd.read_csv(r'Page View Time Series Visualizer\fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data.
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot.

    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(data=df, x=df.index, y='value', ax=ax, color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig.
    fig.savefig(r'Page View Time Series Visualizer\line_plot.png')
    return fig

def draw_bar_plot():
    # Group data to show average daily page views for each month grouped by year.
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot.
    fig = df_bar_grouped.plot(kind='bar', figsize=(12, 8)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])


    # Save image and return fig.
    fig.savefig(r'Page View Time Series Visualizer\bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots.
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
   

    # Draw box plots.
    fig, axs = plt.subplots(ncols=2, figsize=(15, 5))
    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x='month', y='value', data=df_box, ax=axs[1], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig.
    fig.savefig(r'Page View Time Series Visualizer\box_plot.png')
    return fig
