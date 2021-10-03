import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    # print(data)

    # for i in data["cards"]:
    #     print(i)

    total=len(data["cards"])
    score=0;

a = True
while(a):
    for i in data["cards"]:
        guess=input(i["q"] + " > ")
        # print(guess)

        # if guess == i["a"]:
        if guess.lower() == i["a"].lower():
            score +=1
            print(f"Correct!")
            print(f" Current Score: {score}/{total}")
        else:
            print("Incorrect! The answer was ", i["a"])
            print(f" Current Score: {score}/{total}")

    print(f"Good studying! You scored {score}/{total}.")
    again=input("Play again?")
    if(again.lower()=="yes"):
        a = True;
    else:
        a = False;
        print("Goodbye!")
