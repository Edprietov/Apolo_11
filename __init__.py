import models.event as ev
from modules.file_writer import FileWriter

def main():
  file_writer :FileWriter = FileWriter
  event_list :list = []
  for i in range (0, 10):
      event = ev.Event()
      event_list.append(event)

  for event in event_list:
    file_writer.write(event, f"APL[{str(event.mission.name)}-{str(event.hash)}].txt")

main()


