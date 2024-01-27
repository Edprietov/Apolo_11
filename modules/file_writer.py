from models.event import Event

class FileWriter:

  def write(event: Event, file_name):
      with open(file_name, 'a') as f:
          f.write(str(event) + '\n')