'''
Author: Lee Zhen Xuan 31860532

Last Modified: 25/3/2022, 09:36 AM

Task 1: Partial Wordle Trainer
functions: trainer(main function), counting_sort_index, counting_sort

Task 2: Finding a Local Maximum
functions: localMaxima


'''

def trainer(wordlist, word, marker):
    '''
    Written by Lee Zhen Xuan 31860532
    This function filters the wordlist based on the guessed word and marker, where if the corresponding index at marker is 0, the words must have a character at that index that exists in another position where if the corresponding index at marker is 1, the words must have a character at that index that exists in the same position.

    Precondition: The length of each unique word in the wordlist is equal to the length of the guessed word and the length of the marker, and they consists of alphabetical letters that are in lowercase.
    Postcondition: Each of the characters of every word in wordlist where if it corresponds to 0 in that index, the character at that index exists in another position and if it corresponds to 1, that character at that index exists in the same position as guessed word
    Input:
        wordlist: a list of N words as strings of length M, where each word is unique, and each character of the word in the range of lowercase {a-z}
        word: is a string of length M that the user have guessed with each character in the range of {a-z}
        marker: is an array of integers of length X, where each element is in the range of {0,1}.
                0 denotes that the character at that index exists in another position.
                1 denotes that the character at that index exists in the same position.

        Return wordListResult: where each character that corresponds to 1 in guessed word is in the right position and letter, and 0 where the character is in another position other than 1 or that position
        Time complexity: O(NM), where N is the number of items in wordlist, and M is the length of words in wordlist and word
            Best case complexity = Worst case complexity: O(NM) where N is the number of items in wordlist and M is the length of the words in wordlist and word
        Space complexity:
            O(N) where N is the number of items in the wordlist
            O(N) where N is the number of items in the wordlist

    '''

    #This loop goes through each of the element in the marker, sorts the list based on the column alphabetically, and removes the words that does not matches with the guessed word if marker at the corresponding index is 0 and 1.
    #The loop only checks until the corresponding letter, where the alphabets that are larger than that letter are not checked.
    #Complexity: O(XN) where X is the length of marker, and N is the length of wordlist
    for i in range(len(marker)):
        continued = False
        filtered01 = []
        wordlist = counting_sort_index(wordlist, i)
        if marker[i] == 1:

            j = 0
            while j < len(wordlist):
                if wordlist[j][i] != word[i]:
                    if continued:
                        break
                elif wordlist[j][i] == word[i]:
                    filtered01.append(wordlist[j])

                    continued = True
                j += 1
        elif marker[i] == 0:
            for j in range(len(wordlist)):
                if wordlist[j][i] != word[i]:
                    filtered01.append(wordlist[j])
        wordlist = filtered01

    #Since the words that contains the letters which corresponds to marker 0 and 1 in the guessed words are removed, this loop filters the words in wordlist that contains all the same letters with the guessed word.
    wordListResult = []
    sortedLetters = counting_sort(word)
    #The complexity of this part of the function will be O(NM) where N is the number of items in wordlist, and M is the length of the words in wordlist and word
    for i in wordlist:
        if counting_sort(i) == sortedLetters:
            wordListResult.append(i)

    return wordListResult


def counting_sort_index(wordlist,col):
    '''
    Written by Lee Zhen Xuan 31860532
    This function sorts the words based on the columns/index of the letters.
    Precondition: All the letters in wordlist must have at least length of more than or equal to the value of col
    Postcondition: All the letters in wordlist are sorted based on the index of the letter.

    Input:
        wordlist: a list of N words as strings of length M, where each word is unique, and each character of the word in the range of lowercase {a-z}.
        col: the column/index of the letter that is wished to be sorted. col = 1 indicated that the words will be sorted based on the first letter.
    Return:
        sortedWords: a list of N word that has been sorted alphabetically based on the column/index of the letters


    '''
    if len(wordlist) ==0:
        return wordlist
    #This part of the function sorts finds the largest letter in the words based on the column of the words
    max_value = ord(wordlist[0][col])
    for i in wordlist:
        if ord(i[col]) > max_value:
            max_value = ord(i[col])


    #This part of the function sorts finds the smallest letter in the words based on the column of the words
    min_value = ord(wordlist[0][col])
    for j in wordlist:
        if ord(j[col]) < min_value:
            min_value = ord(j[col])

    #Count array contains the frequency of each of the letters based on the words index of the letters in each of the words starting from the smallest letter to the largest letter
    count_array = [0] * (max_value - min_value+1)
    for freq in wordlist:
        count_array[ord(freq[col])-min_value]+=1

    #Position indicates the position of the words that contains the letter in that index.
    position = [0] * (max_value-min_value+1)
    position[0] = 1
    for pos in range(1,len(count_array)):
        position[pos] = position[pos-1] + count_array[pos-1]

    #sortedWords contains the sorted words based on the value of the letter in that column.
    sortedWords = [None] * len(wordlist)
    for i in range(len(wordlist)):
        sortedWords[((position[ord(wordlist[i][col])-min_value])-1)] = wordlist[i]
        position[ord(wordlist[i][col]) - min_value] +=1
    wordlist = sortedWords
    return sortedWords



def counting_sort(word):
    '''
    Written by Lee Zhen Xuan 31860532
    This function sort a word alphebetically

    Input:
        word: A word
    Return:
        sortedWord: A word that has been sorted by letters alphabetically

    '''
    # This part of the function sorts finds the largest letter in the words
    max_value = ord(word[0])
    for i in word:
        if ord(i) > max_value:
            max_value = ord(i)

    # This part of the function sorts finds the smallest letter in the words
    min_value = ord(word[0])
    for j in word:
        if ord(j) < min_value:
            min_value = ord(j)

    # Count array contains the frequency of each of the letters
    count_array = [0] * (max_value - min_value+1)
    for freq in word:
        count_array[ord(freq)-min_value]+=1

    # Position indicates the position of the letters alphabetically
    position = [0] * (max_value-min_value+1)
    position[0] = 1
    for pos in range(1,len(count_array)):
        position[pos] = position[pos-1] + count_array[pos-1]

    #sortedWord return the words that have been sorted alphabetically
    sortedWord = [None] * len(word)
    for i in range(len(word)):
        sortedWord[((position[ord(word[i]) - min_value]) - 1)] = word[i]

        position[ord(word[i]) - min_value] += 1
    return sortedWord



def localMaxima(M):
    '''
    Written by Lee Zhen Xuan 31860532
    This function finds the local minimum based on the concept of divide and conquer

    Precondition: The matrix has a size of n by n where n indicates the length of both row and column
    Postcondition: The local maximum is found where all the neighbouring numbers are smaller than the number found

    Input:
        M: An n-by-n grid of distinct integers/n-by-n matrix
    Return:
        The coordinates of a local maximum, where the neighbouring numbers are smaller than the number

    Time complexity:
        Best case complexity = Worst case complexity: O(N) where N is the number of rows.
    Space complexity:
        Input: O(N) where N is the number of rows in the matrix
        Aux: O(1). This algorithm is an in place algorithm.

    '''
    topRowIndex = 0
    btmRowIndex = len(M)-1
    topColIndex = 0
    btmColIndex = len(M)-1


    while(topRowIndex<= btmRowIndex) and (topColIndex<=btmColIndex):
        midRowIndex = (topRowIndex+btmRowIndex)//2
        rowindex = 0
        colindex = 0
        midColIndex = (topColIndex+btmColIndex)//2
        maxRowValue = M[midRowIndex][0]
        maxColValue = M[0][midColIndex]

        #Finds the maximum value in a row
        for i in range(topColIndex,btmColIndex+1):
            if maxRowValue < M[midRowIndex][i]:
                maxRowValue = M[midRowIndex][i]
                colindex = i

        #Finds the maximum value in a column
        for j in range(topRowIndex,btmRowIndex+1):
            if maxColValue < M[j][midColIndex]:
                maxColValue = M[j][midColIndex]
                rowindex = j


        #If the top value is more than the maxRowValue, update bottom row index to mid row index -1
        if M[(midRowIndex-1)][colindex] > maxRowValue:
            btmRowIndex = midRowIndex -1
        # If the bottom value is more than the maxRowValue, update top row index to mid row index -1
        elif M[(midRowIndex+1)%len(M)][colindex] > maxRowValue:
            topRowIndex = midRowIndex+1
        #If maximum value is found, return the coordinates
        elif M[midRowIndex-1][colindex] < maxRowValue and M[midRowIndex+1][colindex] < maxRowValue and M[midRowIndex][colindex-1] < maxRowValue and M[midRowIndex][(colindex+1)%len(M)] < maxRowValue:
            return [midRowIndex,colindex]

        # If the left value is more than the maxRowValue, update right col index to mid col index -1
        if M[rowindex][midColIndex-1] > maxColValue:
            btmColIndex = midColIndex-1
        # If the right value is more than the maxColValue, update left rol index to mid col index +1
        elif M[rowindex][(midColIndex+1)%len(M)] > maxColValue:
            topColIndex = midColIndex+1
        # If maximum value is found, return the coordinates
        elif M[rowindex][midColIndex-1] < maxColValue and M[rowindex][midColIndex+1] < maxColValue and M[(rowindex+1)%len(M)][midColIndex] < maxColValue and M[rowindex-1][midColIndex] < maxColValue:
            return [rowindex,midColIndex]






if __name__ == "__main__":
    wordlist = ['limes', 'spare', 'store', 'loser', 'aster', 'pares', 'taser', 'pears', 'stare', 'spear', 'parse','reaps', 'rates', 'tears', 'losts']
    word= "pares"
    marker = [0, 0, 0, 0, 1]
    trainer(wordlist,word,marker)

    M = [[1, 3, 6, 10, 15, 21, 28, 164, 201, 203, 206, 210, 215, 221, 228],
         [2, 5, 9, 14, 20, 27, 34, 163, 202, 205, 209, 214, 220, 227, 234],
         [4, 8, 13, 19, 26, 33, 39, 162, 204, 208, 213, 219, 226, 233, 239],
         [7, 12, 18, 25, 32, 38, 43, 161, 207, 212, 218, 225, 232, 238, 290],
         [11, 17, 24, 31, 37, 42, 46, 160, 211, 217, 224, 231, 909, 908, 907],
         [16, 23, 30, 36, 41, 45, 48, 159, 216, 223, 230, 260, 906, 904, 902],
         [22, 29, 35, 40, 44, 47, 49, 158, 222, 229, 235, 340, 305, 903, 901],
         [51, 52, 53, 54, 55, 56, 57, 157, 506, 505, 504, 503, 502, 501, 650],
         [101, 102, 127, 128, 129, 130, 149, 156, 601, 302, 327, 328, 629, 630, 649],
         [103, 104, 125, 126, 131, 132, 148, 155, 603, 604, 625, 626, 631, 632, 648],
         [105, 106, 123, 124, 133, 134, 147, 154, 605, 606, 623, 624, 633, 634, 647],
         [107, 108, 121, 122, 135, 136, 146, 153, 607, 608, 621, 622, 635, 636, 646],
         [109, 110, 119, 120, 137, 138, 145, 152, 609, 610, 619, 620, 637, 638, 645],
         [111, 112, 117, 118, 139, 140, 144, 151, 611, 612, 617, 618, 639, 640, 644],
         [113, 114, 115, 116, 141, 142, 143, 150, 613, 614, 615, 616, 641, 642, 643]]
    localMaxima(M)




