from abc import ABC, abstractmethod

# IObservable interface


class IObservable:
    @abstractmethod
    def subscribe(self):
        pass

    @abstractmethod
    def unsubscribe(self):
        pass

    @abstractmethod
    def notify(self, *args):
        pass

# IObserver interface


class IObserver:
    @abstractmethod
    def notify(self, *args):
        pass

# Subject : the one who notifies his subscribers
class Subject(IObservable):

    observers = []

    def __init__(self):
        pass

    def subscribe(self, obj):
        if not obj in self.observers:
            self.observers.append(obj)

    def unsubscribe(self, obj):
        self.observers.remove(obj)

    def notify(self, *args):
        for x in self.observers:
            x.notify(args)

# Observer : the one who subscribes and gets notified


class Observer(IObservable):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def notify(self, *args):
        print("{} notified. Message : {}".format(str(self), args))


# CLIENT
subject = Subject()
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")


subject.subscribe(observer1)
subject.subscribe(observer2)

subject.notify("Winter is coming. Brace yourselves")


subject.unsubscribe(observer2)

subject.notify("Summer is coming. All is good")
