

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        answer = pascal(n-1, k-1) + pascal(n-1, k)
        return answer

n = 4
k = 2

print(pascal(n, k))