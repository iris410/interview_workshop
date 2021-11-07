#log(n)
def closest(list1, num):
    low = 0
    high = len(list1) - 1
    if num > list1[high] or num < list1[low]:
        return -1

    answer = list1[high]
    while (low <= high):
        mid = (low + high) // 2
        if num <= list1[mid]:
            high = mid - 1
            answer = list1[mid]
        else:
            low = mid + 1
    return answer

#O(upper_bound * a * log(n))
def find_max_of_min(list1:list,a:int):#linear search
    upper_bound = list1[-1]
    answer = -1
    for i in range(1,upper_bound+1):
        current = list1[0]
        found = True
        for j in range(a-1):
            current = closest(list1,current+i)
            if current == -1:
                found = False
                break

        if found == False:
            break
        answer = i

    return answer

#log(upper_bound) * a * log(n)
def find_max_of_min2(list1:list,a:int):#lbinary search
    upper_bound = list1[-1]
    lower_bound = list1[0]
    answer = -1
    while(lower_bound <= upper_bound):
        mid = (lower_bound + upper_bound)//2
        current = list1[0]
        found = True
        for j in range(a-1):
            current = closest(list1,current+mid)
            if current == -1:
                found = False
                break

        if found == False:
            upper_bound = mid - 1
        else:
            answer = mid
            lower_bound = mid + 1

    return answer



print(closest([1, 3, 5, 7, 9], 0))
print(find_max_of_min2([1,3,5,7,9],6))
