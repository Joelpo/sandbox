# Singleton.py / Singleton pattern
# Class uses an imbricated _private class to garantee unicity.
# If Singleton is instanciated but instance is already there, we just change the attribute of current instance.
class Singleton:

    # Singleton instance object
    instance = None

    # If no current singleton instance, call inner class constructor
    # If current instance, just change the name of instance
    def __init__(self, name):
        if not Singleton.instance:
            Singleton.instance = Singleton._Singleton(name)
        else:
            Singleton.instance.name = name

    def getName(self):
        return self.instance.getName()

    class _Singleton:
        def __init__(self, name):
            self.name = name

        def getName(self):
            return self.name

# Main class for testing purposes.
def main():
    obj1 = Singleton("Llamas")
    print("Name is {}".format(obj1.getName()))

    obj2 = Singleton("Llamas2")
    print("Name is {}".format(obj2.getName()))

    # should print second name, even though we are calling first object
    print("Name is {}".format(obj1.getName()))


if __name__ == "__main__":
    main()
