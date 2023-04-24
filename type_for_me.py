from pynput.keyboard import Key, Controller
from time import sleep
import sys
import json

""" vars """
bot = Controller()

# get args
cong = json.loads(sys.argv[1])
report = json.loads(sys.argv[2])
form = json.loads(report['data'])
# get args

sleep(5)

def fillHeader():
    for i in [f"{cong['name']} - {cong['number']}", cong['city'], cong['state'], report['month'], report['year']]:
        bot.press(Key.delete)
        bot.type(str(i))
        # print(str(i))
        bot.press(Key.tab)
        # sleep(.1)


def fillForm():
    for i in form:
        bot.press(Key.delete)
        bot.type(str(i))
        # print(str(i))
        bot.press(Key.tab)
        # sleep(.1)


if __name__ == '__main__':
    fillHeader()
    fillForm()
