print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.strip().lower() not in ["yes", "y"]:
    print("Okay! Maybe next time :)")
    quit()

print("Okay! Let's play :)")

score = 0
quiz = [
    {"quiz": "What does CPU stand for? ", "answer": "central processing unit"},
    {"quiz": "What does GPU stand for? ", "answer": "graphic processing unit"},
    {"quiz": "What does RAM stand for? ", "answer": "random access memory"},
    {"quiz": "What does PSU stand for? ", "answer": "power supply"},
]

for question in quiz:
    answer = input(question["quiz"])
    if answer.strip().lower() == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You got {score} question(s) correct!")
print(f"You got {(score/4)*100}%.")
