import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file

    df=pd.read_csv('epa-sea-level.csv')
    #print(df.dtypes)

    # Create scatter plot
    colors=(0,0,0)
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], marker='o',color=colors)

    # Create first line of best fit
    result=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    xvals=np.arange(1880,2050,1)
    plt.plot(xvals,result.slope*xvals+result.intercept,'r' ,label='fitted line')
    #plt.show()

    # Create second line of best fit
    df2=df.iloc[120:134,0:2]
    #df2.index=df2['Year']
    #print(df2)
    result2=linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    valsx=np.arange(2000,2050,1)
    plt.plot(valsx, result2.slope*valsx+result2.intercept, 'g',label='from 2000 fitted line', color='blue')
    #plt.show()
                   
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    #plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

