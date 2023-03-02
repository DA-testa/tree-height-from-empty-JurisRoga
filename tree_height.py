# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    cela_gar = np.zeros(n, dtype=int)
    max_height = 0
    # Your code here
    for elements in range(n):
        height = 0
        while elements != -1:
            if cela_gar[elements] != 0:
                height += cela_gar[elements]
                break
            height += 1
            elements = parents[elements]
        cela_gar[elements] = height
        if height > max_height:
            max_height = height
    return max_height


def main():
    # implement input form keyboard and from files
    parbaude = input()
    if parbaude == "I":
        node_sk = int(input())
        parents = np.array(list(map(int, input().split())))
    else:
        vieta = input()
        if "a" in vieta:
            print("Nepareiza ievade")
            return
        with open(vieta) as fails:
            node_sk = int(fails.readline())
            parents = np.array(list(map(int, fails.readline().split())))
    height = compute_height(node_sk, parents)
    print(height)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))