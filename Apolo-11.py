from modules.event_generator.generator import Generator
from modules.event_consumer.events_reader import EventsReader


Generator.generate_events()

EventsReader.read_events()
