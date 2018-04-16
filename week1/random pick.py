import random
list = []
ran_num = random.randint(1,5)

for i in range(1):
    while ran_num in list:
        ran_num =random.randint(1,5)
    list.append(ran_num)

list.sort()
print(list)




import random
i = [1, 2, 3, 4, 5]
print(random.choice(i))
