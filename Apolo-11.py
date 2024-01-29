from modules.event_generator.generator import Generator
from modules.event_consumer.events_reader import EventsReader
from modules.report_generator.stats_generator import StatsGenerator
from modules.report_generator.report_writer import ReportWriter
from datetime import datetime

import os
import shutil


simulation_number: int = 1
os.mkdir(f"./reports")
os.mkdir(f"./backup")
os.mkdir(f"./devices")

for i in range(5):

    date: str = datetime.now().strftime("%d%m%Y%H%M%S")

    Generator.generate_events()

    events_list = EventsReader.read_events()
        
    stats_generator = StatsGenerator(events_list)

    report_writer = ReportWriter(stats_generator, date)

    report_writer.write_report()

    os.mkdir(f"./backup/Simulation_{simulation_number}")

    file_names = os.listdir("./devices")
        
    for file_name in file_names:
        shutil.move(os.path.join("./devices", file_name), f"./backup/Simulation_{simulation_number}")

    simulation_number += 1