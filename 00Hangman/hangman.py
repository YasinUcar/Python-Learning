import hangman_words
import hangman_art
import random

words = hangman_words.word_list
logo = hangman_art.logo
stages = hangman_art.stages

print(logo)
random_word = random.choice(words)
word_length = len(random_word)
print(f"Seçilen kelime : {random_word}")
blank_List = []
lives = 6

for list in range(word_length):
    blank_List += "_"

end_of_game = False
while not end_of_game:
    tahmin = input("Kelime giriniz: ").lower()
    for i in range(word_length):
        if tahmin == random_word[i]:
            blank_List[i] = tahmin
            
    if tahmin not in random_word:
        lives-=1
    if(lives<=0) :
        end_of_game=True
        print("You Lose!")
    if "_" not in blank_List:
        end_of_game = True
        print("You Win!")

    print(blank_List)
    print(stages[lives])