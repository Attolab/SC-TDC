import numpy as np
import re


def string2substring(string,regexp):
    return re.findall(regexp, string)

def sortArray(array_input,ordering):
    # 1: Sort up
    if ordering == 1:
        series = np.sort(array_input)
    # 2: Sort down
    elif ordering == 2:
        series = series[np.argsort(-array_input)]
    # 3: Staggered Acending
    elif ordering == 3:
        series = np.sort(array_input)
        firstHalf = series[0::2]
        secondHalf = series[1::2]
        # Reverse the second half to get staggered ascending:
        secondHalf = secondHalf[::-1]
        series = np.concatenate((firstHalf, secondHalf))
    # 4: Staggered decending
    elif ordering == 4:
        series = series[np.argsort(array_input)]
        firstHalf = series[0::2]
        secondHalf = series[1::2]
        # Reverse the first half to get staggered decending:
        firstHalf = firstHalf[::-1]
        series = np.concatenate((firstHalf, secondHalf))
    else:
        # 0: No sorting:
        series = array_input        
    return series

def parseStringInput(string="0:1:10",ordering=0):
    class DelayParseException(Exception):
        def __init__(self, message):
            Exception.__init__(self, message)

    # First check for paranthesis enclosed ranges:
    measurement_strings = string2substring(string,"(\(?[-\d.,;:\s]+\)?(?:\*\d+)?)")
    parsed_arrays = np.asarray([])
    # print(f"delayInput: {delayInput}")
    # print(f"meansurement_strings: {measurement_strings}")
    for measurement_string in measurement_strings:
        # Measurement string should always have either 1 or 2 substrings, depending
        substrings = string2substring(string,"[-\d.,;:\s]+")
        # print(f"substrings: {substrings}")
        # print(f"len(substrings): {len(substrings)}")
        multiplier = 1
        # if len(substrings) == 2:
        #     multiplier = int(substrings[1])
        # elif len(substrings) == 1:
        #     multiplier = 1            
        # else:
        #     raise DelayParseException(f"Unable to make out a measurement and multiplier for this string: {measurement_string}, which gives {len(substrings)} substrings")
        # print(multiplier)
        parsed_array = np.asarray([])
        # Split the string on ; first.
        series_strings = re.findall("[^;]+", substrings[0])
        # Now do something for each string that defines a series:
        for series_string in series_strings:
            # Then split on , or any whitespace to find the range specifiers: "?:?:?"
            range_strings = re.findall("[^,\s]+", series_string)
            # print(f"range strings: {range_strings}")
            series = np.asarray([])
            for range_string in range_strings:
                # Extract the numbers by splitting on :.
                number_strings = re.findall("[^:]+", range_string)
                # If the range specifier is not either 1 or 3 string representations of numbers, the input is invalid:
                # 3 Numbers specify a range
                if len(number_strings) == 3:
                    start,step,stop = [float(number) for number in number_strings]
                    numberofsteps = abs(round(1.0 + abs((stop - start)/step)))                    
                    this_range = np.linspace(start,stop,int(numberofsteps))
                    # print(f"this_range: {this_range}")
                    # range = np.arange(start, stop, step)
                    # range = np.append(range,stop)
                # 1 number just specifies a single number
                elif len(number_strings) == 1:
                    this_range = np.asarray([float(number_strings[0])])
                else:
                    raise DelayParseException(
                        f"Error! Following substring does not lead to either 1 or 3 numbers: {range_string}")
                # Add all of the series to the range:
                series = np.concatenate((series, this_range))
                # print(f"series: {series}")

            series = sortArray(series,ordering) 
            # Concatenate together all the delays
            parsed_array = np.concatenate((parsed_array, series))

        # Repeat according to the multiplier, and add to all_delays
        parsed_arrays = np.concatenate((parsed_arrays, np.tile(parsed_array, multiplier)))

    return parsed_arrays
