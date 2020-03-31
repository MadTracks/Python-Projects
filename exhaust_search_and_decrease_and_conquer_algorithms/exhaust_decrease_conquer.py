#CSE 321 Introduction to Algorithm Design - Fall 2019
#Berke Suslu
#161044076


#example implementation of question 1

def black_and_white_boxes(box,n): 
    if n>0:
        temp=box[len(box)-n]
        box[len(box)-n]=box[n-1]
        box[n-1]=temp
        black_and_white_boxes(box,n-2)

#example driver function for question 1

testarray = ["B","B","B","B","B","W","W","W","W","W"]
black_and_white_boxes(testarray,5)
print("Question1:",testarray)

#example implementation of question 2
def find_fake_coin(coins):
    if len(coins) < 3:
        print("We need at least 3 coins in order to find fake coin.")
        return -1
    else:
        temp = find_3_coin(coins[0],coins[1],coins[2])
        if temp == False:
            if len(coins)-3 >= 3:
                return find_fake_coin(coins[3:len(coins)])
            else:
                return find_fake_coin(coins[len(coins)-3:len(coins)])
        else:
            return temp

def find_3_coin(c1,c2,c3):
    if c1 == c2:
        if c2 == c3:
            return False
        else:
            return c3
    elif c2 == c3:
        return c1
    else:
        return c2

#example driver function for question 2

testarray = [1,1,1,1,1,1,1,1,1,2]
fake = find_fake_coin(testarray)
print("Question2:",fake)

#implementation of question 3
def partition(array,l,r): 
    i=l-1
    p=array[r]  
    for j in range(l,r): 
        if   array[j] <= p:
            i=i+1 
            temp=array[i]
            array[i]=array[j]
            array[j]=temp  
    temp=array[i+1]
    array[i+1]=array[r]
    array[r]=temp 
    return i+1

def quickSort(array,l,r): 
    if l < r:  
        pivot = partition(array,l,r) 
        quickSort(array, l, pivot-1) 
        quickSort(array, pivot+1, r) 

def insertionSort(array): 
    for i in range(1, len(array)): 
        largest = array[i]
        j=i-1
        while j >= 0 and largest < array[j]: 
                array[j+1]=array[j] 
                j-=1
        array[j+1]=largest 

#driver function for question 3

quickarray = [423,214,112,41,6,1,19,2435,14,174,12,121]
insertionarray = [231,12,1643,2645,976,435,963,45,3,754]
print("Question 3:") 
print(quickarray)
quickSort(quickarray,0,len(quickarray)-1) 
print("Sorted array by using quickSort =",quickarray)
print(insertionarray)
insertionSort(insertionarray)
print("Sorted array by using insertionSort =",insertionarray)

#implementation of question 4


#using same partition fuction
def quickSelect(array,l,r,k):
    if (k > 0 and k <= r-l+1): 
        s = partition(array,l,r) 
        if (s-l == k-1): 
            return array[s] 
        if (s-l > k-1):
            return quickSelect(array,l,s-1,k)  
        return quickSelect(array,s+1,r,k-s+l-1)

#driver function for question 4

print("Question 4:")
quickselarray = [423,214,112,41,6,1,19,2435,14,174,12,121]
median = quickSelect(quickselarray,0,len(quickselarray)-1,(len(quickselarray)//2)+1)
print("Median:",median)
quickSort(quickselarray,0,len(quickselarray)-1)
print(quickselarray)
