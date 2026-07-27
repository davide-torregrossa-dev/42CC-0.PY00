def ft_plant_age():
    plant_days = input("Enter plant age in days: ")
    if int(plant_days) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
