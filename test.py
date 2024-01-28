
with open('config.yaml', 'r') as file:
    config_params =  file.read().strip().split('\n')
    config_params = list(map(lambda x: x.split(' ')[1], config_params))
