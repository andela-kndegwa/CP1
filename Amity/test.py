first_names = []
last_names = []
person_type = []
wants_accomodation = []

f = open('sample.txt', 'r+')
for x in f.readlines():
    y = x.split()
    first_names.append(y[0])
    last_names.append(y[1])
    person_type.append(y[2])


print(first_names)
