# deque objects are like double-ended queues

import collections
import string

def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))#26

    # deques can be iterated over
    for elem in d:
         print(elem.upper(), end=",")#A,B.....Z,

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)#deque([1, 'b', 'c'... 'x', 'y', 2])

    # rotate the deque
    print(d)#deque([1, 'b', 'c'... 'x', 'y', 2])
    d.rotate(1)
    print(d)#deque([2, 1, 'b', 'c'... 'w', 'x', 'y'])


if __name__ == "__main__":
    main()