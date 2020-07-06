import os
import pathlib
import shutil
import random
from os.path import basename

curr_dir = pathlib.Path().absolute()
path = str(curr_dir) + "//AudioData//"

label_conversion = {'01': 'n',
                '02': "calm", #this feature is absent in SAVEE dataset
                '03': 'h',
                '04': 'sa',
                '05': 'a',
                '06': 'f',
                '07': 'd',
                '08': 'su'}

for subdir,dirs,files in os.walk(path):
    string = basename(subdir)
    new_path = str(curr_dir)+ "//SAVEE_RAVDESS//" +str(string) + "//"
    os.makedirs(new_path)
    for filename in files:        
        old_file_path = os.path.join(os.path.abspath(subdir), filename)
        base, extension = os.path.splitext(filename)
        for key, value in label_conversion.items():
            if base.startswith(value):
                random_list = random.sample(range(10, 99), 7)
                random_name = '-'.join([str(i) for i in random_list])
                if str(string) == "DC":
                    file_name_with_correct_emotion = "03" + random_name[2:3] + "01" + '-' + key + random_name[8:18] + "27" + extension
                elif str(string) == "JE":
                    file_name_with_correct_emotion = "03" + random_name[2:3] + "01" + '-' + key + random_name[8:18] + "29" + extension
                elif str(string) == "JK":
                    file_name_with_correct_emotion = "03" + random_name[2:3] + "01" + '-' + key + random_name[8:18] + "31" + extension
                elif str(string) == "KL":
                    file_name_with_correct_emotion = "03" + random_name[2:3] + "01" + '-' + key + random_name[8:18] + "33" + extension
                new_file_path = new_path + file_name_with_correct_emotion
                shutil.copy(old_file_path, new_file_path)