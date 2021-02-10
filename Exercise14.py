from sys import argv
script, user_name, name, password = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")

print("I'd like to ask you a few questions.")
print(f"Do you like my {script}?")
likes = input(prompt)
print(f"I heard that your password is {password} Can you repeat it please?")
password = input(prompt)
print(f"Where do you live {name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f""""
alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. 
And you have a {computer} computer with {password} as password. Nice.
""")