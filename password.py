from termcolor import colored
import random
import time

time.sleep(0.5)

print(colored('\n'+'                 **************************************','green'))
print(colored('                 **************************************','green'))
print(colored('                 **************************************','green'))
print(colored('                 **************************************','white'))
print(colored('                 *************** AKINGA ***************','white'))
print(colored('                 **************************************','white'))
print(colored('                 **************************************','red'))
print(colored('                 **************************************','red'))
print(colored('                 **************************************','red'))

print(colored('\n'+'for name + emoji and number type 1','blue'))
print(colored('\n'+'for name + emoji + number type 2','red'))
print(colored('\n'+'for name emoji in choice 3','cyan'))


start = input(colored('\n'+'Enter : ','magenta'))
emogi_list = ['!','@','#','$','%','^','*','()','+']


file = open('password.lst','w')

def password_for_name_and_number_emoji(num,target):
    for i in range(1,num):
        number = random.randrange(1,100000)
        number = str(number)
        password_Emoji = random.choice(emogi_list)
        
        print(colored(target + number , 'magenta'))
        print(colored(target+ password_Emoji , 'red'))

        password_emogi = target + password_Emoji
        password_Number = target + number
        file.writelines(password_emogi + '\n')
        file.writelines(password_Number + '\n')


def password_for_name__number_emoji(num,target):
    for i in range(1,num):
        number = random.randrange(1,100000)
        number = str(number)
        password_Emoji = random.choice(emogi_list)
        
        print(colored(target + password_Emoji + number , 'magenta'))

        password_emogi = target + password_Emoji
        password_Number = number
        file.writelines(password_emogi + password_Number +'\n')


def password_choice(target,num):
    for ei in range(1,num):
        name_list = list(target) 
        name_list_len = len(name_list)
        name_list_len = int(name_list_len - 1)
        f = []
        for i in range(0,name_list_len):
            i = int(i)
            f.append(i)
        password_Emoji = random.choice(emogi_list)
        name_chenger = random.choice(name_list)
        number_chenger = random.choice(f)
        number_chenger2 = random.choice(f)
        number_chenger = int(number_chenger)
        number_chenger2 = int(number_chenger2)
        name_list[number_chenger] = name_chenger 
        name_list[number_chenger2] =  password_Emoji
        e = ''.join(name_list)
        print(colored(e,'red'))
        file.writelines(e+'\n')

if start == '1':
    num = int(input(colored('Enter the number for pass : ','yellow')))
    target = input('Enter youre Target name : '+'\n')
    password_for_name_and_number_emoji(num,target)
elif start == '2':
    num = int(input(colored('Enter the number for pass : ','yellow')))
    target = input('Enter youre Target name : '+'\n')
    password_for_name__number_emoji(num,target)
elif start == '3':
    num = int(input(colored('how meny number password : ','yellow')))
    target = input(colored('Enter youre name : ','green'))
    password_choice(target,num)