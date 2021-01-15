from efficientnet.tfkeras import EfficientNetB0
from tensorflow.keras import callbacks
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import tensorflow as tf


def create_efficientnet_model(relu_units = 120,learning_rate=0.0001):
    efficient_net = EfficientNetB0(
        weights='imagenet',
        #input_shape=(32,32,3),
        include_top=False,
        pooling='max'
    )

    model = Sequential()
    model.add(efficient_net)
    model.add(Dense(units = relu_units, activation='relu'))
    model.add(Dense(units = relu_units, activation = 'relu'))
    model.add(Dense(units = 1, activation='sigmoid'))

    model.compile(optimizer=Adam(lr=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])

    return model

def create_keras_efficientnet_model(relu_units = 128,learning_rate=0.0001):
    model_builder = tf.keras.applications.efficientnet.EfficientNetB0
    # img_size = (256, 256)
    # preprocess_input = tf.keras.applications.xception.preprocess_input
    # decode_predictions = tf.keras.applications.xception.decode_predictions

    # last_conv_layer_name = "block14_sepconv2_act"
    # classifier_layer_names = [
    #     "avg_pool",
    #     "predictions",
    # ]

    efficientnet_model_base = model_builder(weights="imagenet",include_top=False, pooling='max')
    efficientnet_model_base.summary()

    model = tf.keras.Sequential()
    model.add(efficientnet_model_base)
    model.add(tf.keras.layers.Dense(units = relu_units, activation='relu'))
    model.add(tf.keras.layers.Dense(units = relu_units, activation = 'relu'))
    model.add(tf.keras.layers.Dense(units = 1, activation='sigmoid'))

    model.compile(optimizer=Adam(lr=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])

    return model

def create_keras_efficientnet3_model(relu_units = 128,learning_rate=0.0001):
    model_builder = tf.keras.applications.efficientnet.EfficientNetB3
    # img_size = (256, 256)
    # preprocess_input = tf.keras.applications.xception.preprocess_input
    # decode_predictions = tf.keras.applications.xception.decode_predictions

    # last_conv_layer_name = "block14_sepconv2_act"
    # classifier_layer_names = [
    #     "avg_pool",
    #     "predictions",
    # ]

    efficientnet_model_base = model_builder(weights="imagenet",include_top=False, pooling='max')
    efficientnet_model_base.summary()

    model = tf.keras.Sequential()
    model.add(efficientnet_model_base)
    model.add(tf.keras.layers.Dense(units = relu_units, activation='relu'))
    model.add(tf.keras.layers.Dense(units = relu_units, activation = 'relu'))
    model.add(tf.keras.layers.Dense(units = 1, activation='sigmoid'))

    model.compile(optimizer=Adam(lr=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])

    return model

def create_keras_xception_model(dense_units = 1000,learning_rate=0.0001):
    from tensorflow.keras.layers import GlobalAveragePooling2D
    from tensorflow.keras.layers import Dense    

    model_builder = tf.keras.applications.xception.Xception
    # img_size = (299, 299)
    preprocess_input = tf.keras.applications.xception.preprocess_input
    decode_predictions = tf.keras.applications.xception.decode_predictions
    # img_array = preprocess_input(get_img_array(img_path, size=img_size))
    xception_model_base = model_builder(weights="imagenet",include_top=False)
    model = tf.keras.Sequential()
    model.add(xception_model_base)
    model.add(GlobalAveragePooling2D(name='avg_pool'))
    model.add(Dense(1, activation='sigmoid',name='predictions'))

    model.compile(optimizer=Adam(lr=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])
    return model,xception_model_base

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Model Choice')
    parser.add_argument('--model', default='keras_efficientnet',type=str,metavar='m',help='name of the experiment')    
    args = parser.parse_args()
    if args.model == 'keras_efficientnet':
        model_builder = tf.keras.applications.efficientnet.EfficientNetB0
        efficientnet_model_base = model_builder(weights="imagenet",include_top=False)
        # last_conv_layer_name = "top_activation"
        # classifier_layer_names = [
        #     "avg_pool",
        #     "predictions",
        # ]
        efficientnet_model_base.summary()
    elif args.model == 'keras_xception':
        model_builder = tf.keras.applications.xception.Xception
        xception_model = model_builder(weights="imagenet")
        # last_conv_layer_name = "block14_sepconv2_act"
        # classifier_layer_names = [
        #     "avg_pool",
        #     "predictions",
        # ]
        xception_model.summary()
    elif args.model == 'constructed_xception':
        model,base_model = create_keras_xception_model()
        model.summary()        
        base_model.summary()