#!/usr/bin/python3
""" console.py """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand """

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) '
    if not sys.__stdin__.isatty():
        prompt = ''
        
    def do_quit(self, command):
        """ Method to exit the console"""
        exit()
        
    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()
        
    def emptyline(self):
        """ Overrides the emptyline method """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
