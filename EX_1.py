#1.1 Дано 2 скрипта. Объяснить возникающие ошибки.
a = None
if len(a) > 0 or a is not None:
    print('OK')
    print('Length =', len(a))
#1.2
a = None
if a is not None and len(a) > 0:
    print('OK')
    print('Length =', len(a))