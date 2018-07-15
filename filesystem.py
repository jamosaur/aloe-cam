import config
import os
import glob


def get_latest_file_number():
    list_of_files = glob.glob(config.LOCAL_STORAGE_LOCATION + "*")
    if not list_of_files:
        return 1
    latest_file = max(list_of_files, key=os.path.getctime)
    _, filename = os.path.split(latest_file)
    print("Latest Filename " + filename)
    return int(filename.split(".")[0])


def copy_photo_to_local_storage():
    file_name = "%010d" % get_latest_file_number() + ".jpg"
    os.system("cp -f photo.jpg " + config.LOCAL_STORAGE_LOCATION)
    os.system("mv " + config.LOCAL_STORAGE_LOCATION + "photo.jpg " + config.LOCAL_STORAGE_LOCATION + file_name)
