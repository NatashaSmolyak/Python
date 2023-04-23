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
