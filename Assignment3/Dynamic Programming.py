"""
    Author: Lee Zhen Xuan
    StudentID: 31860532
    Last modified: 6/5/2022
"""
def mergeSort(arr):
    """
    Author: Lee Zhen Xuan
    StudentID: 31860532

    This function mergeSort sorts a list of list, by increasing order based on the second index of the list of list
    Input:
        arr: a list of list that is to be sorted based on the 2nd index of the list of list
    Time complexity:
        Best: O(n*log n) where n is the length of the array
        Worst: O(n*log n) where n is the length of the array
    Space complexity:
        Input: O(n)
        Aux : O(n)
    """
    if len(arr) > 1:
        #partitions the array into 2 everytime, where left_arr are the elements from the start to the mid
        left_arr = []
        for i in range(len(arr) // 2):
            left_arr.append(arr[i])
        #the right_arr are elements from the mid to the end
        right_arr = []
        for i in range(len(arr) // 2, len(arr)):
            right_arr.append(arr[i])

        mergeSort(left_arr)
        mergeSort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr)  and j< len(right_arr):
        #sort the whole array based on comparing the left and the right side of the array
            if left_arr[i][2] < right_arr[j][2]:
                arr[k] = left_arr[i]
                i+=1
                k+=1
            elif left_arr[i][2] > right_arr[j][2]:
                arr[k] = right_arr[j]
                j+=1
                k+=1

            else:
                arr[k] = right_arr[j]
                j+=1
                k+=1
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1


def binary_Search(attacks, n):
    """
    Author: Lee Zhen Xuan
    StudentID: 31860532

    Reference: based on the Binary Search algorithm from FIT1045 2021, Y1S1 Week 6
    This function find the index that is closest to the end (2nd index of the list of list) of the list of list

    Precondition: The input array should be sorted
    Postconditon: The index closest to n is found

    Input:
        attacks: a list of list where the inner list contains at least 3 elements
        n: the index that the closest index to this index is to be found
    Output:
        m where the index is the closest to n,
        -1 where the index is not within the array



    Time complexity:
        Best: O(1) where the index to be found is in the middle of the array
        Worst: O(log n) where n is the length of the input array

    Space complexity:
        Input: O(1)
        Aux : O(1)
    """

    l = 0
    r = n


    while l <= r:
        #compares based the middle value, and if the middle value is less than the value to be found, move the right indicator

        m = (l + r) // 2
        if attacks[m][2] < attacks[n][1]:
            if attacks[m + 1][2] < attacks[n][1]:
                l = m + 1
            else:
                return m
        else:
            r = m - 1

    # return the negative index if no closest day to start is found
    return -1


def hero(attacks):
    """

    Author: Lee Zhen Xuan
    StudentID: 31860532

    This function finds the number of consecutive attacks based on the start day(index 1), end day(index 2) and number of clones(index 3) where the total number of clones is the maximum
    Preconditon: Merge sort and Binary search are implemented correcty to search for the consecutive days of attacks
    Postcondition: The maximum possible clones to be attacked is calculated from the start to the end of the array based on all the attacks

    Input:
        attacks: a list of attacks that consists of 4 elements
                    - the multiverse number that is attacked
                    - the starting day of the attack
                    - the ending day of the attack
                    - the number of clones available from the starting day to ending day
    Output:
        result: A list of consecutive attacks based on the starting day and ending day where the number of clones defeated is the maximum

    Time complexity:
        Best: O(N log N) where N is length of attacks
        Worst: O(N log N) where N is the length of the attacks

    Space complexity:
        Input: O(N)
        Aux: O(N)
    """

    max = attacks[0]
    #if there is only one attack, can only attack that many clones
    if len(attacks) ==1:
        return attacks


    #sorts the attacks based on the ending day of the attack to find the closest value of start day of current attack to ending day
    mergeSort(attacks)
    clonesArr = [None] * len(attacks)
    attacksIndex =[]
    for i in range(len(attacks)):
        attacksIndex.append([])
    #initialize the first count of clones attack as the number of clones of first attack
    clonesArr[0] = attacks[0][3]
    attacksIndex[0].append(0)
    for i in range(1, len(attacks)):
        clones = attacks[i][3]
        if binary_Search(attacks, i) != -1:
            clones += clonesArr[binary_Search(attacks, i)]
        #compare if the value looped until is the maximum clones to attack or not
        if clonesArr[i - 1] < clones:
            clonesArr[i] = clones
            if binary_Search(attacks, i) != -1:
                attacksIndex[i] = attacksIndex[binary_Search(attacks, i)].copy()
            attacksIndex[i].append(i)
        else:
            attacksIndex[i] = attacksIndex[i - 1].copy()
            clonesArr[i] = clonesArr[i - 1]


    result = []
    #attacksIndex's last elements stores all the index of consecutive attacks that gives maximum clones to attack
    for i in range(len(attacksIndex[-1])):
        result.append(attacks[attacksIndex[-1][i]])
    return result




def best_revenue(revenue,travel_days,start):
    """
    Author: Lee Zhen Xuan
    StudentID: 31860532

    This function is to find he maximum possible revenue from the starting day
    Precondition: the length of travel_days and the number of elements inside each element of travel_days must be equal to the number of cities
    Postcondition: The maximum possible revenue based on the starting day is found

    Input:
        revenue: a list of lists where each element is the revenue that can be made based on the day and city
        travel_days: a list of lists that contains the number of days to travel from one city to another, and -1 if city cannot be travelled to another city

    Output:
        The maximum possible profit based on the starting day

    Time complexity:
        Best: O(n^2 (d)) where n is the number of cities, and d is the number of days
        Worst: O(n^2 (d)) where n is the number of cities, and d is the number of days

    Space complexity:
        Input: O(n)
        Aux: O(n)

    """
    memo = []

    for i in range(len(revenue)):
        #initialize a new list of revenue to store the maximum revenue
        memo.append([0])

        for j in range(len(revenue[0]) - 1):
            memo[i].append(0)
    # initialize the revenues from the last day
    for i in range(len(revenue[0])):
        memo[-1][i] = revenue[-1][i]
    # looping through each revenue, and choosing if to stay, or to travel to give the maximum profit
    for days in range(len(revenue) - 1, -1, -1):
        for city in range(len(revenue[0])):

            if days + 1 < len(revenue):
                #update the current day with the next day
                memo[days][city] = revenue[days][city] + memo[days + 1][city]
            for k in range(len(travel_days[0])):
                #if can travel from that city to city, and the day does not exceed the limit
                if travel_days[city][k] != -1 and travel_days[city][k] + days <= len(revenue) - 1:
                    #compare and make decision to travel or stay
                    if memo[days][city] < memo[travel_days[city][k] + days][k]:
                        memo[days][city] = memo[travel_days[city][k] + days][k]

    return memo[0][start]

