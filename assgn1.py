import numpy as np
import matplotlib.pyplot as plt 
import h5py
import scipy 
from PIL import Image 
from scipy import ndimage
from lr_utils import load_dataset 





train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

m_train = train_set_x_orig.shape[0]
m_test = test_set_x_orig.shape[0]
num_px = test_set_x_orig.shape[1]




