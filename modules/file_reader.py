
class FileReader:
    def get_config_params():
        with open('config.yaml', 'r') as file:
            config_params =  file.read().strip().split('\n')
            config_params = list(map(lambda x: x.split(' ')[1], config_params))
            return config_params
        
    def read_files(file_name):
        with open(file_name, 'r') as file:
            return file.read()
            # return file.read().strip().split('\n')
