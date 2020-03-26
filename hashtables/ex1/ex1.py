#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):

        value_needed = limit - weights[i]

        difference_idx = hash_table_retrieve(ht, value_needed)

        if difference_idx: 
  
            if i < difference_idx:

                pair = [ difference_idx, i]

                return pair

            else:
                pair = [ i, difference_idx ]

                return pair
            
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



