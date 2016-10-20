import os
import sys
import time
import click
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


def enter_amity():
    os.system('clear')
    print "Loading Amity...\\",
    syms = ['\\', '|', '/', '-']
    for _ in range(10):
        for sym in syms:
            sys.stdout.write("\b %s" % sym)
            sys.stdout.flush()
            time.sleep(0.04)
    click.secho("DONE!", bold=True)
    # Amity Pyfilget format begins here!
    time.sleep(0.9)
    click.secho('=' * 75, fg='cyan')
    click.secho('*' * 75, fg='yellow')
    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    cprint(figlet_format('AMITY', font='roman'),
           'cyan', attrs=['bold'])
    click.secho('*' * 75, fg='yellow')
    click.secho('=' * 75, fg='cyan')


def exit_bar():
    with click.progressbar(range(20000),
                           label=click.secho(
            '\t\t\tAMITY SAYS GOODBYE!',
                           blink=True, bold=True),
                           fill_char=click.style('  ', bg='cyan')) as prog_bar:
        for i in prog_bar:
            pass
