## Title:       Jiggler Bells
## Description: My own very basic mouse jiggler
## Author:      Claudiu Costin
## Version:     1.1
## Date:        2024-01-17

## prereq's:
## pip install pyautogui

# import pyautogui
# import time
# import random
# import sys

# pyautogui.FAILSAFE = False

# def switch_screens() -> None:
#     """
#     Switches the active screen using Alt + Tab
#     a random number of times.
#     """
#     max_switches = random.randint(1, 5)
#     pyautogui.keyDown('alt')

#     for _ in range(1, max_switches):
#         pyautogui.press('tab')

#     pyautogui.keyUp('alt')

# def wiggle_mouse() -> None:
#     """
#     Wiggles the mouse between two coordinates.
#     """
#     max_wiggles = random.randint(4, 9)

#     for _ in range(4, 9):
#         coords = get_random_coords()
#         pyautogui.moveTo(
#         x=coords[0],
#         y=coords[1],
#         duration=5
#     )
#     time.sleep(10)

# def get_random_coords() -> []:
#     """
#     Returns a list of coordinates in the format [x=1900, y=1800]
#     """

#     screen = pyautogui.size()
#     width = screen[0]
#     height = screen[1]

#     return [
#         random.randint(100, width - 200),
#         random.randint(100, height - 200)
#     ]

# if __name__ == "__main__":
#     print('Press CTRL-C to quit.')
#     try:
#         while True:
#             switch_screens()
#             wiggle_mouse()
#             sys.stdout.flush()
#     except KeyboardInterrupt:
#         print("\n")
