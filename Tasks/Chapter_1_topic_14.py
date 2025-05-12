def ask_info(information):
    information["Name"] = input("Enter your Name:")
    information["Age"] = input("Enter your Age:")
    information["Gender"] = input("Enter your Gender:")
    information["City"] = input("Enter your current city:")

def show_info(information):
    print("\nShowing your information")
    print("Name :", information["Name"])
    print("Age :", information["Age"])
    print("Gender :", information["Gender"])
    print("city :", information["City"])

tarif_info = {"a":0}
ask_info(tarif_info)
del tarif_info["a"]
show_info(tarif_info)


