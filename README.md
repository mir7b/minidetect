# minidetect
mini object detection

## WHAT
Detects objects. Based on [https://github.com/bbferka/odu_iai](https://github.com/bbferka/odu_iai) dataset.

## WHERE
Somewhere on your computer (hopefully!).

## HOW
Check scripts if you're a nerd. You should first clone into the repo mentioned above, make sure you know where on your system it is. Then checkout `datamaker.py` which makes you the samples. Then checkout `fancy.ipynb` which makes you the model. You can skip all of this and instead use the model I have uploaded. But you will need to run the `detect_single.py` (no pun intended) given the path to the image of the object you want classified. If your folder structure differs from normal, or if you get errors in prediction, run the fancy file again, because it will recreate the lables. (I couldn't just save the LabelBinarizer state, unfortunately)

You also get log files to help you debug. Add stuff there in scripts, the guide for which is in each python file. 

## WHY
Because :P 
