from keras.models import load_model
import logging
import argparse
import os
import cv2
from sklearn.preprocessing import LabelBinarizer
import pandas as pd
import numpy as np

'''
## TODO: add batch processing

How to use this detection for single image
python3 detect_single.py -i /home/path/to/image/address.jpg

ignore tensorflow errors for cuda.
'''


class ObjDetect(object):
    logger = None

    def __init__(self, ):
        self.logger = self.set_logger()
        pass

    def detect(self, im_ad):
        h = w = 100  # height and width of the images we will feed into nn
        self.logger.info("received image address: "+im_ad)
        _im = cv2.imread(im_ad)
        _im = cv2.cvtColor(_im, cv2.COLOR_RGB2BGR)
        _im = cv2.resize(_im, (h, w), interpolation=cv2.INTER_NEAREST)
        x = np.array([_im], dtype=np.float32) / 255
        model = load_model('obj_classification_small_model.h5')
        pred = model.predict(x)
        encoder = LabelBinarizer()
        lf = pd.read_csv('labels.csv', header=None)
        encoder.fit(lf.iloc[:, 0].to_list())
        pred_label = encoder.inverse_transform(pred)[0]
        self.logger.info("predicted label: {}".format(pred_label))
        return pred_label

    def set_logger(self):
        # create logger
        self.logger = logging.getLogger('log_application')
        self.logger.setLevel(logging.DEBUG)
        # create file handler
        fh = logging.FileHandler('log2.log')
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)
        ### usage
        # logger.info("message")
        # logger.debug("message")
        return self.logger


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
    parser = argparse.ArgumentParser(
        description='look into the eyes of the code',
        epilog="add stuff, if need be"
    )
    parser.add_argument('-i', type=str, default="", help='image address')
    args = parser.parse_args()
    if len(args.i) > 1:
        od = ObjDetect()
        _this = od.detect(args.i)
        print(_this)
    exit(0)
