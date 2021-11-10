separator = 40 * "-"
TEXTS = ['''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
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

#Dict s daty o uživatelech
users = {"bob":"123", "ann":"pass123", "mike":"password123","liz":"pass123"}
#Pomocí if zkontrolujeme, zda se jméno nachází v dict users.
user_name = input("User name: ")
if (user_name in users.keys()) == True:
    pass
else:
    print("Your user name isn't in our database.")
    quit()
#Poté zkontrolujeme zda se heslo zadané uživatelem shoduje s hodnout klíče, který nám definuje user_name.
user_pass = input("Password: ")
if users.get(user_name) == user_pass:
    pass
else:
    print("Incorrect password.")
    quit()
#Oddělovač
print(separator)
#Výpis všech dostupných textů, a jejich čísla pro volbu.
print(f"Welcome to the app {user_name}.")
print(f"We have {len(TEXTS)} texts to be analyzed.")
#Oddělovač
print(separator)
if input("Do you want to check what is inside of them? (Write y for yes or n for no) :") == "y":
    c = 1
    for i in TEXTS:
        print(f"TEXT no. {c}")
        print(i)
        c +=1
#Oddělovač
print(separator)
#Kontrola zda uživatel nezadal číslo větší než kolik máme textů, a nebo zda-li nezadal jiný znak než int.
try:
    user_choice = int(input(f"Enter a number between 1 and {len(TEXTS)} to select: "))
    #Oddělovač
    print(separator)
except:
    print("This is not a number.")
    quit()

if user_choice > len(TEXTS) or user_choice < 1:
    print(f"You can choose only numbers between 1 to {len(TEXTS)}. You entered number {user_choice}.")
    quit()


#Tato smyčka filtruje slova v textu od čehokoliv co není číslo nebo písmeno, a řadí je do listu words_list. Pokud narazí na prázdný string "", tak ho přeskočí, a jde na další slovo.
words_list = []
for i in TEXTS[user_choice - 1].split(" "):
    if i == "":
        continue
    i = ''.join(filter(str.isalnum, i))
    words_list.append(i)

#Proměnné určené pro výpis informací o textu uživateli. 
titlecased_words = []
uppercase_words = []
lowercase_words = []
numeric_strings = []
numbers_sum = 0

#Smyčka postupně projíždí slova z listu words_list, a zjišťuje kam je má zařadit.
for i in words_list:
    if i.isnumeric() == True:
        numeric_strings.append(i)
        numbers_sum += int(i)
    if i.istitle() == True:
        titlecased_words.append(i)
    if i.isupper() == True and i[0].isdigit() == False:
        uppercase_words.append(i)
    if i.islower() == True:
        lowercase_words.append(i)

#Výpis všech hodnot.
print(f"There are {len(words_list)} words in the selected text.")
print(f"There are {len(titlecased_words)} titlecase words.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers is {numbers_sum}.")

#Stanovení defaultní nulové hodnoty pro klíče všech různých délek slov, které se v textu nacházejí.
word_len_dict = dict()
for i in words_list:
    word_len_dict[str(len(i))] = 0
#Proměnné pro automatické zarovnávání grafického zobrazení.
most_letters = 0
longest_num = 0

#Smyčka vybere 1 slovo z listu words_list, zjistí jeho délku, a podle ní k jakému klíči délka patří, a následně k hodnotě klíče přičte 1, a novou hodnotu aktualizuje.
#Tímto způsobem projde všechny slova z listu words_list.
#Takto zjistím kolik slov určité délky se v listu words_list nachází, a budu je moct graficky zobrazit.
for i in words_list:
    c = word_len_dict.get(str(len(i)))
    c += 1
    #Updatuju hodnotu po každém přičtení 
    word_len_dict[str(len(i))] = c
    #Zjišťuji jaká délka slov má nejvíce písmen, kvůli zarovnání hvězd.
    if c > most_letters:
        most_letters = c
    #Zjišťuji který číslo má nejvíc číslíc, kvůli zarovnání řady čísel označující délky slov. Pokud má nejdelší číslo 2 číslice, přidám 1 mezeru před čísla co mají jen 1 číslici.
    if c > longest_num:
        longest_num = c

#Zde seřazuji délky slov od nejkratší po nejdelší, aby graf ukazoval hodnoty vzsetupně.
keys_list = []
for i in word_len_dict.keys():
    keys_list.append(int(i))
keys_list = sorted(keys_list)

#Oddělovač
print(separator)
#Délka slov | kolikrát se v textu objevuje 1 slovo = 1 hvězda | Počet kolikrát se v textu objevuje číslicí.
print("LEN| OCCURENCES |NR.")
#Oddělovač
print(separator)

#Grafické zobrazení kolik slov určité délky se v textu nachází.
for i in keys_list:
    #Výskyt každého slova určité délky značí 1 hvězda
    x = int(word_len_dict.get(str(i))) * "*"
    #Tato proměnná zarovnává hvězdy podle proměnné most_letters. Od proměnné most_letters(která značí délku slova s největším výskytem v textu) odečte délku ostatních slov, a potom vynásobí
    #rozdíl * " " (prázdná mezera), a vyplní tak místo v grafu, a vše tím zarovná.
    spaces = (most_letters - int(word_len_dict.get(str(i)))) * " "
    #Tato proměnná zarovnává seznam, podle toho kolik má nejdelší číslo číslic. Pokud má nejdelší číslo 2 číslice, přidám 1 mezeru před čísla co mají jen 1 číslici.
    first_space = (len(str(longest_num)) - len(str(i)))  * " "
    print(f" {first_space}{str(i)}|{x}{spaces} |{int(word_len_dict.get(str(i)))}")