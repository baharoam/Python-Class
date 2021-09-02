Nationality = int(input("Hello, Are you persian or not? \n 1.Yes \n 2.No"))
if Nationality==1:
    ScoreIrani= int(input("Tell us your score : "))
    if 18<=ScoreIrani<=20:
        print("you got A")
    if 16<=ScoreIrani<18:
        print("you got B")
    if 14<=ScoreIrani<16:  
        print("you got C")
    if 12<=ScoreIrani<14:
        print("you got D")
    if 10<=ScoreIrani<12:
        print("you got E")
    elif 0<ScoreIrani<10:
        print("you got F")
elif(Nationality==2):
    Score= input("Tell us your score : ")
    if Score == 'A': 
        print("Your score is between 18 and 20")
    if Score == 'B':
        print("Your score is between 16 and 18")
    if Score == 'C':
        print("Your score is between 14 and 16")
    if Score == 'D':
        print("Your score is between 12 and 14")
    if Score == 'E':
        print("Your score is between 10and 12")
    if Score == 'F':
        print("Your score is under 10 and you failed")


else:
    print("Wrong Command")