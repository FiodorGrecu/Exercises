def count_islands(adjacency_list):
    dict_count_edges = dict.fromkeys(adjacency_list.keys(), 0)
    for adjkeyNode, edge_lst in adjacency_list.items():
        for keyNode in dict_count_edges.keys():
            if not adjkeyNode == keyNode:
                if keyNode in edge_lst:
                    dict_count_edges[keyNode] +=1
    numIslands = 0
    for edgeCount in dict_count_edges.values():
        if edgeCount == 0:
            numIslands +=1
    return numIslands

adjacency_list = {
    0: [1,3,5],   
    1: [0,1,3,6],
    2: [],
    3: [0,3],
    4: [],
    5: [6],
    6: [3,5]
}

count_islands(adjacency_list)