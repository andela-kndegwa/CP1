"""
	Commands:
		quit
	Options:
		-h, --help  Show this screen and exit
		--version  Show version
"""

from docopt import docopt, DocoptExit
import cmd


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def introduction():
    print("#" * 160)
    print("#" * 160)
    print("Class Attendance Register: This program aids in checking in students ")
    print("in and out of class and also stores basic information about the students ")
    print("and the classes")
    print(__doc__)


class ClassRegister(cmd.Cmd):
    prompt = "<class_register>"

    # Student Commands
    # This command creates a new student in the database and generate an id
    # for the student
    @docopt_cmd
    def do_student_add(self, arg):
        """Usage: student_add <firstname> <lastname>"""
        print(arg)

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        print("Goodbye! ")
        exit()

if __name__ == "__main__":
    introduction()
    ClassRegister().cmdloop()
