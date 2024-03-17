with open('day5.txt', 'r') as file: 
    file_iterator = iter(file)
    line = next(file_iterator)
    seeds = [int(x) for x in line.split()[1:]]

    
    line = next(file_iterator)
    line = next(file_iterator)
    line = next(file_iterator)
    
    seed_to_soil = []
    while line != '\n':
        seed_to_soil.append([int(x) for x in line.split()])
        line = next(file_iterator)

    line = next(file_iterator) 
    line = next(file_iterator)

    soil_to_fertilizer = []
    while line != '\n':
        soil_to_fertilizer.append([int(x) for x in line.split()])
        line = next(file_iterator)

    line = next(file_iterator)
    line = next(file_iterator)

    fertilizer_to_water = []
    while line != '\n':
        fertilizer_to_water.append([int(x) for x in line.split()])
        line = next(file_iterator)

    line = next(file_iterator)
    line = next(file_iterator)

    water_to_light = [] 
    while line != '\n':
        water_to_light.append([int(x) for x in line.split()])
        line = next(file_iterator)
    
    line = next(file_iterator)
    line = next(file_iterator)

    light_to_temperature = []
    while line != '\n':
        light_to_temperature.append([int(x) for x in line.split()])
        line = next(file_iterator)

    line = next(file_iterator)
    line = next(file_iterator)

    temperature_to_humidity = []
    while line != '\n':
        temperature_to_humidity.append([int(x) for x in line.split()])
        line = next(file_iterator)

    line = next(file_iterator)

    humidity_to_location = []
    j = 0
    while j != 16: 
        line = next(file_iterator)
        humidity_to_location.append([int(x) for x in line.split()])
        j += 1

def transformation(original, matrix): 
    for row in matrix: 
        lower = row[1]
        upper = row[1] + row[2] - 1

        if original >= lower and original <= upper: 
            original += (row[0] - row[1])
            return original # if we do not return here might run again.
        
    return original 


def journey(seed): 
    soil = transformation(seed, seed_to_soil)
    fertilizer = transformation(soil, soil_to_fertilizer)
    water = transformation(fertilizer, fertilizer_to_water)
    light = transformation(water, water_to_light)
    temperature = transformation(light, light_to_temperature)
    humidity = transformation(temperature, temperature_to_humidity)
    location = transformation(humidity, humidity_to_location)
    return location 

print(journey(72))


    