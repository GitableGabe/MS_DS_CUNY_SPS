# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:55:27 2020

@author: gcamp

Continued outputs while follwoing alond with 
'Doing Math with Python text'
"""


import matplotlib_venn
from pylab import plot, show, title, xlabel, ylabel, legend, axis

#list creation
x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]

# plotting
#from pylab import plot, show
#import done at start of file

plot(x_numbers, y_numbers)
show()
plot(x_numbers, y_numbers, marker='o')
show()
plot(x_numbers, y_numbers, '+')
show()
# Basic scatter plot
nyc_temp=[53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7,
          56.4, 57.3]
years=range(2000,2013)
plot(years,nyc_temp, marker='*')

# Overlapping graphs
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0,
                  45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 
                  51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 
                 43.9, 41.5]
months = range(1,13)
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012)

#Seperated method
plot(months, nyc_temp_2000)
plot(months, nyc_temp_2006)
plot(months, nyc_temp_2012)
show()

# With a legend
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0,
                  45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 
                  51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 
                 43.9, 41.5]
months = range(1,13)
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012)
#from pylab import legend
#import done at start of file
legend([2000,2006,2012])

#More customizing
#from pylab import plot, show, title, xlabel, ylabel, legend
#done at start of file
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012)
title('Average monthly tempature in NYC')
xlabel('Month')
ylabel('Temperature')
legend([2000, 2006, 2012])

#axis customizing
#from pylab import axis
#done at start
nyc_temp=[53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7,
          56.4, 57.3]
plot(nyc_temp, marker='o')
axis()
axis(ymin=0)

# All four axis extremes xmin xmax ymin ymax
nyc_temp=[53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7,
          56.4, 57.3]
plot(nyc_temp, marker='o')
axis([5,10,5,20])