# 1
first_name = input("What is your first name? ")
second_name = input("What is your middle name? ")
third_name = input("What is your last name? ")
print(f"{first_name[0]}{second_name[0]}{third_name[0]}")

# 2
course_name = input("Course: ")
department = course_name[0:2]
number = course_name[2:]
print("Department:", department)
print("Number:", number)

# 3
phrase = input("Give me a phrase: ")
waldo_search = phrase.find('Waldo')
if waldo_search >= 0:
    print("Found Waldo")
else:
    print("No Waldo")

# 4
email_ad = input("What is your email address? ")
at_sign = email_ad.find('@')
print(email_ad[at_sign + 1:])

# 5
sentence = ""
while True:
    if sentence.startswith("This") and sentence.endswith("that!"):
        print("Done!")
        break
    else:
        sentence = input("Sentence: ")

# 6
name = input("What is your name? ")
len_name = len(name)
for i in range(len_name):
    print(name[-i - 1])