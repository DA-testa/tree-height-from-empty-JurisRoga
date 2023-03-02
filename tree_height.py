# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    cela_gar = np.zeros(n, dtype=int)
    # Your code here
    for elements in range(n):
        if cela_gar[elements] != 0:
            continue
        height = 1
        vertiba = parents[elements]
        while vertiba != -1:
            if cela_gar[vertiba] != 0:
                height += cela_gar[vertiba]
                break
            height += 1
            vertiba = parents[vertiba]
        j = elements
        while j != -1 and cela_gar[j] ==0:
            cela_gar[j] = height
            height -= 1
            j = parents[j]
    return np.max(cela_gar)


def main():
    # implement input form keyboard and from files
    parbaude = input().strip()
    if parbaude == "I":
        node_sk = int(input().strip())
        parents = np.array(list(map(int, input().split())))
    else:
        vieta = input().strip()
        if "a" in vieta:
            print("Nepareiza ievade")
            return
        with open ("test/" + vieta, mode= 'r') as fails:
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
# main()
# print(numpy.array([1,2,3]))