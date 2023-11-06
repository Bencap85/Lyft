from battery.battery import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init_(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        if((datetime.today() - self.last_service_date).years > 4):
            return True
        else:
            return False