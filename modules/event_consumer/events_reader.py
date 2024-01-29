from models.event import Event
from os import walk
from modules.event_consumer.file_reader import FileReader
from enums.status import Status
from enums.mission import Mission
from enums.devices import Devices
import json

class EventsReader:
    
    def read_events():
        filenames = next(walk("./devices/"), (None, None, []))[2]  # [] if no file
        files_content = []
        for f in filenames:
            content = FileReader.read_files("./devices/" + f)
            files_content.append(content)
            
        event_list = []
        for f in files_content:
            event_content = json.loads(f)
            event = Event()
            event.date = event_content["date"]
            event.mission = Mission(event_content["mission"].lower())
            event.device_type = Devices(event_content["device_type"])
            event.device_status = Status(event_content["device_status"].lower())
            event.hash = event_content["hash"]
            event_list.append(event)
            
    
        return event_list