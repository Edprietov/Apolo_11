from models.counter import Counter
from models.event import Event
from enums.mission import Mission

class FileNameBuilder:
    counter = Counter()
    
    def build_name(self, event: Event):
        if event.mission == Mission.CLNM:
            self.counter.clnm_count += 1
            return f"APL[{str(event.mission.name)}]-{self.counter.clnm_count:08d}.log"
        elif event.mission == Mission.GALXONE:
           self.counter.galxone_count += 1
           return f"APL[{str(event.mission.name)}]-{self.counter.galxone_count:08d}.log"  
        elif event.mission == Mission.ORBONE:
            self.counter.orbone_count += 1 
            return f"APL[{str(event.mission.name)}]-{self.counter.orbone_count:08d}.log"
        elif event.mission == Mission.TMRS:
            self.counter.tmrs_count += 1 
            return f"APL[{str(event.mission.name)}]-{self.counter.tmrs_count:08d}.log"
        else: 
            self.counter.unkn_count += 1
            return f"APL[{str(event.mission.name)}]-{self.counter.unkn_count:08d}.log"