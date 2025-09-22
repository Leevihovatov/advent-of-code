from math import sqrt, floor, ceil
def main():
    with open("input06.txt", "r") as f:
        data = f.read().splitlines()
    
    silver = 1
    gold = 0

    times = data[0].split()[1:]
    distances = data[1].split()[1:]

    second_time = ''
    second_distance = ''
    for i in range(len(times)):
        wins = 0
        for j in range(1,int(times[i])): # No need to check zero time and full time presses
            d = j*(int(times[i])-j)
            if d > int(distances[i]):
                wins += 1
        silver *= wins
        second_time += times[i]
        second_distance += distances[i]

    # Math, haven't done this in 5 years
    t = int(second_time)
    d = int(second_distance)
    # -x^2 + time x - distance = 0
    z = []
    z.append((-t+sqrt(t**2-4*d))/-2)
    z.append((-t-sqrt(t**2-4*d))/-2)

    # Upside down parabola
    gold = ceil(max(z))-floor(min(z))-1
    
    print(f'Silver: {silver}')
    print(f'Gold: {gold}')

if __name__ == "__main__":
    main()