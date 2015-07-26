#?/usr/bin/env python

#Prob 15: Lattice paths

"""
for an nxn lattice, moving down and right only in increments of 1 unit at a time,
one would need to make n+n total moves to get from one corner to the next.
"""
import math
def num_of_lattice_paths(length):
    """
    find the number of paths for a square lattice
    """
    numerator = math.factorial(length + length)
    denominator = math.factorial(length) * math.factorial(length)
    
    return numerator/denominator

print num_of_lattice_paths(20)