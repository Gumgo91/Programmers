import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    n = 0
    while True:
        try:
            first = heapq.heappop(scoville)
            if first >= K:
                break
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
            n += 1
        except:
            n = -1
            break
    return n