from tkinter import *
from tkinter import messagebox
import logging
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


def create_translation_window():
    global translation_listbox
    global translation_window
    translation_window = Tk()
    translation_window.title("Sõnastik")
    translation_window.geometry("200x200")
    x_scrollbar = Scrollbar(translation_window, orient=HORIZONTAL)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    y_scrollbar = Scrollbar(translation_window)
    y_scrollbar.pack(side=RIGHT, fill=Y)
    translation_listbox = Listbox(translation_window, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
    x_scrollbar.config(command=translation_listbox.xview)
    y_scrollbar.config(command=translation_listbox.yview)


def read_in(database, dict_1, dict_2):
    if database == ".\\Words_for_translator\\en_et_words.txt":
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
    return dict_1, dict_2

# Järgnev on töö optimeerimieks, et iga kord ei peaks tekstifaile uuesti lugema.

dict_et_en, dict_en_et = {}, {}
dict_en_de, dict_de_en = {}, {}
dict_en_fr, dict_fr_en = {}, {}
dict_en_it, dict_it_en = {}, {}
dict_en_es, dict_es_en = {}, {}

dict_en_et, dict_et_en = read_in(".\\Words_for_translator\\en_et_words.txt", dict_en_et, dict_et_en)
dict_en_de, dict_de_en = read_in(".\\Words_for_translator\\en_de_words.txt", dict_en_de, dict_de_en)
dict_en_fr, dict_fr_en = read_in(".\\Words_for_translator\\en_fr_words.txt", dict_en_fr, dict_fr_en)
dict_en_it, dict_it_en = read_in(".\\Words_for_translator\\en_it_words.txt", dict_en_it, dict_it_en)
dict_en_es, dict_es_en = read_in(".\\Words_for_translator\\en_es_words.txt", dict_en_es, dict_es_en)

et, de, es, fr, it = dict_en_et, dict_en_de, dict_en_es, dict_en_fr, dict_en_it

en = et

available_dictionaries = [dict_et_en, dict_de_en, dict_fr_en, dict_it_en, dict_es_en, et, de, es, fr, it]

universal_dict = []
translation_listbox = []


def direct_match(input_, dictionary):
    global translation_listbox
    if input_ in dictionary:
        output = dictionary[input_]
        if not translation_listbox:
            create_translation_window()
        translation_listbox.insert(END, output + " | " + input_)
        return True


def non_direct_match(input_):
    for dictionary in available_dictionaries:
        for key in dictionary:
            if input_.lower() in key:
                pre_output = key.strip().split(", ")
                for _ in pre_output:
                    if len(input_) == _ or input_ in _[0:len(input_)]:
                        universal_dict.append(dictionary[key])


def getTranslation(input_):
    global translation_listbox
    global translation_window

    input_ = input_[0].split()

    if len(input_) > 1:
        dictionary_for_url = input_[1]
        logging.info("dictionary for url: " + dictionary_for_url)
        try:
            dictionary = eval(input_[1])
            logging.info("dictionary= " + input_[1])
        except:
            logging.info("Dictionary not available")
            if messagebox.askyesno("Ended up in Sahara...", "Tundmatu sihtkeel."
                                                            " Kutsun abiväed? (Google Translate?)"):
                webbrowser.open_new_tab("https://translate.google.ee/#auto/" + input_[1] + "/" + input_[0])
            return
    else:
        dictionary = et

    input_ = input_[0]
    logging.info("input= " + input_)
    listbox_ = False

    if input_ in dictionary:
        logging.info("Using direct match")
        direct_match(input_, dictionary)
        translation_listbox.pack(side=LEFT, fill=BOTH, expand=1)
        translation_window.mainloop()
        return
    else:
        logging.info("Using non-direct match")
        non_direct_match(input_)
        for word in universal_dict:
            if dictionary_for_url != "en":
                if direct_match(word, dictionary):
                    listbox_ = True
            else:
                try:
                    if not translation_listbox:
                        if dictionary[word]:
                            create_translation_window()
                    translation_listbox.insert(END, word + " | " + dictionary[word])
                    listbox_ = True
                except KeyError:
                    continue
        if listbox_:
            translation_listbox.pack(side=LEFT, fill=BOTH, expand=1)
            translation_window.mainloop()
            return

    logging.info("Word not in dictionary")
    if messagebox.askyesno("Ended up in Sahara...", "Vaste leidmine ebaõnnestus, sissekanne puudub sõnastikust!"
                                                    " Kutsun abiväed? (Google Translate?)"):
        webbrowser.open_new_tab("https://translate.google.ee/#auto/" + dictionary_for_url + "/" + input_)
