import cv2
from keras.models import load_model
import numpy as np
model = load_model('./keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    predictions = []
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        predictions.append(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release() # After the loop release the cap object
    cv2.destroyAllWindows() # Destroy all the windows
    pred_array = np.vstack(predictions)
    pred_list = []
    for row in pred_array:
        pred_list.append(np.argmax(row))
    result = max(set(pred_list), key=pred_list.count)
    labels = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3: 'Nothing'}
    print(labels[result])
    return result

get_prediction()