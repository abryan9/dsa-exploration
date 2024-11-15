import math

def tsp_hk(distanceMatrix):
    numCities = len(distanceMatrix)
    print(f"\n+ numCities: {numCities}")
    if (numCities) <= 1:
        return 0
    
    memo = {}

    def find_tour_len(visitedCities, currentCity):
        P2P = f"{visitedCities:08b}-{currentCity:08b}"
        print(f"+ New entry: {P2P}")

        if (P2P in memo):
            print("  + Already calculated this.")
            return memo.get(P2P)
        
        if (visitedCities == (1 << numCities) - 1):
            print("  | + All cities visited.")
            return distanceMatrix[currentCity][-1] | 0
        
        minCost = math.inf

        for nextCity in range(numCities):
            print("  | + New column!")
            if not(visitedCities & (1 << nextCity)):
                updateChecked = visitedCities | (1 << nextCity)
                cost = distanceMatrix[currentCity][nextCity] + find_tour_len(updateChecked, nextCity)
                print(f"  | + This trip cost {cost}")
                minCost = min(minCost, cost)
            else:
                print("+ This entry already exists.")

        memo.update({P2P: minCost})
        return minCost
    
    minTourLen = math.inf

    for startCity in range(numCities):
        print("| + New row!")
        minTourLen = min(minTourLen, find_tour_len(1 << startCity, startCity))

    return minTourLen