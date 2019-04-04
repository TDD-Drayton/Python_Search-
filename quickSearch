from random import randrange, shuffle


def quick_sort(lst, start, end):
   # This portion of list has been sorted
   if start >= end:
       return

   # Select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = lst[pivot_idx]

   # Swap random element with last element in sub-lists
    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]

   # Tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

   for i in range(start, end):
       # We found an element out of place
       if lst[i] < pivot_element:
           # Swap element to the right-most portion of lesser elements
            lst[i], lst[less_than_pointer] = lst[less_than_pointer], lst[i]
           # Tally that we have one more lesser element
            less_than_pointer += 1

   # Move pivot element to the right-most portion of lesser elements
    lst[end], lst[less_than_pointer] = lst[less_than_pointer], lst[end]

   # Recursively sort left and right sub-lists
    quick_sort(lst, start, less_than_pointer - 1)
    quick_sort(lst, less_than_pointer + 1, end)


lst = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(lst)

quick_sort(lst, 0, len(lst) - 1)

print(lst)
# Output [1, 2, 3, 4, 5, 6, 7, 8]
