from tkinter import *
from tkinter import messagebox
import webbrowser


""" Funktsioon võtab sisse listi, kus esimesel kohal on tõlgitav sõna ja teisel kohal sihtkeel. Sihtkeele
    vaikeväärtus on eesti keel. Kui sisendit ei leita, siis küsitakse kasutajalt, kas ta soovib avada Google Translate'.

    Tööpõhimõte:
    Funktsiooni tõlkeosa võib jagada kaheks.
     Esimene osa otsib üks-ühest vastet: kasutaja sisendit võrreldakse sõnastiku võtmega ja kuvatakse vaste.
     Teine osa pöörab sõnastiku ümber, tõlgib kasutaja sisendi (vaste leidmisel) inglisekeelseks ja sealt edasi
     soovitud keelde.

     Integreerimine:
     - Kui funktsiooni kasutada ilma ülemfunktsioonita, siis peab 'dict_flag = False' leiduma selles .py failis.
     - Kui funktsioonil on olemas ülemfunktsioon, siis peab "dict_flag = False" olema ülemfunktsioonis koos kõigi
     sõnastikega.

     Toetatud sisendid:
     et, de, en, fr, it, es , de
     NB! Võib kasutada ka sõnastike originaalnimesid (dict_et_en).

     Näide väljakutsumisest:
     getTranslation(["fork", "it"])"""


global dict_flag
global dict_et_en, dict_en_et
global dict_en_de, dict_de_en
global dict_en_fr, dict_fr_en
global dict_en_it, dict_it_en
global dict_en_es, dict_es_en

dict_flag = False

root = Tk()
root.title("Sõnastik")
root.geometry("200x200")
x_scrollbar = Scrollbar(root, orient=HORIZONTAL)
x_scrollbar.pack(side=BOTTOM, fill=X)
y_scrollbar = Scrollbar(root)
y_scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
x_scrollbar.config(command=listbox.xview)
y_scrollbar.config(command=listbox.yview)


def read_in(database, dict_1, dict_2):
    global dict_flag
    if database == "en_et_words.txt":
        f = open(database, encoding="UTF8")
    else:
        f = open(database, encoding="ISO-8859-1")
    for line in f:
        line = line.strip("\n").replace("[Verb]", "")\
                               .replace("[Noun]", "")\
                               .replace("[Adjective]", "")\
                               .replace("[Adverb]", "")\
                               .replace("(f)", "")\
                               .replace("(m)", "")\
                               .lower()\
                               .split("\t")
        if len(line) != 2:
            continue
        dict_1[line[0]] = line[1]
        dict_2[line[1]] = line[0]
    f.close()
    dict_flag = True
    return dict_1, dict_2

# Järgnev on töö optimeerimieks, et iga kord ei peaks tekstifaile uuesti lugema.
if not dict_flag:
    dict_et_en, dict_en_et = {}, {}
    dict_en_de, dict_de_en = {}, {}
    dict_en_fr, dict_fr_en = {}, {}
    dict_en_it, dict_it_en = {}, {}
    dict_en_es, dict_es_en = {}, {}

    dict_en_et, dict_et_en = read_in("en_et_words.txt", dict_en_et, dict_et_en)
    dict_en_de, dict_de_en = read_in("en_de_words.txt", dict_en_de, dict_de_en)
    dict_en_fr, dict_fr_en = read_in("en_fr_words.txt", dict_en_fr, dict_fr_en)
    dict_en_it, dict_it_en = read_in("en_it_words.txt", dict_en_it, dict_it_en)
    dict_en_es, dict_es_en = read_in("en_es_words.txt", dict_en_es, dict_es_en)

    et, de, es, fr, it = dict_en_et, dict_en_de, dict_en_es, dict_en_fr, dict_en_it

    en = et

    available_dictionaries = [dict_et_en, dict_de_en, dict_fr_en, dict_it_en, dict_es_en, et, de, es, fr, it]

    universal_dict = []

def direct_match(input, dictionary):
    if input in dictionary:
        output = dictionary[input]
        listbox.insert(END, output + " | " + input)
        return True


def non_direct_match(input):
    for dictionary in available_dictionaries:
        for key in dictionary:
            if input.lower() in key:
                pre_output = key.strip().split(", ")
                for _ in pre_output:
                    if len(input) == _ or input in _[0:len(input)]:
                        universal_dict.append(dictionary[key])


def getTranslation(input):
    if len(input) > 1:
        dictionary_for_url = input[1]
        try:
            dictionary = eval(input[1])
        except:
            print("Dictionary not available")
            if messagebox.askyesno("Ended up in Sahara...", "Tundmatu sihtkeel."
                                                            " Kutsun abiväed? (Google Translate?)"):
                webbrowser.open_new_tab("https://translate.google.ee/#auto/" + input[1] + "/" + input[0])
            return
    else:
        dictionary = et

    input = input[0]
    listbox_ = False

    if input in dictionary:
        print("Using direct match")
        direct_match(input, dictionary)
        listbox.pack(side=LEFT, fill=BOTH, expand=1)
        root.mainloop()
        return
    else:
        print("Using non-direct match")
        non_direct_match(input)
        for word in universal_dict:
            if dictionary_for_url != "en":
                if direct_match(word, dictionary):
                    listbox_ = True
            else:
                try:
                    listbox.insert(END, word + " | " + dictionary[word])
                    listbox_ = True
                except KeyError:
                    continue

        if listbox_:
            listbox.pack(side=LEFT, fill=BOTH, expand=1)
            root.mainloop()
            return

    print("Word not in dictionary")
    if messagebox.askyesno("Ended up in Sahara...", "Vaste leidmine ebaõnnestus, sissekanne puudub sõnastikust!"
                                                    " Kutsun abiväed? (Google Translate?)"):
        webbrowser.open_new_tab("https://translate.google.ee/#auto/" + dictionary_for_url + "/" + input)
