def solution(n):
    m = str(n)
    val = len(m)//2
    first = 0
    second =0 
    for i in range(val):
        first += int(m[i])
        second += int(m[val+i])
    return True if first==second else False
