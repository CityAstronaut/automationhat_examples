import automationhat
import time

while True:
    automationhat.relay.one.toggle()
    time.sleep(0.5)
