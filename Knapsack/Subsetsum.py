'''
Author: Connor Keenum
Date: 28 Aug 2021
Description: Find the closest subset sum less than or equal to the target value
Algorithm: Recursive Backtracking 
Complexity: O(2^n)

Input: 
    Array of numbers
    Target number

Output: 
    Array of numbers whose sum is closest to the target value
'''

import itertools;
def subsetsum(array, target):
    absDiff = target
    bestCombo = []

    for L in range(0, len(array) + 1):
        for subset in itertools.combinations(array, L):
            s = sum(subset)
            absDiff_test = abs(target - s)
            if s == target:
                absDiff = absDiff_test
                bestCombo = subset
                return bestCombo
            elif ((s < 0 and s >= target) or (s > 0 and s <= target)) and (absDiff_test <= absDiff):
                absDiff = absDiff_test
                bestCombo = subset
    return bestCombo

targetPoints = 21902
amexCharges = [
    458,
    1933,
    8332,
    2132,
    2492,
    1183,
    708,
    1500,
    970,
    3497,
    2492,
    1417,
    1332,
    1583,
    523,
    1667,
    4782,
    2498,
    967,
    4845,
    8667,
    767,
    1982,
    4958,
    1517,
    308,
    382,
    1517,
    375,
    1275,
    583,
    1467,
    1133,
    2492,
    4838,
    1133
]

print(subsetsum(amexCharges,targetPoints))