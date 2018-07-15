import os
import config
import filesystem
import imageio
import time


def take_photo():
    command = "raspistill -w " + config.WIDTH + " -h " + config.HEIGHT + \
              " -o photo.jpg -sh 40 -awb auto -mm spot -ex auto -q 100 -sh 50 -v -n"
    os.system(command)

    if config.LOCAL_STORE_ENABLED:
        filesystem.copy_photo_to_local_storage()
    return True


def gather_files(latest_photo=None):
    if latest_photo:
        images = []
        filenames = []
        i = 36
        while i > 0:
            filenames.append(config.LOCAL_STORAGE_LOCATION + "%010d" % (int(latest_photo) - i) + ".jpg")
            i = i - 1
        return filenames
    return None


def create_gif(latest_photo=None):
    start = int(time.time())
    images = []
    filenames = gather_files(latest_photo)
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('timelapse-full.gif', images)
    end = int(time.time())
    print("Took " + str(end - start) + " seconds to create gif")
    print("Optimising gif and resizing to 25%")
    os.system('gifsicle --scale 0.25 -i timelapse-full.gif > timelapse.gif')
    end2 = int(time.time());
    print("Took " + str(end2 - end) + " seconds to optimise/resize gif")
    print("Took " + str(end2 - start) + " seconds total")


def create_mp4(latest_photo):
    filenames = gather_files(latest_photo)
    writer = imageio.get_writer('timelapse.mp4', fps=10)
    for filename in filenames:
        writer.append_data(imageio.imread(filename))
    writer.close

    start = int(time.time())
    end = int(time.time())
    print("Took " + str(end - start) + " seconds to create mp4")
