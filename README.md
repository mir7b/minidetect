# minidetect
mini object detection

## WHAT
detects objects. based on [https://github.com/bbferka/odu_iai](https://github.com/bbferka/odu_iai) dataset.

## WHERE
somewhere on your computer

## HOW

Check scripts. but overall, you should first clone into the repo mentioned above, make sure you know where on your system it is. then checkout datamaker which makes you the samples. then checkout `fancy.ipynb` which makes you the model. you can skip all of this and instead use the model that I have uploaded. but you will need to run the `detect_single.py` (no pun intended) given the path to the image pof the object you want classified. if your folder structure differs than normal, or if you get errors, run the fancy file again, as it will recreate the lables. (I couldn't just save the LabelBinarizer state, unfortunately)

you also get log files to help you debug. add stuff there, guide is in each python file. 

## WHY
Because :P 

