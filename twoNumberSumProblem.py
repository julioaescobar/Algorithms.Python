
def solution1(numberList, target):
    try:
        for numA in range(0,len(numberList)):
            for numB in range(1,len(numberList)):
                if(numberList[numA] + numberList[numB] == target):
                    return [numA,numB]
    except Exception as exception:
        print(exception)

def solution2(numberList, target):
    try:
        sorted(numberList)
        left = 0
        right = len(numberList) - 1

        while(left < right):
            if(numberList[left] + numberList[right] == target):
                return [left,right]
            elif(numberList[left] + numberList[right] < target):
                left+=1
            else:
                right-=1

    except Exception as exception:
        print(exception)  

def solution3(numberList, target):
    try:
        hashMap = {}
        for index,num in enumerate(numberList):
            complement = target - num
            if(complement in hashMap):
                return [hashMap[complement], index]
            else:
                hashMap[num] = index
    except Exception as exception:
        print(exception)        

numberList = [2, 7, 11, 15]
target = 18

print(solution1(numberList,target))

print(solution2(numberList,target))

print(solution3(numberList,target))