#Main file for UI interface and calling sorting algorithms
from typing import List, Dict, Tuple
import random
import time
from radix_demo import *

#Demo to test out for calling functions from files and using random int generators
#To test with other algorithsm comment out other __name__ == __main__  from respective files
if __name__ == "__main__":
   random_index_size = random.randint(1,50) #Sets index ranging from 1 - 50

   #Filling the list with numbers from 1 - 200. May be increased if need to
   random_filled_list = [random.randint(1, 200) for i in range(random_index_size)] 
   
   base = 10 #Printing purposes but it shows base number for radix sort
   
   #Prints with function already inside for efficiency, may change as it shows time before sorted list
   print(radix_sort_lsd_nonneg(random_filled_list,10))
   