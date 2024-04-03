from model_loader import model
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from PIL.Image import Image
import numpy as np


def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]  # RGB
    image = np.expand_dims(image, axis=0)  # 차원을 확장: 2차원 -> 3차원
    image = (
        image / 127.5 - 1.0
    )  # scaler(정규화): 이미지데이터가 -1에서 1 사이 값으로 정규화
    # tf.keras.applications.imagenet_utils.decode_predictions(preds, top=5)
    # preds: NumPy array encoding a batch of predictions.
    # top: Integer, how many top-guesses to return. Defaults to 5.
    # return: (class_name, class_description, score)
    result = decode_predictions(model.predict(image), 3)[0]
    print(result)
    response = []
    for i, res in enumerate(result):
        response.append({"class": res[1], "confidence": f"{res[2]*100:0.2f} %"})

    return response
