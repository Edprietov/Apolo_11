from enum import Enum

class Status(Enum):

    EXCELLENT = "excellent"

    GOOD = "good"

    WARNING = "warning"
    
    FAULTY = "faulty"
    
    KILLED = "killed"
    
    UNKNOWN = "unknown"