
def find_kth(array1,array2,m,n,k,array_end1,array_end2):
    
    if array_end1 == m:
        return array2[array_end2+k-1]
    
    if array_end2 == n:
        return array1[array_end1+k-1]
    
    if k == 0 | k > (m-array_end1)+(n-array_end2):
        return -1
    if k == 1:
        if array1[array_end1] < array2[array_end2]:
            return array1[array_end1]
        else:
            return array2[array_end2]
    curr = k//2
    if curr-1 >= m-array_end1:
        if array1[m-1] < array2[array_end2+curr-1]:
            return array2[array_end2+(k-(m-array_end1)-1)]
        else:
            return find_kth(array1,array2,m,n,k-curr,array_end1,array_end2+curr)
    
    if curr-1 >= n-array_end2:
        if array2[n-1]<array1[array_end1+curr-1]:
            return array1[array_end1+(k-(n-array_end2)-1)]
        else:
            return find_kth(array1,array2,m,n,k-curr,array_end1+curr,array_end2)
    else:
        if array1[curr+array_end1-1] < array2[curr+array_end2-1]:
            return find_kth(array1,array2,m,n,k-curr,array_end1+curr,array_end2)
        else:
            return find_kth(array1,array2,m,n,k-curr,array_end1,array_end2+curr)

def test_question2():
    arr1 = [5,11,41,76]
    arr2 = [8,9,10,15]

    k=5
    m=find_kth(arr1,arr2,len(arr1),len(arr2),k,0,0)
    print("Question 2")
    print("The k =",k,"element is",m)


def max_between_sum(array,l,m,h):
    s=0
    left_sum=float('-inf')
    for i in range(m,l-1,-1):
        s = s+array[i]
        if s>left_sum:
            left_sum = s
    
    s=0
    right_sum=float('-inf')
    for i in range(m+1,h+1):
        s=s+array[i]
        if s>right_sum:
            right_sum=s
    
    return left_sum+right_sum

def max_subarray_sum(array,l,h):
    if(l==h):
        return array[l]
    m=(l+h)//2

    return max(max_subarray_sum(array,l,m),max_subarray_sum(array,m+1,h),max_between_sum(array,l,m,h))

def test_question3():
    arr = [5,-6,6,7,-6,7,-4,3]

    max_sum = max_subarray_sum(arr,0,len(arr)-1)
    print("Question 3")
    print("The sum of contiguous subset is",max_sum)

def color_graph(G,color,pos,c,v):
    if color[pos] != -1 & color[pos] != c:
        return False
    
    color[pos] = c
    a = True
    for i in range(0,v):
        if G[pos][i]:
            if color[i] ==-1:
                a = a & color_graph(G,color,i,1-c,v)
            if color[i] !=-1 & color[i] != 1-c:
                return False
        
        if not a:
            return False
    
    return True

def is_bipartite(G,v):

    color = [-1] * v
    pos = 0
    return color_graph(G,color,pos,1,v)

def test_question4():
    G = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]

    bipa = is_bipartite(G,len(G[0]))
    print("Question 4")
    if(bipa):
        print("The graph is bipartite")
    else:
        print("The graph is not bipartite")


def evaluate_gain(cost,price,startindex):
    if len(cost)<1:
        return [startindex,False]
    if len(cost) == 1:
        gain = price[0]-cost[0]
        return [startindex,gain]
    if len(cost)>1:
        first_half=evaluate_gain(cost[0:len(cost)//2],price[0:len(cost)//2],startindex)
        last_half=evaluate_gain(cost[len(cost)//2:len(cost)],price[len(cost)//2:len(cost)],startindex+len(cost)//2)
        gain = max(first_half[1],last_half[1])
        if gain == first_half[1]:
            return first_half
        else:
            return last_half

def max_gain(c,p):
    max_g = evaluate_gain(c[0:len(c)-1],p[1:len(p)],0)
    if max_g[1] < 0:
        print("There is no day to make money.")
    else:
        print("The best day to buy is the",max_g[0],"day and the gain is",max_g[1])
    return max_g
def test_question5():
    C=[5,11,2,21,5,7,8,12,13,False]
    P=[False,7,9,5,21,7,13,10,14,20]
    print("Question 5")
    max_gain(C,P)

test_question2()
test_question3()
test_question4()
test_question5()