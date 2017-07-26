Design and implement an LRU (Least Recently Used) cache.
--------------------------------------------------------
This readme.md in well formatted Markups and the code can also be found here:

https://github.com/haowu0802/lru

To Run:
---
`python lru.py`

Specification
---
Algorithm
* fixed sized cache in terms of the number of items
* won't worry about the number of bytes, (this implies memory space is cheap in this situation)
* keys and values are strings, with no spaces
* cache support gets and sets(upsert)
* when full, upon insert, the least recently used item shall be overwritten or removed
* persistence across sessions not needed

Application behaviors
* read from stdin, write to stdout, no prompt/extra line
* first input set SIZE - max number of items in cache, respond SIZE OK, as first OP
* to SET item: SET <KEY> <VALUE>, return SET OK
* to GET item: GET <KEY>, return GOT <VALUE> or NOTFOUND if not found
* EXIT to terminate gracefully
* invalid input: respond ERROR

Analysis
--------
* when SET or GET, the item is considered being used, it should become the most recent used
* by moving the items to the top of the list each time it's GET/SET, the list becomes a sorted list ordered by 'recently used time' DESC
* ~~to be able to efficiently move an item from a certain place to the top of the list, a linked list should be a good choice of data structure~~
* ~~since the linked list is always sorted by last used time, the bottom of the list is always the least recently used item, and should be removed when the list is full and a new KEY is pushed~~
* [EDIT]since linked list does not perform well on random access, an ordered array will be used instead
* to be efficient on look ups, a hash-table should be used for the keys and their values, as described in the Algorithm section, in the current situation of the problem, memory space is not considered expensive and is not limited
* because the VALUE is looked up from the hash-table, there's no need to store them in the linked list, therefore the ~~linked list node~~ array will store the KEY as their data
* when implementing SETs and GETs, both structures(array and hash-table) will be modified
* with both array and hash-table, the look up time(on GET/SET) complexity will be O(1+n),the space complexity will be O(2*n) for having an array of the keys and a hash-table for key-value pairs


Problem Description
---
> Design and implement an LRU (Least Recently Used) cache. This is a cache with fixed size in terms of the number of items it holds (supplied at instantiation).  For this exercise, we won’t worry about the number of bytes. Your program can treat the keys and values as strings.  You don’t need to support keys or values that contain spaces.  The cache must allow client code to get items from the cache and set items to the cache. Once the cache is full, when the client wants to store a new item in the cache, an old item must be overwritten or
removed to make room. The item we will remove is the Least Recently Used (LRU) item.  Note that your cache does not need persistence across sessions.

> Please read input from stdin and print output to stdout and support the following format (please DO NOT print any kind of a prompt or extra line breaks).
All inputs and outputs exist on their own line:

> The first input line should set the max number of items for the cache using the keyword SIZE.  The program should respond with ‘SIZE OK’. This must only occur as the first operation.

> Set items with a line giving the key and value, separated by a space,
your program should respond with 'SET OK'.

> Get items with a line giving the key requested, your program should respond with the previously stored value, for example “GOT foo”. If the the key is not in the cache, it should reply with “NOTFOUND”.

> ‘EXIT’ should cause your program to exit.

> If the input is invalid, your program should respond with ‘ERROR’

| Sample Input        | Expected Output           |
| ------------- |:-------------:|
| SIZE 3      | SIZE OK |
| GET foo      | NOTFOUND      |
| SET foo 1 | SET OK      |
| GET foo  |  GOT 1 |
| SET foo 1.1  |  SET OK |
| GET foo  | GOT 1.1  |
| SET spam 2  |  SET OK |
| GET spam  |  GOT 2 |
| SET ham third  | SET OK  |
| SET parrot four  | SET OK  |
| GET foo  | NOTFOUND  |
| GET spam  | GOT 2  |
| GET ham  | GOT third  |
| GET ham parrot  | ERROR  |
| GET parrot  |GOT four   |
| EXIT  |   |













