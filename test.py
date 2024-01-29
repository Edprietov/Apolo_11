import random


files_to_generate = random.randint(1,15)

time_to_simulate = 20

for i in range(files_to_generate):
    with open('./reports/' + f"SOME-{i}.log", 'a') as file:
        file.write("******************************************" + '\n')
        file.write("*                 STATS                  *" + '\n')





#with open('config.yaml', 'r') as file:
    #config_params =  file.read().strip().split('\n')
    #config_params = list(map(lambda x: x.split(' ')[1], config_params))
