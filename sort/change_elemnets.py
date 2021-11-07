# input n, k
n, k = map(int, input().split())
a = list(map(int, input().split())) # input array a
b = list(map(int, input().split())) # input array b

a.sort() # ascending sort
b.sort(reverse=True) # decending sort

for i in range(k):
    if b[i] <= a[i]:
        break
    else:
        a[i], b[i] = b[i], a[i]

print(sum(a))