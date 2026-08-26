print("===== zip =====")

people_name_list = ["김철수","김영희","임꺽정"]
people_age_list = [20 , 21 , 33]

for name,age in zip(people_name_list,people_age_list):
    print(f"name : {name}, age : {age}")
