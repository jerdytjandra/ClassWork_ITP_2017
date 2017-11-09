print("These are the languages I would like to learn:")
languages = ["hebrew", "french", "sumeria", "spanish", "sanskrit"]
print(languages)

message1 ="I would like to learn the " + languages[0].title() + " language."
print("\n" + message1)

language_removed="sanskrit"
print("\n" +"language removed:")
print(language_removed.title())

language_removed1="french"
print("\n" + "another language removed:")
print(language_removed1.title())

languages.remove("french")
print("\n" + "languages left:")

languages.pop(-1)
print(languages)

language_add="mandarin"
print("\n"  + "language added:")
languages.append("mandarin")
print(language_add.title())
print(languages)

languages.reverse()
print(languages)

languages.append("japanese")
print(languages)

languages.insert(2, "malay")
print(languages)

del languages[2]
print(languages)
