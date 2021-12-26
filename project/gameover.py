from random import *

words = ["python", "turtle", "computer"] # 단어DB는 여기에 
word = choice(words) # 단어들 중에 랜덤으로 선택된 단어
print("answer : " + word)
letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳
life = 3 # 남은 기회
game_over = False

while not game_over:
    
    print(f"남은 기회: {life}번")
    succeed = True # 성공 여부
    print()
    for w in word: # ex) p y t h o n
        if w in letters:
            print(w, end=" ")
        else: # "_"가 남아있으면 succeed를 False로 유지
            print("_", end=" ")
            succeed = False 
    print()

    if succeed: # 성공 했으면 "Success" 출력
        print("Success")
        break

    letter = input("Input letter -> ") # 사용자 입력칸
    if letter not in letters:
        letters += letter
    
    if letter not in letters:
        life = life - 1
        if life == 0 :
            game_over = True
            print(f"게임 오버! 정답은 {letters}입니다.")

    if letter in word: # 입력받은 글자의 맞음/틀림 여부 출력
        print("Correct")
    else:
        print("Wrong!")

