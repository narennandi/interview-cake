"""
I have a list of n + 1n+1 numbers. Every number in the range 1..n1..n appears once except for one number that appears twice.

First, we sum all numbers 1..n1..n. We can do this using the equation:

(n*2 +n) / 2

because the numbers in 1..n1..n are a triangular series. ↴

"""

def find_repeat(numbers_list):
    if len(numbers_list) < 2:
        raise ValueError('Finding duplicate requires at least two numbers')

    n = len(numbers_list) - 1
    sum_without_duplicate = (n * n + n) / 2

    actual_sum = sum(numbers_list)

    return actual_sum - sum_without_duplicate

"""
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.

We choose a random item to move to the first index, 
then we choose a random other item to move to the second index, etc. 
We "place" an item in an index by swapping it with the item currently at that index.

Crucially, once an item is placed at an index it can't be moved. 
So for the first index, we choose from nn items, for the second index we choose from n-1n−1 items, etc.
This is a semi-famous algorithm known as the Fisher-Yates shuffle (sometimes called the Knuth shuffle).
"""
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    # If it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # Walk through from beginning to end
    for index_we_are_choosing_for in xrange(0, len(the_list) - 1):

        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index_we_are_choosing_for,
                                         last_index_in_the_list)

        # Place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing_for]

"""
Suppose we had a list ↴ of nn integers sorted in ascending order. How quickly could we check if a given integer is in the list?
"""

def binary_search(nums, target):

    low = 0
    high = len(nums) -1

    while low <= high:

        mid = (high + low) // 2

        if nums[mid] == target:
            return mid
        
        elif target > nums[mid]:
            low = mid + 1 

        else:
            high = mid - 1
    
    return "Target not in array"


