from modules.file_writer import FileWriter
from modules.event_generator.file_name_builder import FileNameBuilder
from modules.event_consumer.file_reader import FileReader
from datetime import datetime
import models.event as ev
import math
import random
import time


class Generator:

    def generate_events():
        file_writer :FileWriter = FileWriter
        file_name_builder :FileNameBuilder = FileNameBuilder()
        config_params = FileReader.get_config_params()
        
        generated_files = 0

        files_to_generate = random.randint(int(config_params[2]),int(config_params[1]))
        time_to_simulate = int(config_params[2])

        delta = time_to_simulate/files_to_generate
        files_number = 1
        now = datetime.now()
        if delta < 1:
            delta = 1
            files_number = int(math.ceil(files_to_generate/time_to_simulate))
        else:
         delta = int(delta)
    
        while generated_files < files_to_generate:
            for i in range (files_number):
                event = ev.Event()
                file_writer.write(event, file_name_builder.build_name(event))
            time.sleep(delta)
            generated_files += files_number