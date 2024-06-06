def game():
    guesses=[]
    count=0
    quest_num=1
    for key,value in questions.items():
        print(key)
        for i in options[quest_num -1]:
            print (i)  
        quest_num +=1
        guess=input("enter A, B, C or D").upper()
        guesses.append(guess)
        count+=check_answer(questions.get(key),guess)
    display_result(count,guesses)

def check_answer(answer,guess):
    if (answer==guess):
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
def display_result(count,guesses):
    print("Correct guess:",end="")
    for i in questions:
       print(questions.get(i),end=" ")
    print("\n")
    print("your guess:",end="")
    for i in guesses:
        print(i,end=" ")
    print("\n")
    perc=count/4*100
    print("you scored :"+str(perc) +"%")

def play_again():
    a=input("play again?(y/n)").upper()
    if a=="Y":
        return True
    else:
        return False

questions={"In which year did Nepal become a federal democratic republic? ":"C",
            "Which river is considered the longest river in Nepal? ":"D",
            'Who was the first king of unified Nepal?':'B',
            'What is the name of the famous trekking region located in northeastern Nepal?':'D'
            }

options=[["A. 2000", "B. 2006"," C. 2008", "D. 2015"],
            ["A. Bagmati River", "B. Gandaki River", "C. Koshi River", "D. Karnali River"],
            ["A. Tribhuvan", "B. Prithvi", "C. Gyanendra", "D. Mahendra "],
            ["A. Annapurna", "B. Langtang", "C. Mustang", "D. Everest (Khumbu)"]]

game()
while(play_again()):
        game()

        