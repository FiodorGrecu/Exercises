def frequency_array(lst):
    max_elem = -1
    for i in lst:
        if i > max_elem:
            max_elem = i
    frequency_list = [0 for i in range(max_elem+1)] 

    for i in range(len(lst)):
        frequency_list[lst[i]] += 1
    return frequency_list

def frequency_array_cumulative(lst):
    freq_lst = frequency_array(lst)
    freq_len = len(freq_lst)
    freq_cum_lst = [0 for i in range(freq_len)]
    for i in range(freq_len):
        if i == 0:
            freq_cum_lst[i] = freq_lst[i]
        else:
            freq_cum_lst[i] = freq_lst[i] + freq_cum_lst[i-1]
    return freq_cum_lst


# lst = [1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6]

print(frequency_array_cumulative([1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6]))

