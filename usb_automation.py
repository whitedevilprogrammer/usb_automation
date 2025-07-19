import os
class Usb_Automation:
    def __init__(self):
        self.this_is_my_usb = False
        
    def First_level_security(self):
        while not self.this_is_my_usb:
            v = os.popen('wmic logicaldisk where drivetype=2 get description, volumename, volumeserialnumber, size').readlines()
            for i in v:
                if 'Removable Disk  30748426240  MY NAME     C6A7547D            \n' == i:
                    self.this_is_my_usb = True
                    os.startfile('E:/java.txt')
                    
start = Usb_Automation()
start.First_level_security()


        
        


