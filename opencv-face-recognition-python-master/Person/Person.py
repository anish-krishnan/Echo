import os


class Person:

    def __init__(self, name, number):
        self.name = name
        self.number = number

        self.training_data_path_for_person = "../newtraining/s"+str(number)
        if not os.path.exists(self.training_data_path_for_person):
            os.makedirs(self.training_data_path_for_person)

    def save_image(self, image):
        pass
