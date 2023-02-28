import numpy as np

SPEED_OF_LIGHT = 299792458

def makeConversionFactor(input,output):    
    if input is not None and output is not None:
        return 10**findScaling(input[:-1])*10**-findScaling(output[:-1])*findUnits(input[-1],output[-1])
    else:         
        return 1


def findScaling(input):    
    if input == 'd':
        return -1
    elif input == 'c':
        return -2
    elif input == 'm':        
        return -3
    elif input == 'mu':                
        return -6
    elif input == 'n':        
        return -9        
    elif input == 'p':      
        return -12        
    elif input == 'f':              
        return -15
    elif input == 'a':                              
        return -18     

def findUnits(input_units,output_units):
    if input_units == 'm' and output_units == 's':
        return 2/(SPEED_OF_LIGHT/1.00028609)
    elif input_units == 's' and output_units == 'm':
        return (SPEED_OF_LIGHT/1.00028609)/2
    else:
        return 1        


def main():
    print(makeConversionFactor('fs','nm'))
    print(makeConversionFactor('fs','fs'))
    print(makeConversionFactor('mm','fs'))

if __name__=="__main__":
    main()