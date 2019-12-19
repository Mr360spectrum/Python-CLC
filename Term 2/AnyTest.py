# any() test

list1 = ["hi", "hello"]
list2 = [1,2,3]
list3 = [True, False]
bigList = [list1, list2, list3]
# any([desired item] in [iterable] for [iterable] in [list or 2D array, in this case])
if any(1 in list for list in bigList):
    print("yis")
else:
    print("nah")