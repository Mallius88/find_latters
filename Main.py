data = input()
letters_low = []
letters_up = []
for i in data:
    if i.isalpha():
        if i.lower() == i:
            letters_low.append(i)
        else:
            letters_up.append(i)
print(letters_low, letters_up, sep='\n')

