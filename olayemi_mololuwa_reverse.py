i = 0
while i < 1:
     reverse_string = input("Please Enter Your String: ")
     if reverse_string == 'quit' or reverse_string == 'q' or reverse_string == 'Quit':
          i = 1
     else:
          for i in range(len(reverse_string)-1,-1,-1):
               print(reverse_string[i], end = '')
     print("\n")