# Author PT 12/15/20

def double_stuff(lst):
    for index, value in enumerate(lst):
        lst[index] = 2 * value
        return lst


print(double_stuff([1, 2, 3, 4]) == [2, 4, 6, 8])
print(double_stuff([1.1, 2, 3.14, 4]) == [2.2, 4, 6.28, 8])
print(double_stuff([1, "a", 3, "b"]) == [2, "aa", 6, "bb"])
