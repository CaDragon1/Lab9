############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer


print 'What temperature (in celcius) would you like to convert to fahrenheit?'
celTemp = int(raw_input())
print 'Calculating...'

fahrTemp = celTemp * 9
fahrTemp = fahrTemp / 5
fahrTemp = fahrTemp + 32

print 'The fahrenheit conversion of ' + str(celTemp) + ' degrees celcius is ' + str(fahrTemp) + ' degrees fahrenheit.'