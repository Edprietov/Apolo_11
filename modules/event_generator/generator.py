from modules.file_writer import FileWriter
from modules.event_generator.file_name_builder import FileNameBuilder
from modules.event_consumer.file_reader import FileReader
from datetime import datetime
import models.event as ev
import math
import random
import time


class Generator:
    files_to_generate: int
    time_to_simulate: int
    
    def __init__(self):
        config_params = FileReader.get_config_params()

        self.files_to_generate = random.randint(int(config_params[1]),int(config_params[2]))
        self.time_to_simulate = int(config_params[0])

    def generate_events(self):
        file_writer :FileWriter = FileWriter
        file_name_builder :FileNameBuilder = FileNameBuilder()
        
        generated_files = 0
        delta = self.time_to_simulate/self.files_to_generate
        files_number = 1
    
        if delta < 1:
            delta = 1
            files_number = int(math.ceil(self.files_to_generate/self.time_to_simulate))
        else:
         delta = int(delta)
    
        while generated_files < self.files_to_generate:
            for i in range (files_number):
                event = ev.Event()
                file_writer.write(event, file_name_builder.build_name(event))
            time.sleep(delta)
            generated_files += files_number