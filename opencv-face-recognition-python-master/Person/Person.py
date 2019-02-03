import os
import numpy as np

class Person:

    def __init__(self, name):
        self.name = name

        counter = [3]
        np.save("training_counter_id.npy", np.asarray(counter))

        # counter = np.load("training_counter_id.npy")
        # self.number = counter[0]
        #
        # self.training_data_path_for_person = "../newtraining/s"+str(self.number)
        # if not os.path.exists(self.training_data_path_for_person):
        #     os.makedirs(self.training_data_path_for_person)
        #
        # counter[0] += 1
        # np.save("training_counter_id.npy", counter)

    def save_image(self, image):
        pass

pp = Person("JOHN DOE")
