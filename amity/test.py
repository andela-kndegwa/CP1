import click


def do_load_people(args):
    try:
        with open(args, 'r') as f:
            file_read = f.readlines()
        for person in file_read:
            person = person.split()
            print(person)
        click.secho("FINISHED ADDING PEOPLE.", fg='red', bold=True)
    except Exception:
        print ("Error while adding people to system")


do_load_people('sample.txt')