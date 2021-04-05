import heapq
def solution(N, road, K):
    graph = [[] for i in range(N+1)]
    distance = [float("inf")] * (N+1)
    for r in road:
        graph[r[0]].append((r[2], r[1]))
        graph[r[1]].append((r[2], r[0]))
    
    q = []
    start = 1
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return len(list(filter(lambda x:x<=K, distance[1:])))