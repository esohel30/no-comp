times = [46, 68, 98, 66] 
records = [358, 1054, 1807, 1080]

def dist_traveled(charge, time):
    time_remaining = time - charge
    distance_traveled = time_remaining * charge
    return distance_traveled

def beat_record(time, record): 
    count = 0 
    for i in range(time + 1):
        if dist_traveled(i, time) > record: 
            count += 1

    return count 

def solve_puzzle(times, records): 
    product = 1 
    for i in range(len(times)):
        product *= beat_record(times[i], records[i])

    return product

# Part two: In reality, there is only one race. 

times = 46689866
records =  358105418071080

print(beat_record(times, records))