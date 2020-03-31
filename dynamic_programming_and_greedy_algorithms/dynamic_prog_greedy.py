
def minimum_cost(citytable,cost):
    dp_table= [[0] * len(citytable[0]),[0] * len(citytable[1])]
    dp_table[0][0] = citytable[0][0]
    dp_table[1][0] = citytable[1][0]
    for i in range(1,len(citytable[0])):
        dp_table[0][i]=min(dp_table[0][i-1]+citytable[0][i],dp_table[1][i-1]+citytable[1][i]+cost)
        dp_table[1][i]=min(dp_table[1][i-1]+citytable[1][i],dp_table[0][i-1]+citytable[0][i]+cost)
    return min(dp_table[0][len(dp_table[0])-1],dp_table[1][len(dp_table[1])-1])

def driver_question1():
    print("Question 1 Test Cases:")
    citytable=[[1,3,20,30],[50,20,2,4]]
    citytable2=[[2,54,3,53,30,2],[2,56,124,1234,1,24]]
    print(minimum_cost(citytable,10))
    print(minimum_cost(citytable2,10))

def optimal_list(sessions):
    sessions.sort(key=lambda x:x[1])  #sorts the list according to finishing time
    optimal_list=[sessions[0]]
    optimal_last_finish_time = sessions[0][1]
    for i in range(1,len(sessions)):
        if sessions[i][0] >= optimal_last_finish_time:
            optimal_list.append(sessions[i])
            optimal_last_finish_time = sessions[i][1]
    return optimal_list

def driver_question2():
    print("Question 2 Test Cases:")
    sessions = [[6,8],[4,6],[5,7],[11,15],[10,17],[12,14],[18,20],[19,22]] #first element is starting time, second element is finishing time.
    opt=optimal_list(sessions)
    print(opt)
    print(len(opt))

def calculate_score(s1,s2,hit,miss,gap):
    dp_table=[[0]*(len(s1)+1)]*(len(s2)+1)
    dp_table[0][0]=0

    for i in range(1,len(s1)+1):
        dp_table[i][0]=-i*gap
    for j in range(1,len(s2)+1):
        dp_table[0][j]=-i*gap

    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            dp_table[i][j]=max(dp_table[i-1][j-1]+score(s1[i],s2[j],hit,miss),dp_table[i-1][j]-gap,dp_table[i][j-1]-gap)

    return dp_table[len(s1)][len(s2)]

def score(x,y,h,m):
    if(x==y):
        return h
    else:
        return m

def driver_question4():
    print("Question 4 Test Cases:")
    str1="AGGACT"
    str2="AGGCAC"

    hitscore=2
    misspenalty=-2
    gappenalty=-1
    print(calculate_score(str1,str2,hitscore,misspenalty,gappenalty))

def min_operation(array):

    operation=0
    while len(array)>1:
        firstsmall=float('inf')
        secondsmall=float('inf')
        for i in range(0,len(array)):
            if array[i]<=firstsmall:
                secondsmall=firstsmall
                firstsmall=array[i]
            elif array[i]<secondsmall and array[i]>firstsmall:
                secondsmall=array[i]

        value=firstsmall+secondsmall
        array.remove(firstsmall)
        array.remove(secondsmall)
        array.append(value)
        operation=operation+value
        
    print("Result is",array)
    return operation

def driver_question5():
    print("Question 5 Test Cases:")
    array=[20,30,10,5]
    print("Total operation is",min_operation(array))

driver_question1()
driver_question2()
driver_question4()
driver_question5()