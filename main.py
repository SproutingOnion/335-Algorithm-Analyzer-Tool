#Main file for UI interface and calling sorting algorithms
from typing import List, Dict, Tuple
import random
import time
from algorithms.radix_demo import *
from algorithms.HeapSort_demo import *
from algorithms.mergesort_demo import *
from algorithms.QuickSelectSort_Demo import *
from algorithms.QuickSort_demo import *
from algorithms.bubblesort_demo import *
from algorithms.BucketSort_Demo import *
from algorithms.countingsort_demo import *
from algorithms.insertsort_demo import *


#Demo to test out for calling functions from files and using random int generators
#To test with other algorithsm comment out other __name__ == __main__  from respective files
if __name__ == "__main__":
   random_index_size = random.randint(1,50) #Sets index ranging from 1 - 50

   #Filling the list with numbers from 1 - 200. May be increased if need to
   random_filled_list = [random.randint(1, 200) for i in range(random_index_size)] #Random int filled list
   random_filled_float_list = [random.random() for i in range(random_index_size)] #Random float filled list
   
   base = 10 #Printing purposes but it shows base number for radix sort. May be user inputted if necessary
   
   #Mergre sort time counter in main due to recursion in algorithm
   start = time.perf_counter()
   sorted = merge_sort(random_filled_list)
   end = time.perf_counter()
   print(f"[Mergre] sort in {end-start:.6f} sec")
   print(sorted)


   print(radix_sort_lsd_nonneg(random_filled_list,10))

   print(bubble_sort(random_filled_list))

   print(bucket_sort(random_filled_float_list)) #Proabably shorten float to 2 significant digits (dont know how)

   print(counting_sort(random_filled_list))

   print(insertion_sort(random_filled_list))

   print(heap_sort(random_filled_list))
   
   print(quick_sort(random_filled_list))

   timed_quick_select(random_filled_list,  len(random_filled_list) // 2)
   
