def odd_product_pair(data):
    data = set(data)
    for x in data:
        for y in data:
            if x == y :
                continue
        if x*y % 2 == 1:
            return True
    return False

print(odd_product_pair([2,3,6,8,9,10]))
