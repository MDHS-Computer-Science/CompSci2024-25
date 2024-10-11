target_word = "might"

numbOfGuesses = 6

wordFile = open("words.txt", "r")
wordList = []
nextWord = "AA"
while nextWord != "":
  nextWord = wordFile.readline().strip()
  if nextWord != "":
    wordList.append(nextWord)

for i in range(numbOfGuesses):
  guess = input("Please input a guess: ")
  while (guess not in wordList):
    print("This guess is invalid")
    guess = input("Please input a guess: ")

  output = ""

  for a in range(len(target_word)):
    if guess[a] == target_word[a]:
      output = output + '🟩'
    elif guess[a] in target_word:
      output = output + '🟨'
    else:
      output = output + '⬛'

  print(output)
  if guess == target_word:
    print("You guessed the word :D")
    break
