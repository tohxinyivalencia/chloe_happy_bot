print("Title of program: Happy bot")
print()
while True:
  description = input("Could you describe how you feel with words like sad, happy or tired?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("don't let yesterday's sadness bring you down. this too shall pass. stay positive!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("that's awesome! stay happy and cheerful!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("please do get some rest and sleep well.")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". Even so, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Remember -  "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()


