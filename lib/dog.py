class Dog:
    APPROVED_BREEDS = ["Labrador", "Poodle", "Bulldog", "Beagle", "Pug", "Golden Retriever"]

    def __init__(self, name="Buddy", breed="Labrador"):
        self.name = name  
        self.breed = breed  

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()

    def get_breed(self):
        print("Getting breed")
        return self._breed

    def set_breed(self, value):
        if value not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
