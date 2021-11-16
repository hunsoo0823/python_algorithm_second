# 원소의 갯수 N, 찾는 수 x
from binaty_search.binary_search import binary_search


N, x = map(int, input().split())

sorted_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    