class Component(object):
    """Abstract class"""

    def __init__(self,*args,**kwargs):
        pass

    def component_function(self):
        pass

class Child(Component): #Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self,*args,**kwargs):
        Component.__init__(self,*args,**kwargs)

        #This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        #Print the name of your child item here!
        print("{}".format(self.name))


class Composite(Component):
    """Concrete class and maitains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self,*args,**kwargs)

        #This is where we store the name of the composite object
        self.name = args[0]

        #This is where we keep our child items
        self.children = []


    def append_child(self, child):
        """Meethod to add a new child item"""
        self.children.append(child)

    def remove_child(self,child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):

        #Print the same name of the composite object
        print("{}".format(self.name))

        #Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()


#Build a composite submenu 1
sub1 = Composite("submenu1")

#Create a new child sub_menu 11
sub11 = Child("Sub_submenu 11")
sub12 = Child("sub_submenu 12")

sub1.append_child(sub11)

sub1.append_child(sub12)

#Build a top-level composite menu
top = Composite("top_menu")

#Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

top.append_child(sub1)

top.append_child(sub2)

top.component_function()