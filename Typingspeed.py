
from pynput.keyboard import Key, Listener
import datetime

sentence = "hi i am woodyhi i am"
print("Type this as fast as you can!")
print(sentence)
correct, incorrect = 0, 0
current_index = 0

start_time = datetime.datetime.now()

def on_press(key):
    global current_index, correct, incorrect, sentence
    if key == Key.shift:
        pass
    else:
        if key == Key.backspace and current_index > 0:
            current_index -= 1
        elif key == Key.backspace:
            pass
        elif str(key).replace("'", "") == sentence[current_index] or (key == Key.space and sentence[current_index] == " "):
            correct += 1
            current_index += 1
        else:
            incorrect += 1
            current_index += 1

def on_release(key):
    global current_index, sentence, start_time, correct, incorrect
    if current_index >= len(sentence):
        total_time = datetime.datetime.now() - start_time
        accuracy = (correct * 100) / (correct + incorrect)
        print(f"Total time taken is {total_time} and with an accuracy of {accuracy}%")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
