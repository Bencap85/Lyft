from battery.battery import Battery
from datetime import datetime, timedelta

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        if((datetime.today() - self.last_service_date).days > 730):
            return True
        else:
            return False