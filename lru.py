"""
Least Recently Used Cache
"""
from __future__ import print_function  # py2/3 compatibility
import sys
get_input = input  # py2/3 input compatibility
# If this is Python 2, use raw_input()
if sys.version_info[:2] <= (2, 7):
    get_input = raw_input


"""classes"""


class Cache:
    """the cache, uses ordered array and Dictionary for tracking least recently used and key value pairs"""

    def __init__(self, size):
        self.size = size  # the size of the cache
        self.hash_table = {}  # init a dictionary to work as the hash-table for KEY VALUE pairs
        self.key_array = []

    def set(self, k, v):
        # determine if key is in key_array
        try:
            # if is in key_array
            key_index = self.key_array.index(k)
            # pop key from key array
            self.key_array.pop(key_index)
            # append key to key_array
            self.key_array.append(k)
        except:
            # if not
            # if len(key_array) >= size
            if len(self.key_array) >= self.size:
                # remove oldest element of array
                remove_key = self.key_array.pop(0)
                # remove k/v from dict
                del self.hash_table[remove_key]
            # append key to key_array
            self.key_array.append(k)
        # upsert v in dict
        self.hash_table[k] = v
        print("SET OK")

    def get(self, k):
        try:
            # if is in key_array
            key_index = self.key_array.index(k)
            # pop key from key array
            self.key_array.pop(key_index)
            # append key to key_array
            self.key_array.append(k)
            # print GOT v from dict
            print("GOT %s" % self.hash_table[k])
        except:
            # if not in key_array
            # return NOTFOUND
            print("NOTFOUND")

    def __str__(self):
        output = "SIZE: %s " % self.size
        output += "KEY_ARRAY: %s " % ','.join(self.key_array)
        output += "HASH-TABLE: %s " % str(self.hash_table)
        return output


"""functions"""


def operations(cache_size):
    """ operations from input for each GET/SET, terminate gracefully with EXIT """
    # init cache
    cache = Cache(cache_size)

    # exit signal
    exit_flag = 0

    # continuously take inputs
    while not exit_flag:
        # DEBUG
        # print(cache)

        # input operation
        op = get_input().split(" ")
        if op[0] not in ['GET', 'SET', 'EXIT']:
            print("ERROR")
            continue

        cmd = op[0]

        # terminate
        if cmd == 'EXIT':
            exit_flag = 1
        elif cmd == 'GET':
            if len(op) > 2:
                print("ERROR")
                continue
            key = op[1]
            cache.get(key)
        elif cmd == 'SET':
            key = op[1]
            if len(op) < 2:
                print("ERROR")
                continue
            value = op[2]
            cache.set(key, value)


"""main() entry point"""
if __name__ == "__main__":

    # first operation has to be SIZE <integer>
    size_op = get_input().split(" ")

    # check if first operation is SIZE and <integer> is integer
    if (size_op[0] != 'SIZE') or (not (size_op[1]).isdigit()):
        exit("ERROR")
    else:
        input_size = int(size_op[1])
        # start taking operations
        operations(input_size)

