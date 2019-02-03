import os


class Person:

    def __init__(self, name):
        self.name = name

        self.training_data_path_for_person = "/Users/vashisth/PycharmProjects/PennApps2018/FacesDatabase/"+name
        if not os.path.exists(self.training_data_path_for_person):
            os.makedirs(self.training_data_path_for_person)

    def save_image(self, image):
        pass


