class LRUCache:

def __init__(self,limit=10):
    self.limit = limit
    self.length = 0
    self.list = DoublyLinkedList()
    self.storage = {}

def get(self, key):

    if key in self.storage:
        node = self.storage[key]
        self.list.move_to_end(node)
        return node.value[1]
    else:
        return None


def remove(self,key, value):
    # if the cache is empty:
        # add to the linked list (key and the vallue )
        # increment size
    # if cache not empty:
        # check and see if the key is in the dict
            # if it is
                # overwrite the vlaue
                # move it to the end
            # if it isn't
                # check and see if cache is full
                    # if cache is not full
                        # came as if cache is empty
                    # if cache is full
                        # remove oldest entry from dictionary AND LL
                        # reduce the size
                        # add a new value?
    # add to the linked list (key and value)
    # add the key and value to the dictionary
    # increment size


    if key in self.storage:
        node = self.storage[key]
        node.value = (key, value)
        self.list.move_to_end(node)
        return

    if self.length == self.limit:
        del self.storage[self.list.head.value[0]]
        self.list.remove_from_head()
        self.length -= 1

    self.list.add_to_tail((key, value))
    self.storage[key] = self.list.tail
    self.length +=1
