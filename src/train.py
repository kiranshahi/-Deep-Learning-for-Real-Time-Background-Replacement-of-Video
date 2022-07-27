import pandas as pd
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, CSVLogger

import network as net
from data_frame import get_data as df_get_data
from data_image import get_data as di_get_data

EPOCHS = 10
BATCH = 2


def get_callback(checkpoint_path):
    csv_path = "resnet_data_aug_val.csv"

    callbacks = [
        ModelCheckpoint(filepath='/home/kiran_shahi/dissertation/model/' + checkpoint_path + 'model.h5', monitor="loss",
                        verbose=1, save_best_only=True),
        ReduceLROnPlateau(monitor='loss', factor=0.1, patience=4),
        CSVLogger(csv_path),
        EarlyStopping(monitor='loss', patience=10, restore_best_weights=True)
    ]
    return callbacks


def train_model(train_dataset, valid_dataset, checkpoint_path, saved_model=None):
    if saved_model is not None:
        model = tf.keras.models.load_model(saved_model)
    else:
        model = net.resnet_unet()
    callbacks = get_callback(checkpoint_path)
    model.fit(train_dataset, validation_data=valid_dataset, epochs=EPOCHS, callbacks=callbacks, batch_size=BATCH)


def call_train():
    train_set = ['set1_train.csv', 'set2_train.csv']
    valid_set = ['set1_valid.csv', 'set2_valid.csv']

    for count in range(3):
        if count != 2:
            train_df = pd.read_csv("/home/kiran_shahi/dissertation/csv_data/" + train_set[count])
            valid_df = pd.read_csv("/home/kiran_shahi/dissertation/csv_data/" + valid_set[count])
            train_dataset, valid_dataset = df_get_data(train_df, valid_df, frame_size=15)
        else:
            train_dataset, valid_dataset = di_get_data()

        if count == 0:
            saved_model = None
        else:
            saved_model = 'Set' + str(count) + '/model.h5'

        train_model(train_dataset, valid_dataset, 'Set' + str(count + 1), saved_model)


call_train()
