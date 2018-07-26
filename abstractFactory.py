class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class PetStore:

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):

        pet = self._pet_factory.get_pet()
        print(pet)



#Create a Concrete Factory
factory = DogFactory()

#Create a pet store housing
print("hello")