import models.event as ev
from modules.file_writer import FileWriter
from modules.file_name_builder import FileNameBuilder
from modules.file_reader import FileReader
from os import walk
import json

def generate_events():
  file_writer :FileWriter = FileWriter
  file_name_builder :FileNameBuilder = FileNameBuilder()
  config_params = FileReader.get_config_params()

  for i in range (0, int(config_params[0])):
      event = ev.Event()
      file_writer.write(event, file_name_builder.build_name(event))

generate_events()

def read_events():
  filenames = next(walk("./devices/"), (None, None, []))[2]  # [] if no file
  files_content = []
  for f in filenames:
    content = FileReader.read_files("./devices/" + f)
    files_content.append(content)
    
  lists = []
  for f in files_content:
    json_object = json.loads(f)
    print(type(json_object))
    lists.append(json_object)
  
  print(lists)

read_events()
