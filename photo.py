import os
import config
import filesystem


def take_photo():
    command = "raspistill -w " + config.WIDTH + " -h " + config.HEIGHT + \
              " -o photo.jpg -sh 40 -awb auto -mm spot -ex auto -q 100 -sh 50 -v -n"
    os.system(command)

    if config.LOCAL_STORE_ENABLED:
        filesystem.copy_photo_to_local_storage()
