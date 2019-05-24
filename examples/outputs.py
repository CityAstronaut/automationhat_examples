import automationhat
import time

while True:
    automationhat.output.three.on()
    time.sleep(0.5)
    automationhat.output.three.off()
    time.sleep(0.5)
