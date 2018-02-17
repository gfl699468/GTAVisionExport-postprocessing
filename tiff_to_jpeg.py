import os
from configparser import ConfigParser

from PIL import Image

ini_file = "gta-postprocessing.local.ini"


if __name__ == '__main__':
    CONFIG = ConfigParser()
    CONFIG.read(ini_file)
    in_directory = CONFIG["Images"]["Tiff"]
    out_directory = CONFIG["Images"]["Jpg"]
    files = [
        'info-2017-11-19--23-21-03.tiff',
        'info-2017-11-19--23-21-11.tiff',
        'info-2017-11-19--23-21-31.tiff',
        'info-2017-11-19--23-21-25.tiff',
        'info-2017-11-19--23-21-29.tiff',
        'info-2017-11-19--23-20-42.tiff',
        'info-2017-11-19--23-20-05.tiff',
        'info-2017-11-19--23-20-11.tiff',
        'info-2017-11-19--23-19-12.tiff',
        'info-2017-11-19--23-19-19.tiff',
    ]
    frames = [
        0, 1, 2, 3
    ]
    for name in files:
        base_name = os.path.splitext(name)[0]
        for frame in frames:
            im = Image.open(os.path.join(in_directory, name))
            im.seek(frame)
            im = im.convert(mode="RGB")
            print("Generating jpeg for {}".format(name))
            outfile = os.path.join(out_directory, base_name) + "-{}.jpg".format(frame)
            im.save(outfile)
