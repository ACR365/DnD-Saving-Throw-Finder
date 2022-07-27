import requests
import json
import pprint

def spell():
    BASE_URL = 'https://www.dnd5eapi.co/api/spells/'
    saving_throws = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    type_of_attack = ["melee attack", "ranged attack"]


    title = "Welcome to the Spell Saving Throw Indictator"
    info = "In this program, you insert a cantrip or spell and we tell you if:\n1)they need to do a saving throw (Intelligence, Strength, etc.)\n2)You have to do an action (ranged, melee)"

    print(title + '\n\n' + info)
    spell_name = str(input("Enter spell here: "))

    spell_name = spell_name.lower()
    spell_name = spell_name.replace(" ", "-")

    SPELL_URL = BASE_URL + spell_name
    response = requests.get(SPELL_URL).json()

    description = response['desc']

    print("------------------------------------------------------------------------------")
    print("Description of Spell or Cantrip")
    pprint.pprint(description)
    print("------------------------------------------------------------------------------")

    saving_throw = ""
    attack_type = ""
    for d in description:
        d = d.lower()
        for s in saving_throws:
            if s in d:
                saving_throw = s
                break
    
        if saving_throw == "":
            for t in type_of_attack:
                if t in d:
                    attack_type = t
                    break
            
            if attack_type == "":
                print("The spell or cantrip does not require a saving throw or is a type of attack")
            else:
                print(attack_type)
        else:
            print(saving_throw)

spell()



        




