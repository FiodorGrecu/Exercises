def most_neighbours(adjacency_list):
    max_len = -1
    max_key = -1
    for keyNode, edge_lst in adjacency_list.items():
        num_neighbors = len(edge_lst)
        if num_neighbors > max_len:
            max_key = keyNode
            max_len = num_neighbors
        elif num_neighbors == max_len and keyNode < max_key:
            max_key = keyNode
    return max_key
