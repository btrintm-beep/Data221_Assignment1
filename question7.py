def timeConversion(secondsSinceMidnight):
    
    # Make sure that the input is an integer
    if not isinstance(secondsSinceMidnight, int):
        return "Input must be a non-negative integer."

    # make sure that the input is either 0 or higher
    if secondsSinceMidnight < 0:
        return "Input must be a non-negative integer."

    # Total seconds in one day
    secondsInDay = 24 * 60 * 60

    # Reduce seconds to within one day
    secondsSinceMidnight = secondsSinceMidnight % secondsInDay

    # Calculate hours
    hours = secondsSinceMidnight // 3600

    # Calculate remaining seconds after hours
    remainingSeconds = secondsSinceMidnight % 3600

    # Calculate minutes
    minutes = remainingSeconds // 60

    # Calculate seconds
    seconds = remainingSeconds % 60

    # Figure out AM or PM
    if hours < 12:
        amOrPm = "AM"
    else:
        amOrPm = "PM"

    # Have the time be in a 24 hour scale
    displayHours = hours % 12
    if displayHours == 0:
        displayHours = 12

    # Return formatted string
    return str(displayHours) + " " + str(minutes) + " " + str(seconds) + " " + amOrPm

# Get the user to input
userInput = input("Enter the number of seconds since midnight: ")

# Make sure the input is valid
if not userInput.isdigit():
    print("Input must be a non-negative integer.")
else:
    # Convert input to integer
    secondsSinceMidnight = int(userInput)

    # Call function and print result
    result = timeConversion(secondsSinceMidnight)
    print("Converted Time:")
    print(result)
