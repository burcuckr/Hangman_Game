import random
import day7HangmanArts
import day7HangmanWords

print(day7HangmanArts.logo)
chosen_word = random.choice(day7HangmanWords.word_list)

print("_" * len(chosen_word))

game_over = False
lives = 6
current_word_letters = []
while not game_over:

    user_guess = input("Bir harf tahmin et ve yaz: ").lower()

    if user_guess in current_word_letters:
        print("Bu tahmini daha önce yaptın! Başka bir harf dene.")
        continue
    if user_guess in chosen_word and user_guess not in current_word_letters:
        current_word_letters.append(user_guess)
        print(f"{user_guess} harfi kelimede var!")

    display = ""
    for char in chosen_word:
        if char in current_word_letters:
            display += char
        else:
            display += "_"
    print(display)

    if user_guess not in chosen_word:
        lives -= 1
        print(f"Tahmin ettiğin {user_guess} harfi kelimenin içerisinde değil. 1 can kaybettin.")
        print(f"{lives}/6 deneme hakkın kaldı")
        if lives == 0:
            game_over = True
            print(f"Kaybettin. Doğru kelime: {chosen_word}")
            

    if "_" not in display:
        game_over = True
        print("Kazandın!")

    print(day7HangmanArts.stages[lives]) 
