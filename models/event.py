from enums.status import Status
from enums.mission import Mission
from enums.devices import Devices
from modules.event_generator.random_date_generator import RandomDateGenerator
from datetime import datetime

import random

class Event:
  date: datetime
  mission: Mission 
  device_type: Devices = Devices.UNKNOWN
  device_status: Status = Status.UNKNOWN
  hash: str = ""
  values: dict
  
  __device_categories = [device for device in Devices if device != Devices.UNKNOWN]
  
  def __init__(self, date: str, mission: Mission, device_type: Devices, device_status: Status, hash: str):
      self.date = date
      self.mission = mission
      self.device_type = device_type
      self.device_status = device_status
      self.hash = hash
  
  def __init__(self):
    self.date = RandomDateGenerator()
    self.mission = random.choice(list(Mission))
    if self.mission.value != Mission.UNKN.value:
     self.device_type = random.choice(self.__device_categories)
     self.device_status = random.choice(list(Status))
     self.hash = hash((
                "date", self.date,
                "mission", self.mission,
                "device_type", self.device_type,
                "device_status", self.device_status))
    self.values = {
      "date": str(self.date),
      "mission": self.mission.name,
      "device_type": self.device_type.name,
      "device_status": self.device_status.name,
      "hash": self.hash
     }
  
  def __str__(self):
        return f'date: {self.date},\nmission: {self.mission.name},\ndevice_type: {self.device_type.name},\ndevice_status: {self.device_status.name},\nhash: {str(self.hash)}'

