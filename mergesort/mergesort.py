def merge(lefthalf, righthalf):
    i = j = 0
    result = []
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            result.append(lefthalf[i])
            i += 1
        else:
            result.append(righthalf[j])
            j += 1
    while i < len(lefthalf):
        result.append(lefthalf[i])
        i += 1
    while j < len(righthalf):
        result.append(righthalf[j])
        j += 1
    return result


def mergesort(mergelist):
    if len(mergelist)==1:
        return mergelist
    mid=len(mergelist) // 2
    lefthalf=mergelist[:mid]
    righthalf=mergelist[mid:]
    return merge(lefthalf,righthalf)





