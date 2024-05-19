#!/usr/bin/python3
"""
HBNB command interpreter
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args[0])()
        except NameError:
            print("** class doesn't exist **")
            return
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            instance = storage.all()[f"{args[0]}.{args[1]}"]
        except KeyError:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            instance = storage.all()[f"{args[0]}.{args[1]}"]
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        objects = storage.all()
        if args:
            try:
                objects = [
                    str(obj)
                    for obj in objects.values()
                    if obj.__class__.__name__ == args[0]
                ]
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            objects = [str(obj) for obj in objects.values()]
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            instance = storage.all()[f"{args[0]}.{args[1]}"]
            attr_name = args[2]
            attr_value = args[3]
            if attr_value.startswith('"') and attr_value.endswith('"'):
                attr_value = attr_value[1:-1]
            if '.' in attr_value:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass
            setattr(instance, attr_name, attr_value)
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program")

    def help_create(self):
        """Help for create command"""
        print("Creates a new instance of a class.")
        print("Usage: create <class name>")

    def help_show(self):
        """Help for show command"""
        print("Prints the string representation of an instance.")
        print("Usage: show <class name> <id>")

    def help_destroy(self):
        """Help for destroy command"""
        print("Deletes an instance.")
        print("Usage: destroy <class name> <id>")

    def help_all(self):
        """Help for all command"""
        print("Prints all string representations of all instances.")
        print("Usage: all <class name> (optional)")

    def help_update(self):
        """Help for update command"""
        print("Updates an instance based on the class name and id.")
        print("Usage: update <class name> <id> <attribute name> "
              "\"<attribute value>\"")


if __name__ == '__main__':
        HBNBCommand().cmdloop()
