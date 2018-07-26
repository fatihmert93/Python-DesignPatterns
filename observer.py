class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = [] #This where references to all the observers are being kept
                             # Note that this is a one to many relationship: where will be one subject to be observed by multiple _observers

    def attach(self,observer):
        if observer not in self._observers: #If the observer is not already in the observers list
            self._observers.append(observer) # append the observer to the list


    def detach(self,observer): #Simple remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  #For all te observers in the list
           if modifier != observer: # Don't notify the observer who is actually updating the temperature
                observer.update(self) # Alert the observers!

class Core(Subject): #Inhreits from the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name #Set the name of the core
        self._temp = 0 #Initialize the temeprature of the core

    @property #Getter that gets the core temeprature
    def temp(self):
        return self._temp

    @temp.setter #Setter that sets the core temperature
    def temp(self,temp):
        self._temp = temp
        self.notify() #Notify the observers whenever somebody changes the core temperatures


class TempViewer:

    def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has Temeprature {}".format(subject._name, subject._temp))


c1 = Core("Core1")
c2 = Core("Core2")

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c2.temp = 90

