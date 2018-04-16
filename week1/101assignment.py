import random
korean = ["분식집", "백반집", "해물탕집"]
japannese = ["초밥집", "우동집", "돈까스집"]
chinnese = ["만두집", "탕수육집", "중국집"]

rastaurant = input("한식, 중식, 일식 중에 고르세요")
if rastaurant == "한식":
    print(random.choice(korean))
if rastaurant == "일식":
    print(random.choice(japannese))
if rastaurant == "중식":
    print(random.choice(chinnese))
