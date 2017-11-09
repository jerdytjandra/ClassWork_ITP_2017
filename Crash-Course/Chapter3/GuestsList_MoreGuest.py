guests=["x", "y", "z"]
print(guests)

message1="Hey " + guests[0].title() + "." + " Would you like to have dinner with me?"
print(message1)

message2="Hey " + guests[1].title() + "." + " Would you like to have dinner with me?"
print(message2)

message3="Hey " + guests[2].title() + "." + " Would you like to have dinner with me?"
print(message3)

guest_who_cannot_come="z"
print("\n" + guest_who_cannot_come.title())

guests.pop()
print(guests)

guests.append("p")
print(guests)

message_1="Hey " + guests[0].title() + "." + " Would you like to have dinner with me?"
print("\n" + message_1)

message_2="Hey " + guests[1].title() + "." + " Would you like to have dinner with me?"
print(message_2)

new_message="Hey " + guests[0].title() + ", " + guests[1].title() + ",and " + guests[2].title() + "." + " I have found a larger table."
print(new_message)

guests.insert(0, "a")
print(guests)

guests.insert(2, "b")
print(guests)

guests.insert(5, "c")
print(guests)

message9="Hey " + guests[0].title() + "." + " Would you like to have dinner with me?"
print(message9)

message8="Hey " + guests[1].title() + "." + " Would you like to have dinner with me?"
print(message8)

message7="Hey " + guests[2].title() + "." + " Would you like to have dinner with me?"
print(message7)

message6="Hey " + guests[3].title() + "." + " Would you like to have dinner with me?"
print(message6)

message_9="Hey " + guests[4].title() + "." + " Would you like to have dinner with me?"
print(message_9)

message_8="Hey " + guests[5].title() + "." + " Would you like to have dinner with me?"
print(message_8)

print("\nGuys," + " sorry my table is available only for 2 people.")

guests.pop(3)
note3="I am very sorry " + guests[3].title() + " I cannot invite you to dinner."
print("\n" + note3)
print(guests)

guests.pop(2)
note2="I am very sorry " + guests[2].title() + " I cannot invite you to dinner."
print("\n" + note2)
print(guests)

guests.pop(0)
note1="I am very sorry " + guests[1].title() + " I cannot invite you to dinner."
print("\n" + note1)
print(guests)

guests.pop(1)
note0="I am very sorry " + guests[0].title() + " I cannot invite you to dinner."
print("\n" + note0)
print(guests)


