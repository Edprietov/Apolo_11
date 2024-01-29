from modules.event_generator.generator import Generator
from modules.event_consumer.events_reader import EventsReader
from modules.report_generator.stats_generator import StatsGenerator
from modules.report_generator.report_writer import ReportWriter
from datetime import datetime
from models.event import Event
from enums.mission import Mission
from enums.status import Status
from enums.devices import Devices


date = datetime.now().strftime("%d%m%Y%H%M%S")

Generator.generate_events()

events_list = EventsReader.read_events()
    
stats_generator = StatsGenerator(events_list)

report_writer = ReportWriter(stats_generator, date)

report_writer.write_report()

