from models.event import Event
import json

class FileWriter:

  def write(event: Event, file_name):
      with open('./devices/' + file_name, 'a') as f:
          #f.write(str(event) + '\n')
          f.write(json.dumps(event.values) + '\n')