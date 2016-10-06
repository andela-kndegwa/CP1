#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This shows the usage and options that available for Amity room allocation app
Usage:
    amity allocaterooms
    amity viewallocations  [(-r <name_of_room>)]
    amity viewunallocated
    amity unallocate (-p <fname> <lname> -r <name_of_room>)
    amity reset
    amity (-s | --start)
    amity (-h | --help | --version)
Options:
    -s, --start  Starts the program.
    -h, --help  Shows a list of commands and their usage.
"""

# from Tkinter import Tk
# import tkFileDialog
import sys
import cmd
from docopt import docopt, DocoptExit
from Amity.ui import enter_amity
# from colorama import init, Fore, Back, Style
# from termcolor import cprint
# from pyfiglet import figlet_format
# from utils.FileParser import FileParser
# from db.DatabaseManager import DatabaseManager
# from utils.Allocations import Allocations
# from models.Rooms import Rooms
# from clint.textui import colored, puts


def parser(func):
    """compares args to determine if all have been entered in correct manner"""

    def fn(self, arg):
        try:
            # tries to compare entered commands against the doc
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The entered arguments don't match

            print('Sorry,you entered an invalid command')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Amity (cmd.Cmd):

    """Class overrides method parser so as to validate input.The input arguments
    are mapped to respective methods """

    prompt = '(Amity): '

    @parser
    def do_allocaterooms(self, arg):
        """Usage: allocate """

        # allocate_rooms(arg)

    def quit(self):
        self.root.destroy

    @parser
    def do_viewallocations(self, arg):
        """Usage: viewallocations [(-r <name_of_room>)]"""

        # view_allocations(arg)

    @parser
    def do_unallocate(self, arg):
        """Usage: unallocate (-p <fname> <lname> -r <name_of_room>)"""

        # unallocate(arg)

    @parser
    def do_viewunallocated(self, arg):
        """Usage: viewunallocated """

        # view_unallocated(arg)

    @parser
    def do_reset(self, arg):
        """Usage: reset """

        # reset(arg)

    def do_quit(self, arg):
        """Exit application."""

        print('Bye!')
        exit()


def start():
    enter_amity()

opt = docopt(__doc__, sys.argv[1:])


if opt['--start']:
    """starts application when -start is specified"""

    start()
    Amity().cmdloop()  # creates the REPL

print(opt)
