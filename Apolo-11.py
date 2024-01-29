from modules.event_generator.generator import Generator
from modules.event_consumer.events_reader import EventsReader
from modules.event_consumer.file_reader import FileReader
from modules.report_generator.stats_generator import StatsGenerator
from modules.report_generator.report_writer import ReportWriter
from modules.cleaner.cleaner import Cleaner
from datetime import datetime


simulation_number: int = 1

Cleaner.do_initial_cleanup()

while FileReader.get_config_params()[3] != 'true':

    date: str = datetime.now().strftime("%d%m%Y%H%M%S")

    event_builder = Generator()
    print("******************************************" + '\n')
    print(f"Simulation: {simulation_number} \n")
    print(f" Files to generate: {event_builder.files_to_generate} \n")
    print(f" Simulation time: {event_builder.time_to_simulate} \n")
    
    event_builder.generate_events()

    events_list = EventsReader.read_events()
        
    stats_generator = StatsGenerator(events_list)

    report_writer = ReportWriter(stats_generator, date, simulation_number)

    report_writer.write_report()
    
    print(f"Report generated: {report_writer.report_name} \n\n")
    
    Cleaner.do_cleanup(simulation_number)

    simulation_number += 1
    