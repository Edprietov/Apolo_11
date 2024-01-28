import models.event as ev
from modules.file_writer import FileWriter
from modules.event_generator.file_name_builder import FileNameBuilder
from modules.event_consumer.file_reader import FileReader

class Generator:

    def generate_events():
        file_writer :FileWriter = FileWriter
        file_name_builder :FileNameBuilder = FileNameBuilder()
        config_params = FileReader.get_config_params()

        for i in range (0, int(config_params[0])):
            event = ev.Event()
            file_writer.write(event, file_name_builder.build_name(event))