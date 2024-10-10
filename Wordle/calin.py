target_word = 'carve'

number_of_rounds = 6
word_file = open('words.txt',"r")
word_list=[]
next_word = "XX"
while next_word != '':
  next_word = word_file.readline().strip()
  if next_word != "":
    word_list.append(next_word)

for round in range(number_of_rounds):
  print("round:",round + 1)
  guess = input('please enter a guess : ')
  
  output = ''
  while guess not in word_list:
   print("your guess is invalid")
   guess = input("please enter a guess ")
  for i in range(len(target_word)):
    if guess[i]==target_word[i]:
      output = output+'🟩'
    elif guess[i] in target_word:
      output = output + '🟨'
    else:
      output = output + '⬜'
  print(output)
  if guess == target_word:
    print("you've won")
    break