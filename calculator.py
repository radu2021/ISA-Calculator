import numpy as np

def temp_at_alt(altitude):
    if altitude >= 0 and altitude <= 11000:
        temperature =  288.15 + ((altitude/1000)*-6.5)
    elif altitude > 11000 and altitude <= 20000:
        temperature = 216.65
    elif altitude > 20000 and altitude <= 32000:
        temperature = 216.65 + ((altitude-20000)/1000)
    elif altitude > 32000 and altitude <= 47000:
        temperature = 228.65 + ((altitude-32000)*2.8)/1000
    return round(temperature, 3)

def pressure_at_alt(altitude):    
    if altitude > 11000 and altitude <= 20000:
        pressure = 22625.79149*np.exp((-9.80665*(altitude-11000))/(288.150*temp_at_alt(altitude)))
    elif altitude >= 0 and altitude <= 11000:
        pressure = 101325*((temp_at_alt(altitude)/288.15)**(-(9.80665/((-6.5/1000)*287))))
    elif altitude > 20000 and altitude <= 32000:
        pressure = 22625.79149*((temp_at_alt(altitude)/temp_at_alt(20000))**(-(9.80665/((1/1000)*287))))
    elif altitude > 32000 and altitude <= 47000:
        pressure = 3585.9947911666286*((temp_at_alt(altitude)/temp_at_alt(32000))**(-(9.80665/((2.8/1000)*287))))
    return round(pressure, 3)

def density_at_alt(altitude):
    return round((pressure_at_alt(altitude))/(287*temp_at_alt(altitude)), 3)
