"""
Author: Lee Zhen Xuan 31860532
Last Modified: 30/5/2022

"""


# %%

class Vertex:
    def __init__(self, data = None):
        self.data = data
        self.nights = [None] * 31
        self.admins = [None]


def allocate(preferences, sysadmins_per_night,max_unwanted_shifts, min_shifts):
    '''
    This function returns a lists of lists allocation where allocation[i][j] is 1 if the sysadmin numbered j is allocated to work on the night numbered i, and 0 otherwise
    Precondition: preferences is a list of is where each interior list represents a differnt day, and the values inside the interior list are either 0 or 1
    Postcondition: allocation is a list of list where allocation[i][j] is 1 if the sysadmin numbered j is allocated to work on the night numbered i, and 0 otherwise

    Input:
        preferences: a list of is where each interior list represents a differnt day, and the values inside the interior list are either 0 or 1
    Output:
        allocation: a list of list where allocation[i][j] is 1 if the sysadmin numbered j is allocated to work on the night numbered i, and 0 otherwise
    Time complexity:
        Best: O(N^2) where N is the length of preferences
        Worst: O(N^2) where N is the length of preferences
    Space complexity:
        Input: O(N)
        Aux: O(N)
    '''
    root = Vertex()
    root.admins = [None] * len(preferences[0])
    for i in range(preferences):
        for j in range(preferences):
            if preferences[i][j] == 1 and root.admins[j] != None:
                root.admins[j] = Vertex()
                root.admins[j].nights[i] = 1

class Node: 
    """
    This Node class is created as a vertex for the graph.
    """
    def __init__(self, level = 0, size = 27):
        # terminal $ at index 0
        self.link = [None] * size
        # data payload
        self.data = []
        # level of node
        self.level = level
        #self.largest stores the number of the deepest node 
        self.largest = 0
        #self.nodes stores all the nodes from the root to the current node
        self.nodes = [self]
        #self.letter stores the letter of the current node which will be useful for output
        self.letter = 0
       
class EventsTrie:

    def __init__(self, timelines):
        '''
        This function initializes all the suffixes of the words in timelines
        Precondition: Timelines contains a list of strings,where each letter represents unique events, and there are only a maximum of 26 unique events in total
        Postcondition: All the suffixes of the timelines are inserted into a list
        Input: 
            Timelines: A list of strings, where each letter in the string represents a timeline
        Output:
            self.timelines: A list that contains all the suffixes of the strings in timelines
        Timecomplexity:
            Best: O(NM^2) where N is the number of timelines in timelines, and M is the number of events in the longest timeline.
        Space complexity:
            Input: O(N)
            Aux: O(N)
        '''
        self.root = Node()
        self.max = []
        lst = []
        #looping through all the strings in timelines
        for word in range(len(timelines)):
            #looping through each letter in the string of timelines
            for i in range(len(timelines[word])):
                temp = ""
                #looping through each letter in all the suffixes
                for j in range(i, len(timelines[word])):
                    temp += timelines[word][j]
                #appending a list, to differerentiate unique words when inserting
                lst.append([temp,timelines[word],word])
       
        self.timelines = lst

      
    def insert(self,key, data, noccurences):
        '''
        This function inserts all the characters of a string into a suffix trie
        Precondition: Key is a list of strings,where each letter represents unique events, and there are only a maximum of 26 unique events in total
        Postcondition: self.max contains the longest chain event, where the number of timelines according to noccurences share that longest chain event
        Input: 
            Key: a string where each letter represents unique events, and there are only a maximum of 26 unique events in total
        Timecomplexity:
            Best: O(NM)
        Space complexity:
            Input: O(1)
            Aux: O(1)
        '''
        count_level = 1
        root = self.root
        #begin from root 
        current = self.root
        
        #go through the key one by one 
        for char in key:
            index = ord(char) - 97 +1 
            
            #If the path exists
            if current.link[index] is not None:
                current = current.link[index]  
                
            else:
                #if the path dosen't exist, create a new node 
                current.link[index] = Node(level = count_level)

                #Indicating the letter that has been added to the suffix tree in the Node
                current.link[index].letter = char

                #Nodes contains all the nodes from the root, to the current node.
                current.link[index].nodes += current.nodes
              
                current = current.link[index]
            if not (data in current.data):
                current.data.append(data)
            count_level +=1 

            #if the level is deeper than the previous level recorded, and the number of longest chain events is more than noccurences
            if(count_level>= root.largest and len(current.data)>= noccurences):
                root.largest = count_level
                self.max = current.nodes
  
    def getLongestChain(self, noccurence):
        '''
        This function returns a string that represents the longest chain of events that occurs in at least noccurence timelines.
        Precondition: self.timelines contains a list of strings,where each letter represents unique events, and there are only a maximum of 26 unique events in total
        Postcondition: Output contains a string that represents the longest chain of events that occurs in at least noccurence timelines
        Input: 
            noccurence: a positive integer in he range 1 to N
        Output: 
            output: a string that represents the longest chain of events that occurs in at least noccurence timelines.
        Timecomplexity:
            Best: O(K) where K is the length of the longest event chain that occur at least in noccurence number of timelines
        Space complexity:
            Input: O(1)
            Aux: O(1)
        '''  
        #looping through each of the suffixes of timelines, and inserting all the suffixes into the suffix tree with additional data
        for i in range(len(self.timelines)):
            self.insert(self.timelines[i][0],[self.timelines[i][1],self.timelines[i][2]],noccurence)
        output = ""
        #self.max contains the all the nodes of the longest chain event, in reverse
        if len(self.max)<= 1:
            return None
        else:
            for i in range(2,len(self.max)+1):

                output+= self.max[-i].letter
            return output

if __name__ == "__main__":

    timelines = ["abaaac", "dbce", "aabcba", "dbce", "caaaa"]


    myTrie = EventsTrie(timelines)
    noccurence = 2
    print(myTrie.getLongestChain(noccurence))





        



# %%
