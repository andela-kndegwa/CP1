"""
TIA
Usage:
    create_room (L|O) <room_name>...
<<<<<<< HEAD
    add_person <name> <person_type> <wants_accommodation>
=======
    add_person <first_name> <last_name> (F|S) [<wants_space>]
>>>>>>> af7e76160ec0b36c03fad1cbc98230c89bee7251
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
from ui import enter_amity
from amity import Amity
<< << << < HEAD
import click


def parse(func):
== == == =


amity = Amity()


def docopt_cmd(func):
>>>>>> > af7e76160ec0b36c03fad1cbc98230c89bee7251
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

    prompt = '(amity)===>'

    @parse
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        for r in args['<room_name>']:
            click.secho(amity.create_room(args['<room_type>'], r), fg='red')

    @parse
    def do_add_person(self, args):
        """Usage: add_person <person_name> <person_type> <wants_accommodation>"""
        click.echo(amity.add_person(args['<person_name>'], args[
            '<person_type>'], args['<wants_accommodation>']))

    @parse
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_id> <room_name>"""

    @parse
    def do_print_allocations(self, args):
        """Usage: print_allocations """
        click.secho(amity.print_allocations())

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        for r in args['<room_name>']:
            print(amity.create_room(args['<room_type>'], r))

    @docopt_cmd
    def do_(self):
        print("This will add a person")


if __name__ == '__main__':
    try:
        start()
        Interactive_Amity().cmdloop()
    except KeyboardInterrupt:
        print('Amity says Goodbye!')
