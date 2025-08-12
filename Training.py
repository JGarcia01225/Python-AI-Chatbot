import random
import json
import pickle
import numpy as np

import ntlk
from ntlk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keraas.optimizers import SGD

lemmatizr = WordNetLemmatizer
intents = json.loads(open('intnts.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']


