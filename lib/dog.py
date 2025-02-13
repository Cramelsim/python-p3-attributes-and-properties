class Dog:
    APPROVED_BREEDS = ["Labrador", "Poodle", "Bulldog", "Beagle", "Pug", "Golden Retriever"]

    def __init__(self, name="Buddy", breed="Labrador"):
        self.name = name  
        self.breed = breed  

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()

    def get_breed(self):
        print("Getting breed")
        return self._breed

    def set_breed(self, breed):
        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
