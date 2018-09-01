import win32api, win32con
import time
import winsound

def left_click(x, y):
    '''
    Simulate left click on X and Y coordinates
    :param x:
    :param y:
    :return:
    '''
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def double_click(x, y):
    '''
    Simulate double left click on X and Y coordinates
    :param x:
    :param y:
    :return:
    '''
    left_click(x, y)
    left_click(x, y)

def register_position(z):
    '''
    Register mouse position on screen
    :param z:
    :return:
    '''

    print("Click %s:" % str(z))
    winsound.Beep(2500, 200)

    time.sleep(4)

    # cursor position
    (x, y) = win32api.GetCursorPos()

    left_click(x, y)

    print("Saved (%s, %s)." % (x, y))
    winsound.Beep(2500, 1000)

    return (x, y)


def main():

    print("Auto Clicker Bot v1.0.0.\nPay attention at next step while configuring bot. Clicking cycles run infinitely - until the bot is manually stopped!")
    print("---------------------------")

    sec = float(input("Delay between clicks in seconds (input): "))
    n_click = int(input("Total number of clicks (input): "))

    clicks_list = list()

    print("After the short beep sound, you have 4 seconds to set mouse cursor on screen where your want the click to happen.\nLonger beep will notify you that position is saved.")
    time.sleep(5)

    for i in range(n_click):
        clicks_list.append(register_position(i))

    print("\nConfiguration finished. Bot waking up in 3 seconds...")
    print("---------------------------")

    time.sleep(3)

    i = 0
    while True:

        x, y = clicks_list[i]
        double_click(x, y)
        print("Click %s, coordinates (%s, %s)." % (i, x, y))
        time.sleep(sec)
        i = (i + 1) % len(clicks_list)


if __name__ == "__main__":

    main()
