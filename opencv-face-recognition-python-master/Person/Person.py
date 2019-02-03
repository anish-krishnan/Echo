import os
import numpy as np

class Person:

    def __init__(self, name):
        self.name = name

        #Initialize ONLY!
        # person_dict = {1 : "Vashisth Parekh", 2 : "Anish Krishnan"}
        # np.save("person_dict.npy", person_dict)
        # counter = [3]
        # np.save("training_counter_id.npy", np.asarray(counter))

        counter = np.load("training_counter_id.npy")
        person_dict = np.load("person_dict.npy")
        # print(person_dict.item().get(1))

        self.number = counter[0]
        self.training_data_path_for_person = "../newtraining/s"+str(self.number)
        if not os.path.exists(self.training_data_path_for_person):
            os.makedirs(self.training_data_path_for_person)

        # counter[0] += 1
        # person_dict[self.number] = self.name

        #print(dict(np.ndenumerate(person_dict)).get())

        myarray = person_dict

        updated_person_dict = dict(enumerate(myarray.flatten(), 1))[1]
        updated_person_dict[self.number] = self.name
        print(updated_person_dict)

        np.save("training_counter_id.npy", counter)
        np.save("person_dict.npy", person_dict)

    def save_image(self, image):
        pass

pp = Person("JOHN DOE")
