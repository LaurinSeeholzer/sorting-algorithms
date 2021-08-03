#made by Laurin Seeholzer in august 2021

#bubble sort algorithm
#O(n^2)
def bubble_sort(unsorted_list):
    for e in range(len(unsorted_list)):
        for i in range(0, len(unsorted_list) - 1 - e):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list
