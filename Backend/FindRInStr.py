Stg = "Hello! my friend , How are you?!"

section = Stg[10:30]
for word in section.split():
    if 'r' in word:
        print(word)