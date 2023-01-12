import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('./keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    start_time = time.time()
    elasped_time = 0
    pred_list = []
    countdown = 1
    while (countdown - elasped_time) > 0: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        pred_list.append(np.argmax(prediction))    
        elasped_time = time.time() - start_time
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    result = max(set(pred_list), key=pred_list.count)
    labels = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3: 'Nothing'}
    user_choice = labels[result]
    print(user_choice)
    return user_choice

def get_computer_choice():
    rps_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(rps_choices)
    return computer_choice

def get_winner(computer_choice, user_choice):
    if user_choice == 'Nothing':
        print('You didnt make a choice. Round forfeited.')
        return 1
    elif computer_choice == user_choice:
        print('This round is a tie!')
        return 0
    elif (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        print('You lost this round.')
        return 1
    else:
        print('You won this round!')
        return 2

def play():
    user = get_prediction()
    computer = get_computer_choice()
    return get_winner(computer, user)

def rps_match():
    computer_wins = 0
    user_wins = 0
    rounds_played = 0
    while True:
        if rounds_played == 5:
            break
        if (computer_wins or user_wins) == 3:
            break
        get_ready = input(f'Round {rounds_played + 1}: Ready to proceed? Press enter to continue or CTRL+C to exit.')
        round_result = play()
        rounds_played += 1
        if round_result == 1:
            computer_wins += 1
        elif round_result == 2:
            user_wins += 1
        else:
            continue
    cap.release() # After the loop release the cap object
    cv2.destroyAllWindows() # Destroy all the windows
    if computer_wins > user_wins:
        print(f'You lost the match. Computer : {computer_wins}, User: {user_wins}')
    elif computer_wins < user_wins:
        print(f'You won the match! Computer : {computer_wins}, User: {user_wins}')
    else:
        print(f'The match is a tie. Computer: {computer_wins}, User: {user_wins}')
    
rps_match()
