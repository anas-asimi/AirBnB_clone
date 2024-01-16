#!/usr/bin/python3
""" utils.py """
import json
from models import listOfClasses


def count(className: str, all_objs):
    """ count """
    if className not in listOfClasses:
        print("** class doesn't exist **")
        return
    counter = 0
    for key in all_objs.keys():
        if className in key:
            counter += 1
    return counter


def stringSpliter(args: str):
    """ string tokenizer """
    return json.loads(args.replace("'",'"').join(['[', ']']))
