target_word = "carve"

num_rounds = 6

word_file = open("words.txt", "r")
word_list = []
next_word = "XX"
while next_word != "":
  next_word = word_file.readline().strip()
  if next_word != "":
    word_list.append(next_word)
    #print(word_list)

for round in range(num_rounds):
  guess = input("Enter a 5 letter word: ")
  while guess not in word_list:
    print("this is invalid")
    guess = input("please enter a guess: ")
  
  output = ""
  
  for i in range(len(target_word)):
    if guess[i] == target_word[i]:
      output += "🟩"
    elif guess[i] in target_word:
      output += "🟨"
    else:
      output += "⬜"
  print(output)
  if guess == target_word:
    print("you've won")
    break