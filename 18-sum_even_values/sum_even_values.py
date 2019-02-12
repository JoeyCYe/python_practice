'''
Write a function called sum_even_values. This function should accept a list of numbers and return the sum of all the even numbers. 
If there are no even numbers, the function should return 0.

Examples

```py
sum_even_values([1, 2, 3, 4, 5, 6]) # 12
sum_even_values([4, 2, 1, 10]) # 16
sum_even_values([1]) # 0
```
'''

def sum_even_values(lst):
    even_numbers = [num for num in lst if num %2 == 0]
    if even_numbers == []:
        return 0
    else:
        return sum(even_numbers)