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
    for i in range(len(weights)):
        if hash_table_retrieve(ht, limit - weights[i]):
            index1 = i
            index2 = hash_table_retrieve(ht, limit - weights[i])
            if index1 > index2:
                return(index1, index2)
            return (index2, index1)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
