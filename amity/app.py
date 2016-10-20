"""
TIA -This is Amity.
Usage:
    create_room (L|O) <room_name>...
    add_person <first_name> <last_name> <person_type> [accomodate=N]
    reallocate_person <identifier> <new_room_name>
    reallocate_unallocated <identifier> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename.txt]
    print_unallocated [--o=filename.txt]
    print_room <room_name>
    save_state [--db=sqlite_database]
    load_state <sqlite_database>
    (-i | --interactive)
Options:
    -h --help     Show this screen.
    -v --version
"""
import os
import click
import cmd
from docopt import docopt, DocoptExit
from ui import enter_amity
from amity import Amity
from db import database


amity = Amity()


def parse(func):
    """
    Essentially a decorator that simplifies the try/except block relays result
    of the docopt parsing to the called action.
    i.e @args_cmd thereafter.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # Throws an Invalid Command message when arguments
            # do not match what is outlined in the __doc__ string.
            msg = 'Invalid Command'
            print(msg)
            print(e)
            return

        except SystemExit:
            # Show help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def start():

    enter_amity()

    arguments = __doc__
    print(arguments)


amity = Amity()


class Interactive_Amity(cmd.Cmd):

    prompt = '(amity)===> '

    @parse
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>...
        """
        try:
            for r in args['<room_name>']:
                amity.create_room(args['<room_type>'], r)
        except Exception as e:
            print(e)
            click.secho(
                'Oops!An error occurred in running the command. Please try again',
                fg='red', bold=True)

    @parse
    def do_add_person(self, args):
        """Usage: add_person <first_name> <other_name> <person_type> <accomodate> """
        try:
            amity.add_person(args['<first_name>'],
                             args['<other_name>'], args['<person_type>'],
                             args["<accomodate>"])
        except Exception as e:
            print(e)
            click.secho(
                'Oops!An error occurred in running the command. Please try again', fg='red', bold=True)

    @parse
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_id> <room_name>"""
        amity.reallocate_person(args['<person_id>'], args['<room_name>'])

    @parse
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        amity.print_room(args['<room_name>'])

    @parse
    def do_print_allocations(self, args):
        """Usage: print_allocations """
        amity.print_allocations()

    @parse
    def do_print_unallocated(self, args):
        """Usage: print_unallocated """
        amity.print_unallocated()

    @parse
    def do_load_people(self, args):
        """Usage: load_people <filename>"""

        if os.path.exists(args['<filename>']):
            filename = args['<filename>']
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    person_details = line.split()
                    if len(person_details) == 3:
                        first_name = person_details[0]
                        other_name = person_details[1]
                        person_type = person_details[2]
                        accomodate = "N"
                        amity.add_person(first_name=first_name, other_name=other_name,
                                         person_type=person_type, accomodate=accomodate)
                    elif len(person_details) == 4:
                        first_name = person_details[0]
                        other_name = person_details[1]
                        person_type = person_details[2]
                        accomodate = person_details[3]
                        amity.add_person(first_name=first_name, other_name=other_name,
                                         person_type=person_type, accomodate=accomodate)
                    else:
                        print("An error occurred")
        else:
            click.secho('PLEASE PROVIDE A VALID FILE NAME.',
                        fg='red', bold=True)

    @parse
    def do_get_identifier(self, args):
        """ Usage: get_identifier <first_name> <last_name> """
        first_name = args['<first_name>']
        last_name = args['<last_name>']
        amity.get_identifier(first_name, last_name)

    @parse
    def do_reallocate_unallocated(self, args):
        """ Usage: reallocate_unallocated <person_id> <room_name> """
        amity.reallocate_unallocated(args['<person_id>'], args['<room_name>'])

    @parse
    def do_save_state(self, args):
        """ Usage: save_state """
        amity.save_state()

    @parse
    def do_load_state(self, args):
        """ Usage: save_state """
        try:
            amity.load_state()
            click.secho('Database successfully loaded onto the system', fg='green', bold=True)
        except Exception as e:
            print(e)
            click.secho('Oops!An error occurred. Please try again.', fg='red', bold=True)

    @parse
    def do_quit(self, args):
        """Usage: quit """
        with click.progressbar(range(20000),
                               label=click.secho(
                               '\t\t\tAMITY SAYS GOODBYE!', blink=True, bold=True),
                               fill_char=click.style('  ', bg='cyan')) as prog_bar:
            for i in prog_bar:
                pass
        exit()


if __name__ == '__main__':
    try:
        start()
        Interactive_Amity().cmdloop()
    except KeyboardInterrupt:
        with click.progressbar(range(20000),
                               label=click.secho(
                               '\t\t\tAMITY SAYS GOODBYE!', blink=True, bold=True),
                               fill_char=click.style('  ', bg='cyan')) as prog_bar:
            for i in prog_bar:
                pass
