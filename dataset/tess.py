import os
import pathlib
import shutil
import random
from os.path import basename

curr_dir = pathlib.Path().absolute()
path = str(curr_dir) + "//TESS_Toronto_emotional_speech_set_data//"

label_conversion = {'01': 'neutral',
                '02': "calm", #this feature is absent is TESS dataset
                '03': 'happy',
                '04': 'sad',
                '05': 'angry',
                '06': 'fear',
                '07': 'disgust',
                '08': 'ps'}

for subdir,dirs,files in os.walk(path):
    string = basename(subdir)
    new_path = str(curr_dir)+ "//TESS_RAVDESS//" +str(string) + "//"
    os.makedirs(new_path)
    for filename in files:   
        old_file_path = os.path.join(os.path.abspath(subdir), filename)
        base, extension = os.path.splitext(filename)
        for key, value in label_conversion.items():
            if base.endswith(value):
                random_list = random.sample(range(10, 99), 7)
                random_name = '-'.join([str(i) for i in random_list])
                if filename.startswith('OAF'):
                    file_name_with_correct_emotion = "03" + random_name[2:3]  + "01" + '-' + key + random_name[8:18] + "25" + extension
                elif filename.startswith('YAF'):
                    file_name_with_correct_emotion = "03" + random_name[2:3]  + "01" + '-' + key + random_name[8:18] + "26" + extension
                new_file_path = new_path + file_name_with_correct_emotion
                shutil.copy(old_file_path, new_file_path)