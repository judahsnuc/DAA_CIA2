def TSP(list2d):
    import copy
    origin = input("enter source node -> ")
    result = [int(origin)]
    iteraction, indicator = int(origin) -1, 0
    distance, copy = [], copy.deepcopy(list2d)
    for j in range(1, len(list2d)):
        for x in range(len(list2d)):
            list2d[x][iteraction] = 999
        distance.append(min(list2d[iteraction]))
        for i in range(len(list2d)):
            if min(list2d[iteraction]) == list2d[iteraction][i]:
                indicator = i
        list2d[indicator][iteraction] = 999
        result.append(indicator+1)
        iteraction = indicator
    result.append(int(origin))
    a = copy[result[-2]-1][int(origin)-1]
    distance.append(a)
    print("The result is " + str(result) + "\nwith a distance of " + str(sum(distance)) )

TSP([[999,120,220,150,210],[120,999,100,110,130],[220,80,999,160,185],[150,999,160,999,190],[210,130,185,999,999]])
    
#Result 
#source node -> 3
#the result is [3, 2, 4, 1, 5, 3]
#with a distance of 735
