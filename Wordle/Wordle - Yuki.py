target_word ="carve"

number_of_rounds = 6

word_file = open("words.txt", "r")
word_list = []
next_word = "XX"
while next_word != "":
  next_word = word_file.readline().strip()
  if next_word != "":
    word_list.append(next_word)



for round in range(number_of_rounds):
  print("Round:", round+1)
  guess = input("Please enter a guess: ")
  while len(guess) != len(target_word):
      print("This guess is invalid, try again!")
      guess = input("Please eneter a guess: ")

  
  output = ""


  for i in range (len(target_word)):
     if guess[i] == target_word[i]:
      output = output +"🟩" 
     elif guess[i] in target_word:
      output = output + "🟨"
     else:
      output = output + "⬜"
  print(output)


  
  if guess ==  target_word:
   print("Yeah, you got it!")
   break