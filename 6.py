def Guess(num_1, num_2, choice):   
  result = 0
  if choice == '1':
      result = num_1 + num_2
      print("What is",num_1, "+", num_2, "?")
      ans = int(input(">> "))
      if(result==ans):
       print("Good Job! The answer is correct")

  elif choice == '2':
      result = num_1 - num_2
      print("What is",num_1, "-", num_2, "?")
      ans = int(input(">> "))
      if(result==ans):
       print("Good Job! The answer is correct")

  elif choice == '3':
      result = num_1 * num_2
      print("What is",num_1, "X", num_2, "?")
      ans = int(input(">> "))
      if(result==ans):
       print("Good Job! The answer is correct")

  elif choice == '4':
      result = num_1 / num_2
      print("What is",num_1, "/", num_2, "?")
      ans = int(input(">> "))
      if(result==ans):
       print("Good Job! The answer is correct")

  elif choice == '5':
      result = num_1 % num_2
      print("What is",num_1, "%", num_2, "?")
      ans = int(input(">> "))
      if(result==ans):
       print("Good Job! The answer is correct")
  else: 
    print("Oops! The answer is not correct :(")
    print("The correct answer is : ",result)