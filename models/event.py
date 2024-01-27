from enums.status import Status
from enums.mission import Mission
from enums.devices import Devices
from datetime import datetime

import random

class Event:
  date: datetime
  mission: Mission 
  device_type: Devices = Devices.UNKN
  device_status: Status = Status.UNKNOWN
  hash: str = ""
  
  __device_categories = [device for device in Devices if device != Devices.UNKN]
  
  def __init__(self):
    self.date = datetime.now()
    self.mission = random.choice(list(Mission))
    if self.mission.value != Mission.UNKN.value:
     self.device_type = random.choice(self.__device_categories)
     self.device_status = random.choice(list(Status))
     self.hash = hash((
                "date", self.date,
                "mission", self.mission,
                "device_type", self.device_type,
                "device_status", self.device_status))
  
  def __str__(self):
        return f'date= {self.date}\nmission= {self.mission.name}\ndevice=type= {self.device_type.name}\ndevice_status= {self.device_status.name}\nhash= {str(self.hash)}'

