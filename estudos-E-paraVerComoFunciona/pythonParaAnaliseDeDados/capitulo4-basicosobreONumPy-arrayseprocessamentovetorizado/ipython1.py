# coding: utf-8
import numpy as np
my_arr = np.arange(1000000)
my_arr
len(my_arr)
my_list = list(range(1000000))
get_ipython().run_line_magic('', 'time for _ in range(10): my_arr2 = my_arr * 2')
get_ipython().run_line_magic('time', 'for _ in range(10): my_arr2 = my_arr * 2')
get_ipython().run_line_magic('time', 'for _ in range(10): my_arr2 = [x * 2 for x in my_list]')
