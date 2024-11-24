print("WELCOME TO THE LOVE CALCULATOR!")
name1 = input("Enter Your Name: ")
name2 = input("Enter the name of your crush: ")
low_name1 = name1.lower()
low_name2 = name2.lower()
dig1 = low_name1.count("t") + low_name1.count("r") + low_name1.count("u") + low_name1.count("e") + low_name2.count("t")+low_name2.count("r")+low_name2.count("u")+low_name2.count("e")
dig2 = low_name1.count("l") + low_name1.count("o") + low_name1.count("v") + low_name1.count("e") + low_name2.count("l")+low_name2.count("o")+low_name2.count("v")+low_name2.count("e")

prsnt = dig1*10+dig2
if(prsnt<10 or prsnt>90):
    print(f"Your score is {prsnt}, you go together like coke and mentos.")
elif(prsnt>=40 and prsnt<=50):
    print(f"Your score is {prsnt}, you are alright together.")
else:
    print(f"Your score is {prsnt}")