# blueprint/blueprint 

import os

class utilities:
    def show_disk_space(self):
        print(os.system("df -h"))
    
    def show_ram(self):
        print(os.system("free -h"))

    def show_system_details(self):
        print(os.uname_result().sysname)


machine_a = utilities()  # object
machine_a.show_disk_space()

machine_b = utilities() # object 2
machine_b.show_ram()