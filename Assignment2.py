from re import A
import statistics
import pandas

series=pandas.Series([10,50,80,70,49,23,11,4])
print("Min")
print(series.min())
print("Max")
print(series.max())
print("Mean")
print(series.mean())
print("Standard Deviation")
print(series.std(axis=0,skipna=True))
print("Variance")
print(statistics.variance(series))

