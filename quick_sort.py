#made by Laurin Seeholzer in august 2021

#quick sort / Radix MSD algorithm
#O(l*n)
def radix_msd_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    base = max(unsorted_list).bit_length() - 1
    return sort(unsorted_list, 0, len(unsorted_list) - 1, base)

def sort(l, i, j, base):
    m, n = i, j
    while m <= n:
        if unsorted_list[m] >> base & 1 == 0:
            m += 1
            continue
        else:
            if unsorted_list[n] >> base & 1 == 0:
                unsorted_list[n], unsorted_list[m] = unsorted_list[m], unsorted_list[n]
                m += 1
            n -= 1
    if base > 0 and i < j:
        sort(l, i, m-1, base-1)
        sort(l, m, j, base-1)
    return unsorted_list
