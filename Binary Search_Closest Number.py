def closest(lst, x):
    if (x <= lst[0]):
        return lst[0]
    if (x >= lst[len(lst) - 1]):
        return lst[len(lst) - 1]

    left = 0
    right = len(lst)-1
    mid = 0

    while left<=right:
        mid = (left+right)//2

        if lst[mid]<x:
            left = mid+1
        elif lst[mid]>x:
            right = mid-1
        else:
            return mid

    if abs(x-lst[left]) > abs(x-lst[right]):
        return lst[right]
    elif abs(x-lst[right]) > abs(x-lst[left]) :
        return lst[left]
    else:
        return lst[right], lst[left]

lst = [2, 3, 4, 5, 5, 10, 40]
print(closest(lst, 6))
