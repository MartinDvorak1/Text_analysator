TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US and 30N the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

slovnik_poctu = {"words in the selected text.": 0,
                 "titlecase words.": 0,
                 "uppercase words.": 0,
                 "lowercase words.": 0,
                 "numeric strings.": 0,
                 "The sum of all the numbers": 0
                 }

user_details = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = input("username:")
password = input("password:")
number_of_texts = 3
sep = "-" * 40
print(sep)

if user in user_details:
    if user_details.get(user) == password:
        print("Welcome to the app, ", user)
        print(f"You have {number_of_texts} texts to be analyzed.")
        print(sep)
        selected_text = input(f"Enter a number btw. 1 and {number_of_texts} to select:")
        if not selected_text.isnumeric():
            print(f"{selected_text} is not a number!")
            exit()
        elif (int(selected_text) - 1) not in range(number_of_texts):
            print(f"{selected_text} is not btw. 1 and {number_of_texts}.")
            exit()
        else:
            cista_slova = [slovo.strip("@{}&~ˇ^˘°˛`„´˝÷<>*,.()#đ“\n") for slovo in
                           TEXTS[int(selected_text) - 1].split(" ")]

            for index in range(len(cista_slova)):
                if int(len(cista_slova[index])) != 0:
                    if cista_slova[index].isupper() and cista_slova[index].isalpha():
                        slovnik_poctu["uppercase words."] = slovnik_poctu.get("uppercase words.") + 1
                    elif cista_slova[index][0].isupper():
                        slovnik_poctu["titlecase words."] = slovnik_poctu.get("titlecase words.") + 1
                    elif cista_slova[index][0].islower():
                        slovnik_poctu["lowercase words."] = slovnik_poctu.get("lowercase words.") + 1
                    elif cista_slova[index].isnumeric():
                        slovnik_poctu["numeric strings."] = slovnik_poctu.get("numeric strings.") + 1
                        slovnik_poctu["The sum of all the numbers"] = slovnik_poctu.get(
                            "The sum of all the numbers") + int(cista_slova[index])
                else:
                    cista_slova.pop(index)
                    continue
        slovnik_poctu["words in the selected text."] = int(len(cista_slova))

        # tisk vypisu statistiky
        print(sep)
        for klic in slovnik_poctu.keys():
            if klic != "The sum of all the numbers":
                print(f"There are {slovnik_poctu[klic]} {klic}")
            else:
                print(klic, slovnik_poctu[klic])

        set_vyskytu = set()
        slovnik_vyskytu = {}
        for slovo in cista_slova: set_vyskytu.update([len(slovo)])
        slovnik_vyskytu = dict.fromkeys(set_vyskytu, 0)

        for slovo in cista_slova:
            slovnik_vyskytu[len(slovo)] += 1

        # tisk grafu
        print(f'''{sep}
LEN|  OCCURENCES  |NR.
{sep}''')

        max_value = max(slovnik_vyskytu.values())

        for i in slovnik_vyskytu.keys():
            if max_value > 14:
                graph = "*" * slovnik_vyskytu[i] + " " * (max_value - slovnik_vyskytu[i])
            else:
                graph = "*" * slovnik_vyskytu[i] + " " * (14 - slovnik_vyskytu[i])
            if i < 10:
                print(f"{i}  |{graph}|{slovnik_vyskytu[i]}")
            else:
                print(f"{i} |{graph}|{slovnik_vyskytu[i]}")

    else:
        print("Password is not correct!")
        exit()
else:
    print("Unexisting user!")
    exit()
