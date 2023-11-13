from battery.battery import Battery
from datetime import date, datetime, timedelta

class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        if((datetime.today().date() - self.last_service_date).days >= 720):
            return True
        else:
            return False