import itertools
import collections
def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))
        
    for n in course:
        hash = dict()
        comb = list()
        for order in orders: comb += list(map(''.join, itertools.combinations(order, n)))
        hash = collections.Counter(comb)
        answer += [item[0] for item in hash.most_common() if item[1]==hash.most_common(1)[0][1] and item[1]>1]
    return sorted(answer)