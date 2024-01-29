from enums.mission import Mission
from enums.status import Status
from enums.devices import Devices

class StatsGenerator:
    events: list
    devices_failing: dict
    
    
    def __init__(self, events):
        self.events = events
        
    
    def generate_stats(self):
        stats_list = []
        for mission in Mission:
            list = self.__get_status_by_mission(mission.name)
            stats_list.append([mission.name, self.__get_status(list), self.__get_devices(list), len(list)])
        return stats_list
    
    def get_total_killed_devices(self):
        count: int = 0 
        for event in self.events:
             if event.device_status == Status.KILLED:
                 count += 1
        return count         
    
    def get_max_devices_unknown_status(self):
        list = []
        missions = [mission for mission in Mission if mission != Mission.UNKN]
        for mission in missions:
            list.append([mission.name, self.__find_max_failures_by_mission(mission.name)])
        
        return list
    
    
    def __get_status_by_mission(self, mission: str):
        list = []
        for event in self.events:
            if event.mission.name == mission:
                list.append(event)
        return list
    
    def __get_status(self, event_list: list):
        excellent_count = 0
        good_count = 0
        warning_count = 0
        killed_count = 0
        unknown_count = 0
        for event in event_list:
            if event.device_status == Status.EXCELLENT:
                excellent_count += 1
            elif event.device_status == Status.GOOD:
                good_count += 1
            elif event.device_status == Status.WARNING:
                warning_count += 1
            elif event.device_status == Status.KILLED:
                killed_count += 1
            elif event.device_status == Status.UNKNOWN:
                unknown_count += 1
        return {Status.EXCELLENT.name: excellent_count,
                Status.GOOD.name: good_count,
                Status.WARNING.name: warning_count,
                Status.KILLED.name: killed_count,
                Status.UNKNOWN.name: unknown_count}
    
    def __get_devices(self, event_list: list):
        satellites_count = 0
        spacecraft_count = 0
        suits_count = 0
        space_vehicles_count = 0
        for event in event_list:
            if event.device_type == Devices.SATELLITES:
                satellites_count += 1
            elif event.device_type == Devices.SPACECRAFT:
                spacecraft_count += 1
            elif event.device_type == Devices.SUITS:
                suits_count += 1
            elif event.device_type == Devices.SPACE_VEHICLES:
                space_vehicles_count += 1
        return {Devices.SATELLITES.name: satellites_count,
                Devices.SPACECRAFT.name: spacecraft_count,
                Devices.SUITS.name: suits_count,
                Devices.SPACE_VEHICLES.name: space_vehicles_count}
        
    
    def __find_max_failures_by_mission(self, mission_name: str):
        satellites_count = 0
        spacecraft_count = 0
        suits_count = 0
        space_vehicles_count = 0
        for event in self.events:
            if event.mission.name == mission_name and event.device_status == Status.UNKNOWN:
                if event.device_type == Devices.SATELLITES:
                    satellites_count += 1
                elif event.device_type == Devices.SPACECRAFT:
                    spacecraft_count += 1
                elif event.device_type == Devices.SUITS:
                    suits_count += 1
                elif event.device_type == Devices.SPACE_VEHICLES:
                    space_vehicles_count += 1
        final = {Devices.SATELLITES.name: satellites_count,
                Devices.SPACECRAFT.name: spacecraft_count,
                Devices.SUITS.name: suits_count,
                Devices.SPACE_VEHICLES.name: space_vehicles_count}
        return max(final.items(), key=lambda x: x[1])