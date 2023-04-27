## Задачи из Home Work -1.
#### Задача 1.
Create a method to see whether the string is ALL CAPS.
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

**Решение 1**
```
def is_uppercase(inp):
    al = 0
    sp = 0
    st = '''/[!@#$%^&*()~_+\`-=\[\]{};':"\\|,.<>\/?]+/'''
    for i in inp:
        if i.isupper() or i.isdigit() or i in st:
            al = al + 1
        if i == ' ':
            sp = sp + 1      
    if al == len(inp) - sp:
        return True
    else:
        return False
```
**Решение 2**
```
def is_uppercase(inp):
    return inp.upper()==inp
```
#### Задача 2.
Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.
42, "int"    --> True
"42", "int"  --> False

**Решение 1**
```
def type_validation(variable, _type):
    if _type in str(type(variable)):
        return True
    else:
        return False
```
**Решение 2**
```
def type_validation(variable, _type): 
    return _type in str(type(variable))
```
#### Задача 3.
Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
remove("Hi!") == "Hi"
remove("Hi!!!") == "Hi!!"
remove("!Hi") == "!Hi"
remove("!Hi!") == "!Hi"
remove("Hi! Hi!") == "Hi! Hi"
remove("Hi") == "Hi"

**Решение 1**
```
def remove(s):
    if s.endswith('!'):
        return s[:len(s)-1]
    else:
        return(s)
```
**Решение 2**
```
def remove(s):
    return s[:-1] if s.endswith('!') else s
```
**Решение 3**
```
def remove(s):
    return s[:-1] if s and s[-1] == '!' else s
```
**Решение 4**
```
def remove(s):
    return s.removesuffix('!')
```
#### Задача 4.
Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.

'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'

**Решение 1**
```
def string_clean(s):
    st = ''
    for i in s:
        if i.isdigit():
            st = st + ''
        else:
            st = st + i
    return st
```
**Решение 2**
```
def string_clean(s):
    return ''.join(i for i in s if not i.isdigit())
```
**Решение 3**
```
def string_clean(s):
     for i in '0123456789':
     s = s.replace(i, '')
    return s
```
#### Задача 5.
Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

**Решение 1**
```
def get_number_from_string(string):
    st=''
    for i in string:
        if i.isdigit():
            st = st + i
    st = int(st)
    return st
```
**Решение 2**
```
def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))
```
#### Задача 6.
Create a function named (combine_names) that accepts two parameters (first and last name). The function should return the full name.
**Решение 1**
```
def combine_names(first, last):
    return first + " " + last
```
**Решение 2**
```
def combine_names(*args):
    return ' '.join(args)
```









