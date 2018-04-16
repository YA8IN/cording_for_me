user = input("가위, 바위, 보")
import random

list_a = ["가위","바위", "보"]
if user =="가위":
    print(random.choice(list_a))
elif user =="바위":
    print(random.choice(list_a))
elif user =="보":
    print(random.choice(list_a))
else:
    print("유효하지 않은 입력 입니다.")
