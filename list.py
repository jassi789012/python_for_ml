# expences = [2200, 2350, 2600, 2130, 2190]

# print("dollars you spent extra compare to January ",expences[1] - expences[0])

# print("your total expense in first quarter", expences[0] + expences[1] + expences[2])

# print("Did I spent 2000$ in any month? ", 2000 in expences)

# expences.append(1980)

# print(expences)

# expences[3] = expences[3] + 200

# print(expences)


heros=['spider man','thor','hulk','iron man','captain america']

# length of list
print(heros.__len__())

# adding black panther at the end of the list
heros.append('black panther')
print(heros)

# removing black panther from last and adding it after hulk
heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)

#  removing thor and hulk from list and replacing them with doctor strange
heros[1:3] = ['doctor strange']
print(heros)

# Sorting the heros list in alphabetical order
heros.sort()
print(heros)

