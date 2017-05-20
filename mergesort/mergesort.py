def merge(left,right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result


def mergesort(x):
    
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        left = mergesort(x[:middle])
        right = mergesort(x[middle:])
        return merge(left,right)



def main(mergelist):
    x=mergesort(mergelist)
    print(x)
    

main([21,12,51,21,643,123,75,123,754,2132,54,554,548,5485])



