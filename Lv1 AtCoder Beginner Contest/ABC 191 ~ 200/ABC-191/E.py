import math,heapq
def dijkstra(nodes):
    start_node = nodes[0]
    routes_from_start = {n: math.inf for n in nodes}
    routes_from_start[start_node] = 0
    minHeap = []
    heappush(minHeap, (0, start_node))
    path = collections.defaultdict(Node)
    while minHeap:
        (cost, current_node) = heappop(minHeap)
        if cost > routes_from_start[current_node]:continue
        for node in current_node.routes:
            price_info = current_node.routes[node]
            if routes_from_start[node] > price_info + routes_from_start[current_node]:
                routes_from_start[node] = price_info + routes_from_start[current_node]
                path[node.id] = current_node.id
                heappush(minHeap, (price_info + routes_from_start[current_node], node))
    current_node = nodes[-1].id
    path_array = []
    while current_node:
        path_array.append(current_node)
        if current_node not in path:
            break
        current_node = path[current_node]
    return routes_from_start[nodes[-1]], path_array[::-1]

N,M=map(int,input().split())
d=[list(map(int,input().split()))for i in range(M)]

print(dijkstra([0,1,2,3,4]))