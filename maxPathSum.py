#?/usr/bin/env python

#Prob 18: Maximum path sum 1

def makeTriangle(numbers):
    nums = []
    for i in range(0,15):
        nums.append([])
    
    row=0
    appended=0
    appendedThisRow = 0
    pointer = 1
    
    while pointer < len(numbers):
        x = numbers[pointer] + numbers[pointer + 1]
        nums[row].append(x)
        pointer += 3
        appendedThisRow +=1
        if(appendedThisRow - row == 1):
            row+=1
            appendedThisRow = 0
    return nums

def pointers_to_each_node(graph):
    numOfNodes = (15*16)/2
    pointerTo = []
    for i in range(0, numOfNodes):
        pointerTo.append([])
    
    pointerTo[0] = 0
    pointerTo[1] = 0
    pointerTo[2] = 0
    
    CurrRow = 2
    workingOnNum = 3
    
    while workingOnNum <= 121:
        # print CurrRow
        # print '\n'
        # print len(graph[CurrRow])
        if CurrRow == 15:
            break
        for i in range(0, len(graph[CurrRow])):
            
            #print 'i=%s'%i 
            #print"length of current row =", len(graph[CurrRow])
            if(i == 0):
                #print "Start of row<------"
                pointerTo[workingOnNum] = workingOnNum - CurrRow
                #print "pointerTo[", workingOnNum, "]=", pointerTo[workingOnNum]
                workingOnNum+=1
                
            elif(i == len(graph[CurrRow]) - 1): 
                #print "end<-----"
                pointerTo[workingOnNum] = workingOnNum - CurrRow - 1
                #print workingOnNum
                #print "pointerTo[", workingOnNum, "]=", pointerTo[workingOnNum]
                #print "pointerTo[", graph[CurrRow][i], "]=", graph[CurrRow-1][i-1]
                workingOnNum+=1
                CurrRow +=1
                
            else:
                #for j in range(0, CurrRow -1):
                    #print "working on:", workingOnNum
                pointerTo[workingOnNum] = [workingOnNum - CurrRow -1, workingOnNum - CurrRow ]
                #print "pointerTo[", workingOnNum, "]=", pointerTo[workingOnNum]
                    #print "pointerTo[", graph[CurrRow][i], "]=", graph[CurrRow-1][i-1] + " pointerTo[", graph[CurrRow][i], "]=", graph[CurrRow-1][i]
                workingOnNum +=1
                #i+= CurrRow -2
                    
        #print"Finished row:", CurrRow
        
    
    return pointerTo

def maxSumToEachNode(tri, x):
    maxSum = []
    for i in range(0,120):
        maxSum.append(0)
    
    maxSum[0] = int(tri[0][0])
    maxSum[1] = int(maxSum[0]) + int(tri[1][0])
    
    index = 2
    row = 1
    position = 1
    
    while index <= 119:
        if(index == 119):
            maxSum[index] = int(maxSum[x[index]]) + int(tri[row][len(tri[row]) - 1])
            return maxSum
        if(isinstance(x[index], int) and isinstance(x[index+1], int) == False):
            """
            beginning of row
            """
            maxSum[index] = int(maxSum[x[index]]) + int(tri[row][0])
            index +=1
            position +=1
            #print"maxSum[", index -1, "]=", maxSum[index -1]
        
        elif(isinstance(x[index], int) and isinstance(x[index+1], int) == True):
            """
            end of row
            """
            maxSum[index] = int(maxSum[x[index]]) + int(tri[row][len(tri[row]) - 1])
            index +=1
            row +=1
            position = 0
            #print"maxSum[", index -1, "]=", maxSum[index -1]
        
        else:
            first = x[index][0]
            second = x[index][1]
            maxSum[index] = max(maxSum[first], maxSum[second]) + int(tri[row][position])
            index +=1
            position +=1
            #print"maxSum[", index -1, "]=", maxSum[index -1]

triangle =makeTriangle("""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".replace("\n", " "))

for i in range(0,15):
       print triangle[i]
    
    
x = pointers_to_each_node(triangle)
print max(maxSumToEachNode(triangle,x))

