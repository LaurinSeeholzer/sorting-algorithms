#made by Laurin Seeholzer in august 2021

#insertion sort algorithm
#O(n log n)
def insertion_sort(unsorted_list):
    sorted_list = []
    while len(unsorted_list) > 0:
        smallest = unsorted_list[0]
        smallest_index  = 0
        for index, elem in enumerate(unsorted_list):
            if elem < smallest:
                smallest = elem
                smallest_index = index
        unsorted_list.pop(smallest_index)
        sorted_list.append(smallest)
    return sorted_list
