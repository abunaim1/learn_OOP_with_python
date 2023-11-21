# take multiple input in one line


# map (ki korte chai, kar upor korte chai)
# list = tuple(map(int, input().split()))
# list = list(map(int, input().split()))
# print(list)

# lst = [1,2,3,4]
# def sq(i):
#     return i*i
# result = map(sq, lst)

# result = map(lambda i: i*i, lst)
# print(list(result))

# join -> list to string convert
# join function sudhu matro string accept kore
lst = [1,2,3,4,5]
# list er element gulo join korbo
# 1. list e jodi 'int' thake map diye segulo string e convert korbo. 
result = list(map(lambda i: str(i), lst))

# 2. erpor join function chalabo 
f = " ".join(result)
print(f)