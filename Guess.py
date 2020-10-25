#使用random.randint(开始，结束)，生成随机整数#     # 不能这样写文件注释，应该用三对引号。#符号用于语句后面的注释
import random                                 # 不要的空行要有
number = random.randint(1,99)
#利用函数input，提示用户输入数字#
message = "Please enter the number you guessed:\n"
message +="Enter 'quit' to end the program.\n"
guess = ""
k = 1
while guess != 'quit':     # 判断条件不好，有待改进
    guess = input(message)
    k = k+1
#输入quit结束游戏#
    if guess == 'quit':
        break
    if guess > str(number):
        print ("Too big ,please try again.")
    elif guess < str(number):
        print ("Too small ,please try again.")
    else:
        print("Congratulations! You guessed right.\nYou've guessed " + str(k) +" times.")
        break
