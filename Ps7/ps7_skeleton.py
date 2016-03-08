import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name=name
        self.location=(float(location[0]),float(location[1]))
        self.species_types={}
        self.species_types=species_types

    def get_number_of_species(self, animal):
        if animal in self.species_types.keys():
            return self.species_types[animal]
        else:
            return 0

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        if  species in self.species_types.keys():
            self.species_types[species]-=1
            if self.species_types[species]==0:
                self.species_types.pop(species)


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):

        return self.name

    def get_desired_species(self):

        return self.desired_species

    def get_score(self, adoption_center):

        count = 0.0
        sp=self.desired_species.split(' ')
        for specie in sp:
            if adoption_center.get_number_of_species(specie):
                count += adoption_center.get_number_of_species(specie)
        return float(count)


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species=considered_species

    def get_score(self, adoption_center):
        count = 0.0
        for cs in self.considered_species:
            count+=adoption_center.get_number_of_species(cs)*0.3

        return float(count+Adopter.get_score(self, adoption_center))


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species=feared_species

    def get_score(self, adoption_center):

        result = float(Adopter.get_score(self, adoption_center)- adoption_center.get_number_of_species(self.feared_species)*0.3)

        if result > 0:
            return result
        else:
            return 0.0



ad=AdoptionCenter("NY",{"dog":1,"cat":1,"horse":1},(1,1))
fa=FearfulAdopter("boaz","fish","horse")
flix=FlexibleAdopter("Carmit","dog",["cat","fish"])

print fa.get_score(ad)
print flix.get_score(ad)


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        for sp in self.allergic_species:
            if adoption_center.get_number_of_species(sp):
                return 0.0

        return float(Adopter.get_score(self, adoption_center))


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness.copy()

    def get_score(self, adoption_center):
        low = 1.0
        adoptionSpecies = adoption_center.get_species_count()
        for item in adoptionSpecies:
            if item in self.allergic_species and item in self.medicine_effectiveness.keys():
                if low > self.medicine_effectiveness[item]:
                    low = self.medicine_effectiveness[item]
            elif item in self.allergic_species and not (item in self.medicine_effectiveness.keys()):
                low = 0.0

        return low*Adopter.get_score(self, adoption_center)









class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here 

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 



