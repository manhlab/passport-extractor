import torch
import os
from roboflow import Roboflow

os.environ["DATASET_DIRECTORY"] = "./yolov5"
rf = Roboflow(api_key="pewGu5cUedj99Fs27Xjq")
project = rf.workspace("sarkisov1337-gmail-com").project("passport-lk1l7")
dataset = project.version(4).download("yolov5")
