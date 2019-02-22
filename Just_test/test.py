# import monk
#
# def simple_func():
#     print('Standart func was called')
#
# simple_func()
#
# def monkey_f():
#     print('monkey func called')
#
# simple_func = monkey_f
#
# simple_func()

try:
    i = int(input())
except ValueError:
    print('bitch')
else:
    print('continue')
finally:
    print("is it work")