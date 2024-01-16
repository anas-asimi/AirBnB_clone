#!/usr/bin/python3
""" console.py """
import cmd
import sys
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage, listOfClasses


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand """

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def do_quit(self, line: str):
        """ Method to exit the console"""
        return True

    def do_EOF(self, line: str):
        """ Handles EOF to exit program """
        print()
        return True

    def emptyline(self):
        """ Overrides the emptyline method """
        pass

    def do_create(self, line: str):
        """ Handles to create command """

        if not line:
            print("** class name missing **")
            return

        className = line.split()[0]
        if className not in listOfClasses:
            print("** class doesn't exist **")
            return

        if className == "BaseModel":
            my_model = BaseModel()
            print(my_model.id)
            my_model.save()

        elif className == "User":
            my_model = User()
            print(my_model.id)
            my_model.save()

        elif className == "State":
            my_model = State()
            print(my_model.id)
            my_model.save()

        elif className == "City":
            my_model = City()
            print(my_model.id)
            my_model.save()

        elif className == "Amenity":
            my_model = Amenity()
            print(my_model.id)
            my_model.save()

        elif className == "Place":
            my_model = Place()
            print(my_model.id)
            my_model.save()

        elif className == "Review":
            my_model = Review()
            print(my_model.id)
            my_model.save()

        else:
            print("** class doesn't exist **")

    def do_show(self, line: str):
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

    def do_destroy(self, line: str):
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

    def do_all(self, line: str):
        """ Handles to all command """

        className = '' if not line else line.split()[0]

        all_objs = storage.all()
        for key, value in all_objs.items():
            if className == '':
                print(value)
            elif className in key:
                print(value)

    def do_update(self, line: str):
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

    def default(self, line: str):
        """ Handles to others commands """

        if re.match('[a-zA-Z]+\.all\(\)', line):
            className = line[0: line.find('.')]
            self.do_all(className)

        elif re.match('[a-zA-Z]+\.count\(\)', line):
            className = line[0: line.find('.')]
            counter = self.count(className)
            if type(counter) == int:
                print(counter)

        elif re.match('[a-zA-Z]+\.show\("\S+"\)', line):
            className = line[0: line.find('.')]
            id = line[line.find('(') + 1: len(line) - 1].replace('"', '')
            if id:
                self.do_show(' '.join([className, id]))
            else:
                print("** no instance found **")

        elif re.match('[a-zA-Z]+\.destroy\("\S+"\)', line):
            className = line[0: line.find('.')]
            id = line[line.find('(') + 1: len(line) - 1].replace('"', '')
            if id:
                self.do_destroy(' '.join([className, id]))
            else:
                print("** no instance found **")

    def count(self, className: str):
        """ count """
        if className not in listOfClasses:
            print("** class doesn't exist **")
            return

        counter = 0
        all_objs = storage.all()
        for key in all_objs.keys():
            if className in key:
                counter += 1
        return counter


if __name__ == "__main__":
    HBNBCommand().cmdloop()
