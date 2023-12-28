import tensorflow as tf
from keras.models import load_model

class Wrapper:
    
    def __init__(self):
        self._model = load_model(f"static/models/nn.h5")

    def getModel(self):
        return self._model