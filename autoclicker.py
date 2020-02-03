import time
from pynput import mouse, keyboard

# config
trigger_key = keyboard.Key.ctrl
exit_key = keyboard.Key.f12
time_steps = 0.2 # in seconds

# script
print("Please see autoclicker.py for configuration")
print("Trigger Key (start/stop clicking): {}, Exit Key: {}, Time steps: {}s".format(
    trigger_key, exit_key, time_steps))
print("running... waiting for trigger key")

exit_request = False
is_active = False

def is_same_key(a, b):
    return a == b or (hasattr(a, "char") and a.char == b)

def on_press(key):
    global is_active, exit_request
    if is_same_key(key, trigger_key):
        is_active = not is_active
        print("started clicking" if is_active else "stopped clicking")
    elif is_same_key(key, exit_key):
        exit_request = True
        print("stopping script...")

listener = keyboard.Listener(on_press=on_press)
listener.start()

mc = mouse.Controller()
while not exit_request:
    if is_active:
        mc.click(mouse.Button.left, 1)
    time.sleep(time_steps)

keyboard.Listener.stop(listener)