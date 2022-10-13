import os
import logging
import shutil
import argparse

'''
## TODO: give an option for a selectable return path.

address format: /home/path/to/odu_iai
Usage: python3 datamaker.py -i /home/path/to/odu_iai
will create a log file and a samples directory in the same directory that it executed in.

# address for the repo you need to have: https://github.com/bbferka/odu_iai
'''


def do_the_thing(odu_path):
    global logger
    inc_path = odu_path + "/object_data/partial_views/"
    logger.info("source path: " + inc_path)
    out_path = os.getcwd() + "/samples/"
    logger.info("destination path: " + out_path)
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    for i in os.listdir(inc_path):
        if not os.path.exists(out_path + i):
            os.mkdir(out_path + i)
        for j in os.listdir(inc_path + i):
            if j.endswith('_crop.png'):
                src_path = inc_path + i + "/" + j
                dst_path = out_path + i + "/" + j
                logger.debug(src_path)
                shutil.copy(src_path, dst_path) # comment this out for tests.
    return


def set_logger():
    # create logger
    global logger
    logger = logging.getLogger('log_application')
    logger.setLevel(logging.DEBUG)
    # create file handler
    fh = logging.FileHandler('log.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    ### usage
    # logger.info("message")
    # logger.debug("message")


if __name__ == '__main__':
    global logger
    set_logger()
    parser = argparse.ArgumentParser(
        description='look into the eyes of the code',
        epilog="add stuff, if need be"
    )
    parser.add_argument('-i', type=str, default="", help='repository directory address')
    args = parser.parse_args()
    if len(args.i) > 1:
        do_the_thing(args.i)
    exit(0)
