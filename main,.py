l = (i for i in range(10))
val_map = list(map(lambda x: x*2,l))
''' map - для поледовательного применения функции к кадоме елементу итерированого обьекта'''

def filte_func(x):
    if x %2 == 0:
        return x
val_filter = list(filter(filte_func,val_map))
'''filter - для фильтрации елементов в итерированом обьекте'''
from functools import reduce
def my_f(x,y):
    return x+y
reduce_obj = reduce(my_f,val_filter)

'''reduce - moduel functools - прменяет функцию к елементам итерируемого обьекта поочередно чтоб получить одно значение'''

num = [i for i in range(1,6)]

def check(num,flag = None):
    '''
    any - хотябы одни
    all - обьязательно все
    '''
    if flag != None:
        return any(x>4 for x in num)
    else:
        return all(x>0 for x in num)