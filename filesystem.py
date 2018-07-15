import config
import os
import glob


def get_latest_file_number():
    list_of_files = glob.glob(config.LOCAL_STORAGE_LOCATION + "*")
    if not list_of_files:
        return 1
    latest_file = max(list_of_files, key=os.path.getctime)
    _, filename = os.path.split(latest_file)
    return int(filename.split(".")[0])


def copy_photo_to_local_storage():
    file_name = "%10d" % get_latest_file_number()
    os.system("cp -f photo.jpg " + config.LOCAL_STORAGE_LOCATION + file_name + ".jpg")
