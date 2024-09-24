class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=""):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    # def pet_type(self, pet_type):
    #     if pet_type in Pet.PET_TYPES:
    #         self.pet_type = pet_type
    #     else:
    #         raise Exception("pet_type must be in the list of pet types")


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
