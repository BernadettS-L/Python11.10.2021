with open("bonus.csv", "r") as bonus_file:
    content = bonus_file.read().splitlines()

    for row in content:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
