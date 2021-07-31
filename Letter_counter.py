print("Hi,\nI am County and I'll help you count the number of a letters in a\nsentence/message.\nPlease enter your message and the letter you want to count.\nMake sure that you enter the message in the message region\nand the letter in the letter region.")
#asking the user to input the message
message = input( "Enter your message:  ")
#print(message) - this was to check if the code is working correctly
letter = input( "Input the letter:  " )
#print(letter)  - this was to check if the code is working correctly
count = message.count(letter)
print(f"The number of times\nthe letter you specified appeared\nin your message is: {count}")   
percent = (count/len(message))*100
print(f"The percentage of appearance\of the letter you specified is: {percent}") 
