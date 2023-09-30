from src.phonebook import Phonebook

phonebook = Phonebook()

# print(phonebook.get_names())
#
# print(phonebook.get_numbers())

# phonebook.add("Mariana", "(12)9999-8888")
print(phonebook.add("Mariana", "(12)9999-8888"))
# print(phonebook.lookup("Mariana"))
# print(phonebook.get_phonebook_reverse())
print(phonebook.delete("Mariana"))