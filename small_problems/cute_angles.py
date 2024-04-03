# Write a function that takes a floating point number representing an angle 
# between 0 and 360 degrees and returns a string representing that angle in 
# degrees, minutes, and seconds. You should use a degree symbol (˚) to 
# represent degrees, a single quote (') to represent minutes, and a double 
# quote (") to represent seconds. There are 60 minutes in a degree, and 60 
# seconds in a minute.

DEGREE_SYMBOL = '°'
MINUTES_PER_DEGREE = 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE

def pad_zeroes(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string

def dms(degrees_float):
    degrees_int = int(degrees_float)
    minutes = int((degrees_float - degrees_int) * MINUTES_PER_DEGREE)
    seconds = int(
        (degrees_float - degrees_int - (minutes / MINUTES_PER_DEGREE)) *
        SECONDS_PER_DEGREE
    )

    return (f"{degrees_int}{DEGREE_SYMBOL}"
            f"{pad_zeroes(minutes)}'"
            f'{pad_zeroes(seconds)}"')




# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")