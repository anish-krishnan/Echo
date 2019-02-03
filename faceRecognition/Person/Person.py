import os
import numpy as np

class Person:

    def __init__(self, name):
        self.name = name

        #Initialize ONLY!
        # person_dict = {2 : "Vashisth Parekh", 1 : "Anish Krishnan"}
        # np.save("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/person_dict.npy", person_dict)
        # counter = [3]
        # np.save("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/training_counter_id.npy", np.asarray(counter))

        counter = np.load("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/training_counter_id.npy")
        person_dict = np.load("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/person_dict.npy")
        # print(person_dict.item().get(1))
        self.number = counter[0]
        self.training_data_path_for_person = "/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/newtraining/s"+str(self.number)
        if not os.path.exists(self.training_data_path_for_person):
            os.makedirs(self.training_data_path_for_person)
        # print(dict(np.ndenumerate(person_dict)).get())
        updated_person_dict = dict(enumerate(person_dict.flatten(), 1))[1]
        updated_person_dict[self.number] = self.name
        print(updated_person_dict)

        counter[0] += 1
        np.save("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/training_counter_id.npy", np.asarray(counter))
        np.save("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/person_dict.npy", person_dict)

    def save_image(self, image):
        pass

def isNameInDB(name):
    print(name)
    person_dict = np.load("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/person_dict.npy")
    subjects = dict(enumerate(person_dict.flatten(), 1))[1]
    for key in subjects:
        if(subjects[key] == name):
            print("TRUEEEE NAME FOUND")
            return True
    return False

# pp = Person("o90jiugy")
counter = np.load("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/training_counter_id.npy")
person_dict = np.load("/Users/anishkrishnan/GitHub/PennApps2018/faceRecognition/Person/person_dict.npy")
print("Counter", counter)
print("person_dict", person_dict)
