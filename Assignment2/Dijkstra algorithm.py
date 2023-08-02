'''
Author: Lee Zhen Xuan 31860532

Last Modified: 14/4/2022

Task 1: Location Optimisation
functions: ideal_place (main function), medianofmedian, findkthSmallest, quickSelect, insertionSort

Task 2: On the Way
functions: routing (main function)
the MinHeap class is modified based on the unit FIT1008, 2021, Week12 Workshop Malaysia

'''
import math


def ideal_place(inputlist):
    """
      This function finds the optimal location where the location to all of the locations in relevant is the minimum
      Written by Lee Zhen Xuan 31860532
      Precondition: Each of the items in the relevant are lists, where they represents the coordinates of the locations
      Postcondition: The distance from the starting index to each of the locations is the shortest.
      Input:
        inputlist: inputlist  contains all the coordinates of the n relevant points
      Time complexity:
          Best: O(n) where n is the number of items in the inputlist
          Worst: O(n) where n is the number of items in the inputlist
      Space complexity:
          Input: O(n)
          Aux: O(V) where v is the number of unique locations in the roads
      """

    return [medianofmedian(inputlist,0), medianofmedian(inputlist,1)]
'''
medianofmedian sorts the inputlist based on the sublist of list where each sublist has a maximum number of items of 5 
Then, the function finds the median of each of the sublist, and finds the median of median of each of the sublist
'''
def medianofmedian(inputlist,k):
    count = 0
    sublist = []
    subcount = 0



    for i in range(len(relevant)):
        if count % 5== 0:
            sublist.append([])
            subcount += 1
        sublist[subcount-1].append(relevant[i][k])
        count+=1

    for j in range(len(sublist)):
        insertionSort(sublist[j])

        sublist[j] = sublist[j][len(sublist[j]) // 2]

    if len(sublist) %2 ==0:
        pivot = sublist[(len(sublist)//2)-1]

    else:
        pivot = sublist[len(sublist)//2]


    return findKthSmallest(sublist,pivot)

'''
This function is used the find the index of the kth smallest value in the list
'''
def findKthSmallest(nums,pivotv):

    k = (len(nums)-1)//2
    def quickSelect(l,r,pivot):
        p = l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p+=1
        nums[p] , nums[r] = nums[r], nums[p]
        if p > k:
             return quickSelect(l, p-1,nums[(r-l)//2])
        elif p < k:
            return quickSelect(p+1 ,r,nums[(r-l)//2])
        else:
            return nums[p]

    return quickSelect(0,len(nums)-1, pivotv)

'''
This function sorts the list with insertionSort
'''
def insertionSort(inputList):
    # Traverse through 1 to len(arr)
    for i in range(1, len(inputList)):

        value = inputList[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and value< inputList[j]:
            inputList[j + 1] = inputList[j]
            j -= 1
        inputList[j + 1] = value



class RoadGraph:

    """
    Graph class for Question 02 of Assignment02
    """
    def __init__(self,start,roads,preprocessed):

        """
          This function calculates the shortest distance from the starting location, to each of the locations in the roads.
          Written by Lee Zhen Xuan 31860532
              Precondition: Each of the items in the roads, and start is/are Vertices, Connecting Vertices, Weights, and a starting Vertex respectively represented by Integers.
              Postcondition: The distance from the starting index to each of the locations is the shortest.
              Input:
                  start: a starting location represented by an Integer
                  roads: roads is a list of tuples, representing the Vertex, Connecting Vertex and the Weight of the edges.
                  preprocessed: A boolean value, where is False, u and v will swap. This is mainly to find the shortest distance from end to all locations
              Time complexity:
                  Best: O(ElogV) where E is the set of roads, and V is the unique locations of roads
                    Worst: O(ElogV) where V is the number of unique locations in roads
              Space complexity:
                  Input: O(V) where v is the number of unique locations in the roads
                  Aux: O(V) where v is the number of unique locations in the roads
              """
        self.discovered = 0
        self.maxVertex = 0
        self.path = []
        self.preprocessed = preprocessed


        self.distances = []
        self.tracks = []
        if preprocessed == False:
            roads.append((start,start,0))
            for j in range(len(roads)):
                if roads[j][0] > self.maxVertex:
                    self.maxVertex = roads[j][0]

            self.vertices = [None] * (self.maxVertex+1)
            for i in range(self.maxVertex+1):
                self.vertices[i] = Vertex(i)
        elif preprocessed == True:
            roads.append((start, start, 0))
            for j in range(len(roads)):
                if roads[j][1] > self.maxVertex:
                    self.maxVertex = roads[j][1]

            self.vertices = [None] * (self.maxVertex + 1)
            for i in range(self.maxVertex + 1):
                self.vertices[i] = Vertex(i)





        for edge in roads:
            if preprocessed == False:

                if self.vertices[edge[0]]!= None:
                    self.vertices[edge[0]].add_edge(Edge(edge[0], edge[1], edge[2]))
            elif preprocessed == True:
                if self.vertices[edge[1]] != None:
                    self.vertices[edge[1]].add_edge(Edge(edge[1],edge[0],edge[2]))

        self.q = MinHeap(self.maxVertex + 1)
        self.vertices[start].distance = 0
        self.q.add((self.vertices[start].distance, self.vertices[start]))
        u = None
        '''
        This part of the function is to perfomr Dijkstra to get the distance 
        '''
        while self.q.length > 0:
            u = self.vertices[(self.q.get_min().id)]


            u.visited = True
            for edge in u.edges:
                v = self.vertices[edge.v]

                if v.discovered == False:
                    v.discovered = True
                    v.distance = u.distance + edge.w
                    self.path.append([edge.u, edge.v])
                    v.previous = u
                    self.q.add((v.distance, v))
                if not v.visited:
                    if v.distance > u.distance + edge.w:
                        v.distance = u.distance + edge.w
                        u.track.append([u.id , v.id])
                        v.previous = u
                        self.q.add((v.distance, v))
                    for i in range(self.q.length):
                        if self.q.the_array[i]!= None and str(self.q.the_array[i][1].id) == v.id:
                            self.q.the_array[i][0] = v.distance
                            self.q.rise(i)


        '''
        This part of the function find the paths of the Vertices to all of the locations
        '''
        self.distances = []
        for i in self.vertices:
            self.distances.append(i.distance)
        for i in self.path:
            if len(self.vertices[i[-1]].track)==1:
                self.vertices[i[-1]].track[0] = []
            self.vertices[i[-1]].track.append(i)
        output = []
        for j in self.vertices:
            output.append(j.track)

        self.path = output

        for k in range(len(self.vertices)):

            if len(self.vertices[k].track) == 0:
                continue
            while self.vertices[k].track[-1][0] != start:
                self.vertices[k].track.append(self.path[self.vertices[k].track[-1][0]][0])
        for l in range(len(self.vertices)):
            for m in range(len(self.vertices[l].track)):

                if len(self.vertices[l].track[m])!= 0:
                    self.vertices[l].track[m] = self.vertices[l].track[m][0]
        for n in range(len(self.vertices)):
            if preprocessed == False:
                self.vertices[n].track.reverse()
                self.vertices[n].track.append(n)
            else:
                self.vertices[n].track.append(n)





    def __str__(self):
        self.distance2 = []
        for i in self.vertices:
            self.distance2.append(i.distance)

        self.distance = self.distance2
        return str(self.distance)



def routing(start, end, chores_location):
    '''
    Written by Lee Zhen Xuan 31860532
    The function finds the shortest route from the start location to the end loation, going through at least 1 of the locations listed in chores_location
    This implementation checks the length from start, to each of the chores location, and each of the chores location to the end, then adds them up together
    The total of the added numbers is equals to the shortest distance, from start passing by one of the chores location (or None) to the end.

    Precondition: Each of the items in the roads, and chores_location are Vertices, Connecting Vertices, Weights, and Vertices respectively represented by Integers.
    Postcondition: The distance from the Vertices to the chores_locations and chores_locations to the end are the shortest distance
    Input:
        start: a non-negative integer that represents the starting location
        end: a non-negative integer that represents the ending location of the journey
        chores_location: a non-empty list of non-negative integers that stores all of the locations where the chores could be performed
        Time complexity: O(NM), where N is the number of items in wordlist, and M is the length of words in wordlist and word
            Best case complexity = Worst case complexity: O(NM) where N is the number of items in wordlist and M is the length of the words in wordlist and word
        Space complexity:
            O(V) where V is the number of unique locations in roads
            O(E) where E is the number of items roads

    '''

    roadGraph1 = RoadGraph(start,roads,False)


    str(roadGraph1)
    startToChoresList = []
    for i in range(len(chores_location)):
        starttoChores = roadGraph1.distance[chores_location[i]]

        startToChoresList.append(starttoChores)


    roadGraph3= RoadGraph(end,roads,True)
    str(roadGraph3)
    endToChoresList = []
    for i in range(len(chores_location)):
        endtoChores = roadGraph3.distance[chores_location[i]]
        endToChoresList.append(endtoChores)




    totalList = []
    for i in range(len(startToChoresList)):
        if endToChoresList[i] == math.inf or startToChoresList[i] == math.inf:
            totalList.append(math.inf)
        else:
            totalList.append(int(startToChoresList[i])+ int(endToChoresList[i]))


    minTotal = totalList[0]
    for i in range(len(startToChoresList)):
        if totalList[i] < minTotal:
            minTotal = totalList[i]
    if minTotal == math.inf:
        return None
    minIndex = []
    for i in range(len(startToChoresList)):
        if minTotal == totalList[i]:
            minIndex.append(i)

    roadGraph = RoadGraph(start,roads,False)
    startToChoresVertex = roadGraph.vertices[chores_location[minIndex[0]]].track
    roadGraph2 =RoadGraph(chores_location[minIndex[0]],roads,False)
    choresToEndVertex = roadGraph2.vertices[end].track
    startToChoresVertex.pop()
    result = startToChoresVertex +choresToEndVertex
    l = 0
    r = 0+1
    while r< len(result):
        if result[l] == result[r]:
            result.pop(r)
        l += 1
        r +=1

    return result


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.distance = math.inf
        self.visited = False
        self.discovered = False
        self.previous = 0
        self.track = []
        self.tracks = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        output = str(self.id)
        for edge in self.edges:
            output = output + "\n [" + str(edge) + "]"
        return output
class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        output = "u: " + str(self.u) + ", v: " + str(self.v) + ", w: " + str(self.w)
        return output



'''
Heap implemented using an array
__author__ = "Brendon Taylor, Modified by Lee Zhen Xuan"
'''
from typing import Generic

'''
MinHeap is a reference (but modified) version from the unit FIT1008, Week 12 Workshop Malaysia
'''

class MinHeap():
    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        self.length = 0
        # self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)
        self.the_array = [None] * (max_size+1)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:


        item = self.the_array[k]

        while k > 1 and item[0] < self.the_array[k // 2][0]:

            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element) -> bool:

        if self.is_full():
            raise IndexError
        self.length += 1

        self.the_array[self.length] = element
        self.rise(self.length)
    def serve(self):
        if self.the_array.__len__() >1:
            self.the_array[1], self.the_array[self.the_array.__len__()-1] = self.the_array[self.the_array.__len__()-1], self.the_array[1]
            self.length -=1
            output = self.the_array[self.the_array.__len__()-1]
        return output
    def swap(self):
        self.the_array[1], self.the_array[self.the_array.__len__() - 1] = self.the_array[self.the_array.__len__() - 1], \
                                                                          self.the_array[1]

    def largest_child(self, k: int) -> int:

        if 2 * k == self.length or \
                self.the_array[2 * k][0] < self.the_array[2 * k + 1][0]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:

        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.largest_child(k)
            if self.the_array[max_child][0] >= item[0]:
                break
            self.the_array[k] = self.the_array[max_child]
            k = max_child

        self.the_array[k] = item

    def get_min(self):

        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1][1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return max_elt














