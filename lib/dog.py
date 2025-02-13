class Dog:
    APPROVED_BREEDS = ["Labrador", "Poodle", "Bulldog", "Beagle", "Pug", "Golden Retriever"]

    def __init__(self, name="Buddy", breed="Labrador"):
        self.name = name  # Calls the setter
        self.breed = breed  # Calls the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
