def load_people(filename):
    try:
        with open(filename, 'r') as f:
            file_read = f.readlines()
        for person in file_read:
            person = person.split()
            print(person)
	print("Finished adding people")
        return True
    except Exception:
        message = "Error while adding people to system"
    return message
load_people('sample.txt')