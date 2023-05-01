## Задачи из Home Work-2.
### Задача 1.
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= length of input <= 100
All inputs will be strings, consisting only of characters ( and ).
Empty strings are considered balanced (and therefore valid), and will be tested.
For languages with mutable strings, the inputs should not be mutated.

**Решение 1**
```
def valid_parentheses(paren_str):
    n = 0
    for i in paren_str:
        if i == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            return False
    return n == 0
```
**Решение 2**
```
def valid_parentheses(paren_str):
    while "()" in paren_str:
        paren_str = paren_str.replace("()", "")
    return paren_str == ""
```
### Задача 2.
Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.
For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.
If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

**Решение 1**
```
def nearest_sq(n):
    return round(n**0.5)**2
```
### Задача 3.
Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
Notes
Array/list size is at least 2 .
Array/list's numbers Will be only Positives
Repetition of numbers in the array/list could occur.

Input >> Output Examples
productArray ({12,20}) ==>  return {20,12}

Explanation:
The first element in prod [] array 20 is the product of all array's elements except the first element
The second element 12 is the product of all array's elements except the second element .

test.assert_equals(product_array([12,20]), [20,12])
test.assert_equals(product_array([3,27,4,2]), [216,24,162,324])
test.assert_equals(product_array([13,10,5,2,9]), [900,1170,2340,5850,1300])
test.assert_equals(product_array([16,17,4,3,5,2]), [2040,1920,8160,10880,6528,16320])

**Решение 1**
```
def product_array(numbers):
    p = 1
    lst = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j !=i:
                p = p*numbers[j]                 
        lst.append(p)
        p = 1
    return lst
```
**Решение 2**
```
from numpy import prod
def product_array(numbers):
    p = prod(numbers)
    return [p // i for i in numbers]
```

