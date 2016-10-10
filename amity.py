#!/usr/bin/env python
"""
T.I.A -This is Amity!
Amity is a room allocation system that helps you allocate rooms to people at random.
Usage:
    create_room (L|O) <room_name>...
    add_person <first_name> <last_name> (F|S) [<wants_space>]
    reallocate_person <employee_id> <new_room_name>
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
import cmd
from docopt import docopt, DocoptExit
from Amity.ui import enter_amity


def args_cmd(func):
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


class Interactive_Amity(cmd.Cmd):

    prompt = '(amity)===>'

    @args_cmd
    def do_create_room(self):
        print("This will create a room.")

    @args_cmd
    def do_(self):
        print("This will add a person")


try:
    if __name__ == '__main__':
        start()
        Interactive_Amity().cmdloop()
except KeyboardInterrupt:
    print('Amity says Goodbye!')
