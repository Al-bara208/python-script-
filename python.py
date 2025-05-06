name=input ("Full Name : ")
num=input("Enter the password : ")
if (name .isupper()):
 print ("You are successfully logged in")
else:
  print ("Please type the letters in Captal and try again")
  
  
print("\n")

num1=float(input("First number : "))
oper=input("Calculation : ")
num2=float(input("Number two : "))
 
if oper=="+":
  print(num1+num2)
elif oper=="-":
  print(num1-num2)
elif oper=="/":
  print(num1/num2) 
elif oper=="*":
  print(num1*num2)
else:
     print("Please type the number correctly")

print("\n")

text=input("Enter the sentence whose number of letters you want to know : ")
print(len(text))

print("\n")

txte=input("Enter two numbers to extract the larger number between them : ")

try:
    num1, num2 = map(float, txte.split())  
    print(f"The larger number is : {max(num1, num2)}")
except ValueError:
    print("Please enter two valid numbers separated by a space")

print("\n")

for char in input ("Enter the number or sentence you want to divide : "):  
   print(char)

print("\n")

num = input("Enter the number you want to know if it is odd or even : ")   
  
if num.isdigit():
    num = int(num) 
    print(f"{num}\t")
    
    if num % 2 == 0:
        print("That's an even number")
    else:
        print("That's an odd number")
else:
    print("Please enter a valid number!")



print("\n")

word = input("Enter a word to extract its first letter : ")

if len(word) > 0:
    print( word[0])
else:
    print("You did not enter any word : ")
    

word2 = input("Enter the word to extract its last letter : ")

if len(word2) > 0:
  print( word2[-1])
else:
  print("You did not enter any word")

print("\n")

user_input = input("Enter a word to extract the second, fourth, sixth, eighth and tenth letters : ")

if len(user_input) >= 10:
    print("The second letter is : ", user_input[1])
    print("The fourth letter is : ", user_input[3])
    print("The sixth letter is : ", user_input[5])
    print("The eighth letter is : ", user_input[7])
    print("The tenth letter is : ", user_input[9])
else:
    print("The entry contains less than 10 fields")


print("\n")

user_input = input("Enter the numbers you want to add to your list, separated by commas : ")
user_list = user_input.split(", ")
print(f"Here is your list: {user_list}")

