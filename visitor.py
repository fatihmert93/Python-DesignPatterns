class House(object): #The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        #Triggers the visiting operation!
        visitor.visit(self)


    def work_on_hvac(self,hvac_specialist):
        print(self,"worked on by", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object

    def work_on_eletricity(self, electrician):
        #Note that we now have a reference to the electrician object in the house object!
        print(self, "worked on by", electrician)

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__


class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""
    def visit(self,house):
        house.work_on_hvac(self)


class Electrician(Visitor): #Inherits from the parent class, Visitor
    """Concrete visitor: electrician"""
    def visit(self, house):
        #Note that the visitor now has a reference to the house object
        house.work_on_eletricity(self)



hv = HvacSpecialist()

e = Electrician()

home = House()

home.accept(hv)

home.accept(e)