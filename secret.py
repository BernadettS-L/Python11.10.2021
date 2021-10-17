import random
secret_nr = random.randint(1, 30)

talalt = "Correct answer"
hibas = "Incorrect answer"
attempts = 0
message = f"Correct answer is {secret_nr}"

with open("score.txt","r") as score_file:
    best_score = int(score_file.read())
    print("top score: " + str(best_score))

while True:
    guess = int(input("Pick a number!"))
    attempts += 1

    if guess == secret_nr:
        if attempts < best_score:
            with open("score.txt","w") as score_file:
                score_file.write(str(attempts))
        print("yes!")
        print("Attempts needed: " +str(attempts))
        break
    elif guess > secret_nr:
        print("Nope, the number is smaller")

    elif guess < secret_nr:
        print("Nope, the number is higher")
