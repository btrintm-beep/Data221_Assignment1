def distributionAnalysis(numbersList):


    # Make sure for valid input
    if len(numbersList) == 0:
        return "The list cannot be empty."

    # Make sure the values are integers or floats (whole numbers, decimal value)
    for value in numbersList:
        if not isinstance(value, (int, float)):
            return "All values in the list must be numbers."

    totalElements = len(numbersList)

    # Make list with unique values
    uniqueValues = sorted(set(numbersList))

    # Make a dictionary 
    distributionDictionary = {}

    # go through every unique value
    for key in uniqueValues:
        countLessOrEqual = 0

        # start a loop to count the ammount of values under or equal to value of number
        for number in numbersList:
            if number <= key:
                countLessOrEqual += 1

        # Calculate the percentage
        percentage = (countLessOrEqual / totalElements) * 100

        # Store the calculated percentage in the dictionary
        distributionDictionary[key] = percentage

    return distributionDictionary


# get the user to input numbers seperated by commas
userInput = input("Enter a list of numbers separated by spaces: ")

# have the input be split into lists of strings
inputList = userInput.split()

numbersList = []

# Convert input values to numbers
for value in inputList:
    try:
        numbersList.append(float(value))
    except:
        print("All values must be numbers.")
        numbersList = []
        break

# run the function but only when the input is valid
if len(numbersList) > 0:
    result = distributionAnalysis(numbersList)
    print("Distribution Dictionary:")
    print(result)
