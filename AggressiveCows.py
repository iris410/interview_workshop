# Input:
# 5 3
# 1 2 4 8 9
#
# Output:
# 3
#
# => 1 4 9
#
# Answer required configuration =>
# 4-1 = 3
# 9-4 = 5
# Min(3,5) => 3
result =[]
#permutation n^a  (a-1)
def get_sublists(list1: list, a: int, current: int,chain:list):#backTracking
    if a == 0:
        result.append(chain)
        return
    for i in range(current+1,len(list1)-a+1):
        new_chain = chain + [list1[i]]
        get_sublists(list1,a-1,i,new_chain)
    return

#a * n^a
def find_max_of_min(list1:list,a:int):
    global result
    result = []
    temp = []
    get_sublists(list1,a,-1,[])
    print(result)
    for item in result:
        min_distance = float('inf')
        for i in range(a-1):
            distance = item[i+1] - item[i]
            min_distance = min(min_distance,distance)
        temp.append(min_distance)
    return max(temp)












list_test1 = [1,3,5,9]
print(find_max_of_min(list_test1,3))






