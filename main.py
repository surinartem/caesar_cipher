import math
//

def paint_wall(hight,wight,cover):
    num_of_cans = (hight*wight)/cover
    return (math.ceil(num_of_cans))
#
# test_hight = 2ascadfaewwd
# test_wight = 4
# coverage = 5

# print (f"Тебе надо {cans} банок, что б покрасить стену {test_wight} на {test_hight}")

def prime_checker(number):
    counter = True
    for i in range(2,number-1):
        if number % i == 0:
            counter = False
    if counter:
        print ("Число простое")
    else:
        print ("Число не простое")



def prime_checker(number):
    counter = True
    for i in range(2,number-1):
        if number % i == 0:def prime_checker(number):
    counter = True
    for i in range(2,number-1):
        if number % i == 0:def prime_checker(number):
    counter = True
    for i in range(2,number-1):
        if number % i == 0:def prime_checker(number):
    counter = True
    for i in range(2,number-1):
        if number % i == 0:

# n=int(input(" Введите число "))
# prime_checker(number = n)

alphaebt = ("а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я").split()

def encryp(messege,shift):
    result=[]
    for letter in messege:
        for j in range(len(alphaebt)):
        
            result.append(letter)

    return ("".join(result))


def decryp (messege, shift):
    result = []
    for letter in messege:
        for j in range(len(alphaebt)):
            if letter == alphaebt[j]:
                iter = j - shift
                result.append(alphaebt[iter])

        if letter not in alphaebt:
            result.append(letter)

    return ("".join(result))

def caesar(messege, shift, decriptoion):
    result = ""
    for letter in messege:
        if letter in alphaebt:
            position = alphaebt.index(letter)
            if decriptoion == "шифр":
                new_position = position + shift
                if new_position >= 33:
                    new_position = new_position - 33
            elif decriptoion == "расшифр":
                new_position = position - shift
            result += alphaebt[new_position]
        else:
            result+=letter
    print(f"Зашифрованный текст: {result}")

decriptoion = "шифр"
text = "юля варила борщ ээээ!"
# shift = 5
repit = 'да'
print(alphaebt.index("а"))
flag = True
while repit == "да":
    decriptoion = input("Напишите 'шифр' или 'расшифр':\n")
    text = input("Введите ваше сообщение:\n").lower()
    shift = int(input("Введите число сдвига: \n"))
    shift = shift%33
    # while flag :
    #     shift = int(input("Введите число сдвига: \n"))
    #     if shift/33 < 1:
    #         print(shift/33)
    #         flag = False
    #         caesar(text, shift, decriptoion)
    #     else:
    #         print("Число не превышает колличество символов в алфавите, введите еще раз")

    caesar(text, shift, decriptoion)
    flag = True
    # encryp_text=encryp(text,shift)
    # dencryp_text=decryp(text,shift)
    repit = input("Повторить ? да/нет\n")
print("Пока")

