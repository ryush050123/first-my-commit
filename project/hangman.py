import random

words = ["python", "turtle", "computer"] # 단어DB는 여기에

answer = random.choice(words) # 랜덤으로 단어 뽑기
guess_letters = list("_" * len(answer))
life = 5 # 남은 기회

game_over = False
while not game_over: 
    print(f"남은 기회 : {'❤' * life}")
    user_guess = input("한 글자씩 추측해 보세요 -> ").lower()

    if len(user_guess) == 1 and user_guess.isalpha(): # 한 글자만 입력할 수 있도록 하기
        for i in range(len(answer)):
            if answer[i] == user_guess:
                guess_letters[i] = user_guess
        print(guess_letters)
        print()

        if "_" not in guess_letters: # "_"가 모두 없어졌다면 "성공" 출력
            game_over = True
            print("성공!")
        
        if user_guess not in answer: # 틀렸을 경우 남은 기회에서 -1
            life -= 1
            if life == 0: # 남은 기회가 0이 되었을 경우 게임 오버
                game_over = True
                print(f"실패!! 정답은 {answer} 이었습니다.")
    else:
        print("영문 한자씩 입력해 주세요")