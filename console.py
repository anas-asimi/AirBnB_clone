#!/usr/bin/python3
""" console.py """
import cmd
import sys
from models.base_model import BaseModel
from models import storage, listOfClasses


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand """

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, line):
        """ Method to exit the console"""
        return True

    def do_EOF(self, line):
        """ Handles EOF to exit program """
        print()
        return True

    def emptyline(self):
        """ Overrides the emptyline method """
        pass

    def do_create(self, line):
        """ Handles to create command """

        if not line:
            print("** class name missing **")

        if line == "BaseModel":
            my_model = BaseModel()
            print(my_model.id)
            my_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Handles to show command """

        if not line:
            print("** class name missing **")
            return

        className = line.split()[0]
        if className not in listOfClasses:
            print("** class doesn't exist **")
            return

        if len(line.split()) < 2:
            print("** instance id missing **")
            return

        id = line.split()[1]
        all_objs = storage.all()
        for value in all_objs.values():
            if id == value.id:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """ Handles to destroy command """

        if not line:
            print("** class name missing **")
            return

        className = line.split()[0]
        if className not in listOfClasses:
            print("** class doesn't exist **")
            return

        if len(line.split()) < 2:
            print("** instance id missing **")
            return

        id = line.split()[1]
        all_objs = storage.all()
        for key, value in all_objs.items():
            if id == value.id:
                del all_objs[key]
                return
        print("** no instance found **")

    def do_all(self, line):
        """ Handles to all command """

        className = '' if not line else line.split()[0]

        all_objs = storage.all()
        for key, value in all_objs.items():
            if className == '':
                print(value)
            elif className in key:
                print(value)

    def do_update(self, line):
        """ Handles to update command """

        if not line:
            print("** class name missing **")
            return

        className = line.split()[0]
        if className not in listOfClasses:
            print("** class doesn't exist **")
            return

        if len(line.split()) < 2:
            print("** instance id missing **")
            return
        id = line.split()[1]

        if len(line.split()) < 3:
            print("** attribute name missing **")
            return
        attribute = line.split()[2]

        if len(line.split()) < 4:
            print("** value missing **")
            return
        value = line.split()[3].replace('"', '')

        all_objs = storage.all()
        for key, value in all_objs.items():
            if id == value.id and className == value.__class__.__name__:
                valueType = type(all_objs[key][attribute])
                all_objs[key][attribute] = valueType(value)
                return
        print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
