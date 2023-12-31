import tensorflow as tf
from keras.models import load_model
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from sklearn.metrics import accuracy_score, classification_report

class Wrapper:
    
    def __init__(self):
        self._model = load_model(f"apps/detector/static/models/nn.h5")

    def getModel(self):
        return self._model
    
    def predict(self, data):
        return self._model.predict(data)