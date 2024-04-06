my_string = input("I want to ride my bicycle ")
print(len("I want to ride my bicycle "))#Почему-то, если пробовать вывести длинну...
#именно my_string, он выдает 1, а не 26, поэтому и придумывал костыли
print(input(my_string))
my_string = "I want to ride my bicycle"
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ""))
print(my_string[0])
print(my_string[-1])
