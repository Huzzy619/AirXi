import datetime
import string
import random
import os



def get_media_paths(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('school_logo/', filename)


def reference_number_generator (length = 20, chars = string.digits):
    return ''.join(random.choice(chars) for _ in range(length))