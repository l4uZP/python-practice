import time

floors = 10
asterisks = "* "

while floors > 0:
    print(" " * floors, end='')
    print(asterisks)
    asterisks = asterisks + "* "
    floors = floors - 1
    time.sleep(0.1)
