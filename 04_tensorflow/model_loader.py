# tensorflow 에서 모델 불러오기
import tensorflow as tf


def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    print("Success to load model!")
    return model


model = load_model()
