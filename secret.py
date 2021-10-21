import json
import random

secret_nr = random.randint(1,30)

talalt = "Correct answer"
hibas = "Incorrect answer"
attempts = 0
message = f"Correct answer is {secret_nr}"

with open("score_list","r") as score_file:
    score_list = json.loads(score_file.read())
    print("top score: " + str(score_list))

score_list.sort()
print(score_list[:3])

while True:
    guess = int(input("Pick a number!"))
    attempts += 1

    if guess == secret_nr:
        score_list.append(attempts)

        with open("score_list","w") as score_file:
            score_file.write(json.dumps(score_list))
        print("yes!")
        print("Attempts needed: " +str(attempts))
        break
    elif guess > secret_nr:
        print("Nope, the number is smaller")

    elif guess < secret_nr:
        print("Nope, the number is higher")
