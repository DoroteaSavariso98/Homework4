def binary_search(List_val, search_val, start_index = None, stop_index = None):
    if start_index is None:
        start_index = 0
    else:
        start_index
    if stop_index is None:
        stop_index = len(List_val)-1
    else:
        stop_index
    if stop_index < start_index:
        return -1
    else:
        middle_index = int((start_index + stop_index)/2)

        if List_val[middle_index] > search_val:
            return binary_search(List_val, search_val, start_index, middle_index - 1)
        elif List_val[middle_index] < search_val:
            return binary_search(List_val, search_val, middle_index + 1, stop_index)
        else:
            return middle_index


if __name__ == '__main__':

    with open('rosalind_bins.txt') as input_data:
        n, m = [int(input_data.readline().strip()) for repeat in range(2)]
        list_1 = list(map(int, input_data.readline().strip().split()))
        list_2 = list(map(int, input_data.readline().strip().split()))
    indices = [binary_search(list_1, k) for k in list_2]

    indices = [str(index + 1) if index >= 0 else str(-1) for index in indices]

    print(' '.join(indices))
