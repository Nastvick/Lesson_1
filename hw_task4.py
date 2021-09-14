questions = {'5*5: ':'25',
             '4+8: ':'12',
             '25*10: ':'250',
             '72-48: ':'24',
             '11*5: ':'55'}
score1 = 0
score2 = 0
for q in questions.keys():
    user_answer = input(q)
    if questions.get(q) == user_answer:
        score1+=1
        print("Correct!")
    else:
        score2+=1
        print("Wrong!")
print("You have got "+str(score1)+" right answers!")
print("You have got "+str(score2)+" wrong answers!")


