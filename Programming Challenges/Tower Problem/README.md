## Tower Challenge

- [Challenge Instructions](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/mini/tower.md)

A C# Solution
-----------

<details>

- [C# Solution](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/mini/tower.ipynb)

</details>

A Python Solution
---------------

<details>

- [Python Solution](https://github.com/calaldees/TeachProgramming/blob/master/teachprogramming/static/projects/mini/tower.py)

```python
def tower(n):
    return '\n'.join(
        ' '*(n-1-i) + '#'*(i*2+1)
        for i in range(n)
    )
```

</details>