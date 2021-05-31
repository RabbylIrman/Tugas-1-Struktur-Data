def has_distinct_elements(data):
    r = set(data)
    if len(data) != len(r):
        return False
    else:
        return True

def has_distinct_elements_1(data):
    r=[]
    for s in data:
        if s in r:
            return False
        else:
            r.append(s)
    return True

print(has_distinct_elements([1,2,3,3,4,5,6,7,8]))
print(has_distinct_elements_1([1,2,3,4,5,6,7,8]))
