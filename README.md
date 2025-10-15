Project 2 
i have got the question as per my last GW digit
Option 0: Quick select, deterministic (median of medians method)

I have used the following steps to solve:
1. Divide the array A into groups of 5 elements each.  
2. Sort each small group using Insertion sort.  
3. Collect the median from each group to n / 5 medians.  
4. Recursively find the median of these medians to use as the pivot.  
5. Partition A around this pivot.  
6. Recurse into the left or right partition depending on k.

I have used the following python libraries and ran the code in python 3
import time
import random
import matplotlib.pyplot as plt
import numpy as np

i have checked the values for the following n = [15, 16, 17, 18, 19, 20, 50, 100, 500, 1000, 2000, 4000, 8000, 16000, 32000]

As to analyze the graph properly run the code multiple times to get the proper graph for the analysis


