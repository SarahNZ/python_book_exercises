# while loop
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

##########################################################################

# for loop (code is much easier to read and maintain

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max': # Will skip adding 'MAX' to upper names
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)
    # Don't need to increment the index as we do in while loops

print(upper_names)