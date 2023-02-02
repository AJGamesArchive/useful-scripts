## In A Row Challenge

- [Challenge Instructions](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/mini/in_a_row.md)

A C# Solution
-----------

<details>

- [C# Solution](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/mini/in_a_row.ipynb)

</details>

A Python Solution
---------------

<details>

- [Python Solution](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/mini/in_a_row.py)

```python
def in_a_row(data):
    max_count = 0
    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
            else:
                count = 0
            if count > max_count:
                max_count = count
    return max_count
```

</details>