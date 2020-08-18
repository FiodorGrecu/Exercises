def hops_away(adjacency_list, node, num_hops):
    if not node in adjacency_list.keys():
        return []
    elif  num_hops == 0:
        return [node]
    else:
        hops_away_neighbours = []
        for neighbor in adjacency_list[node]:
            hops_away_neighbours.extend(hops_away(adjacency_list, neighbor, num_hops - 1))
        hops_away_neighbours_unic = []
        for n in hops_away_neighbours:
            if not n in hops_away_neighbours_unic:
                hops_away_neighbours_unic.append(n)
            return hops_away_neighbours_unic

adj_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,3,5],
    4: [],
    5: [6],
    6: [3,5]
}
print(hops_away(adj_list, 0, 1))