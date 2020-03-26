#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    # loop over tickets and insert in ht
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)


    # find ticket with none src
    source_flight = hash_table_retrieve(hashtable, "NONE")

    current = source_flight

    # looping over n-1 times to make up for the "NONE" flight source
    for i in range(length - 1):

        # used for chaining together flights
        next_stop = hash_table_retrieve(hashtable, current)

        # setting the destination to the current 'i' index in the array
        route[i] = current

        # updating current to next flight source for next iteration
        current = next_stop     

        
    return route
