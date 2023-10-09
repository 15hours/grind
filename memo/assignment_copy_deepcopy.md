### Assignment:
```python
colors = ['red', 'blue', 'green']
b = colors

>> b.append('white')

>> b
>> ['red', 'blue', 'green', 'white']

>> colors
>> ['red', 'blue', 'green', 'white']
```

### Shallow copy:
###### For simple objects:
```python
a = [[1, 2], [2, 4]]
b = a[:] ## shallow copy

>> b.append([3, 6])

>> b
>> [[1, 2], [2, 4], [3, 6]]

>> a
>> [[1, 2], [2, 4]]
```
###### For compund objects:
```python
a = [[1, 2], [2, 4]]
b = a[:] #shallow copy

>> b[0].append(3)  ## Edit the first element (i.e. [1, 2])
>> b
>> [[1, 2, 3], [2, 4]]

>> a
>> [[1, 2, 3], [2, 4]]
```

### Deep copy:
```python
a = [[1, 2], [2, 4]]

>> import copy
>> b = copy.deepcopy(a) ## deep copy
>> b[0].append(3)  ## Edit the first element (i.e. [1, 2])

>> b
>> [[1, 2, 3], [2, 4]]

>> a
>> [[1, 2], [2, 4]] ## does not affect the original list
```
