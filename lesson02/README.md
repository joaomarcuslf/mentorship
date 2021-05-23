# Data Structure #02

You have three functions that need to be completed.

The first, `get_user_index_by_name`, you will receive a list of names, and you must return the index where the user's name is or -1.

The second, `get_room_index_by_name`, you will receive a matrix with names of the registrants per room, and must return the index of the room where the name is or -1.

The third, `get_room_and_user_indexes_name`, you will receive a matrix with names of the enrolled per room, and must return the index of the room and the student in the room or [-1, -1].

## Advanced topics

### Ex.01: Flatten

Given this Matrix:

```py
matrix = [
  [1,2,3, [ 3, 4 ] ],
  [5, [ 8, [ 7 ] ] ],
  [ 6 ],
]
```

Create an algorithm that converts this matrix in one dimensional array, like this:

```py
list = [ 1, 2, 3, 3, 4, 5, 8, 7, 6 ]
```

The order won't matter, but every element in the matrix should be in the final list.

### Ex.02: Flatten with reference

Given this Matrix:

```py
matrix = [
  [1, 3, [ 3 ] ],
  [ 6, [ [ [ [ [ [ [ 7 ] ], 8 ] ] ] ] ] ],
]
```

Create an algorithm that converts this matrix in one dimensional array, but it should keep the reference to where it was in the Matrix:

```py
reference_list = [
  { 'value': 1, 'index': [ 0, 0 ] },
  { 'value': 3, 'index': [ 0, 1 ] },
  { 'value': 3, 'index': [ 0, 2, 0 ] },
  { 'value': 6, 'index': [ 1, 0 ] },
  { 'value': 7, 'index': [ 1, 1, 0, 0, 0, 0, 0, 0, 0 ] },
  { 'value': 8, 'index': [ 1, 1, 0, 0, 0, 0, 1 ] },
]
```

The order won't matter, but every element in the matrix should be in the final list.

### Ex.03: Get in Matrix

Now, using the code created in the last exercise, create a function that given an `index` in the processed list, get the real element in matrix. I want the value from the `matrix`, even though you have saved the value, it can change in the original matrix.

```py
reference_list = [
  { 'value': 1, 'index': [ 0, 0 ] },
  { 'value': 3, 'index': [ 0, 1 ] },
  { 'value': 3, 'index': [ 0, 2, 0 ] },
  { 'value': 6, 'index': [ 1, 0 ] },
]

matrix = [
  [1, 3, [ 3 ] ],
  [ 6 ],
]

get_from_matrix(reference_list, matrix, 3)
#=> Should return matrix[1][0], which is 6
```
