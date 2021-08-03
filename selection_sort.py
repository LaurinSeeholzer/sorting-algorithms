#made by Laurin Seeholzer in august 2021

#selection sort algorithm
#O(n^2)
def selection_sort(unsorted_list): 
    for e in range(len(unsorted_list)):
        min = e
        for i in range(e+1, len(unsorted_list)):
            if unsorted_list[min] > unsorted_list[i]:
                min = i      
        unsorted_list[e], unsorted_list[min] = unsorted_list[min], unsorted_list[e]
    return unsorted_list
