# for searching perticular elimant in a list then we will go through the linear search

#linear search
#=======================================================
# pos = -1

# def search(list,n):

#     i = 0

#     while i < len(list):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i = i+1
#     return False

# list = [2, 4, 3, 7, 5, 8, 9, 10]
# n = 10
# if search(list,n):
#     print("found at ",pos+1)
# else:
#     print("Not found")

#=================================================


#Binary search
# pos = -1
# def search(list,n):

#     l = 0
#     up = len(list)-1

#     while l <= up:
#         mid = (l+up) // 2
#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid+1
#             else:
#                 up = mid-1
#     return False

# list = [2, 4, 7, 5, 8, 9, 10]
# n = 9
# if search(list,n):
#     print("found at ",pos+1)
# else:
#     print("Not found")

#=============================================================
# bubble sorting
# def sort(list):
#   for i in range(len(list) - 1, 0, -1):
#     for j in range(i):
#       if list[j] > list[j + 1]:
#         list[j], list[j + 1] = list[j + 1], list[j]  # Swap using tuple unpacking

# list = [30,89,2, 4, 3, 7, 5, 8, 9, 10]
# sort(list)
# print(list)
#===============================================================

# linear search will take more anfd more time to search a big list so for that we will go for the bynary search 
# Binary search

# all values in sorted form

#==========================================================================
# selection sort

def sort(list):

    for i in range(len(list)):
        minpos = i
        for j in range(i+1, len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        # print(list)

list = [7,3,5,3,2,7,4,45,2,54,89]
sort(list)

print(list)

#============================================================================
