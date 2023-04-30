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

