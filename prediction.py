import numpy as np
from keras.models import load_model
#from keras.preprocessing import image
import os
import cv2, imageio

class humanface:
    def __init__(self,filename):
        self.filename =filename
        path = r'C:\Users\sathe\Satheesh_SK\Human_Classification'
        os.chdir(path)
        os.chdir('UTKFace_052021')


    def prediction_humanface(self):
        # load model
        model = load_model('multiclass_face.h5')
        images = []
        ages = []
        genders = []
        image_files = os.listdir()
        for file in image_files:
            image = imageio.imread(file)
            image = cv2.resize(image, dsize=(64, 64))
            image = image.reshape((image.shape[0], image.shape[1], 3))
            images.append(image)
            split_var = file.split('_')
            ages.append(split_var[0])
            genders.append(int(split_var[1]))

        def age_group(age):
            if age > 0 and age < 10:
                return 1
            elif age > 10 and age < 30:
                return 2
            elif age > 30 and age < 50:
                return 3
            elif age > 50 and age < 80:
                return 4
            else:
                return 4

        def get_age(distr):
            distr = distr * 4
            if distr <= 0.65: return "Child"
            if distr > 0.6 and distr <= 1.4: return "Adult"
            if distr >= 1.5 and distr <= 2.4: return "Young"
            if distr >= 2.5 and distr <= 3.4: return "MiddleAge"
            if distr >= 3.5 and distr <= 4.4: return "OldAge"
            return "VeryOld"

        def get_gender(prob):
            if prob < 0.5:
                return "Male"
            else:
                return "Female"

        def get_result(sample):
            sample = sample / 255
            yy = model.predict(np.array([sample]))
            age = get_age(yy[0][0])
            gender = get_gender(yy[0][1])
            print("Predicted Gender:", gender, "Predicted Age:", age)


