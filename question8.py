import pandas as pd

# Have the data here
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Make the dataframe
dataFrame = pd.DataFrame(data)

#Make a column that multiplies A and B then after it adds C
dataFrame["Computed"] = (dataFrame["A"] * dataFrame["B"]) + dataFrame["C"]

# Print the final DataFrame
print(dataFrame)
