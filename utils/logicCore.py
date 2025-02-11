import pyautogui
import time

def playScore(score,tik):
    index = 0
    while index < len(score):
        chord = score[index]
        pyautogui.hotkey(*chord)
        time.sleep(tik)
        index += 1


if __name__ == '__main__':
    score = [
        (),
        ('b','Enter'),
        ('c','Enter'),
        ('d','Enter'),
        ('e','Enter'),
        (),
        ('b','Enter'),
        ('c','Enter'),
        ('d','Enter'),
        ('e','Enter'),
        (),
        ('b','Enter'),
        ('c','Enter'),
        ('d','Enter'),
        ('e','Enter'),
        (),
        ('b','Enter'),
        ('c','Enter'),
        ('d','Enter'),
        ('e','Enter'),
    ]
    playScore(score, 0.5)



