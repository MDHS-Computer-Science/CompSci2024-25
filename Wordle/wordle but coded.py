target_word = "scary" # targetted word to guess

number_of_rounds = 6 # number of rounds



wordFile = open("words.txt", "r")
wordList = []
nextWord = "BB"
while nextWord != "":
  nextWord = wordFile.readline().strip()
  if nextWord != "":
    wordList.append(nextWord)
    # print(wordList)
for round in range(number_of_rounds):
  print("Round:", round+1)
  guess = input("Please enter a guess: ")
  while (len(guess)) != len((target_word)):
    print("Your guess is invalid noob")
    guess = input("Please enter a guess: ")


  output = ""


  for i in range (len(target_word)):
    if guess[i] == target_word[i]:
      output = output + '🟩'
    elif guess[i] in target_word:
      output = output + '🟨'
    else:
      output = output + '⬜'
  print(output)
  # print guess
  if guess == target_word:
    print("Congratulations!, You are a winner!")
    break
