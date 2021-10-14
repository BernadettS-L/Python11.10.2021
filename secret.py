secret_nr = 4
guess = 0

talalt = "Correct answer"
hibas = "Incorrect answer"

message = f"Correct answer is {secret_nr}"

while guess != secret_nr:
    guess = int(input("Pick a number!"))
    if guess == secret_nr:
        print(f"{talalt}")
    else:
        print(f"{hibas} {message}")
