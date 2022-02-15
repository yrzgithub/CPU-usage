import file_path_adder
from psutil import virtual_memory
from playsound import playsound
from time import sleep

while 1:
    sleep(1)
    ram = virtual_memory().percent
    print(ram)
    if ram > 9:
        print("CPU usage is high")
