# MatPlotLib 

## Description 
Used for plotting on a graph

## Scatter Plot
* Set the properties of the graph and then call "show" property to show the Result
  * marker and c show the points as red crosses instead of the default blue dots.
```
# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()
```
