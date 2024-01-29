from modules.report_generator.stats_generator import StatsGenerator

class ReportWriter: 
    stats_generator: StatsGenerator
    date: str
    
    def __init__(self, stats_generator, date):
        self.date = date
        self.stats_generator = stats_generator
    
    def write_report(self):
        with open('./reports/' + f"APLSTATS-[REPORT]-{self.date}.log", 'a') as f:
            f.write("******************************************" + '\n')
            f.write("*                 STATS                  *" + '\n')
            f.write("******************************************" + '\n')
            for i in range(2):
                f.write('\n')
            f.write("EVENTS BY MISSION AND DEVICE" + '\n')
            for mission in self.stats_generator.generate_stats():
                f.write(f"------------------{mission[0]}------------------" + '\n')
                f.write(f"Total Events: {mission[3]}" + '\n')
                f.write('Status:' + '\n')
                for status in mission[1]:
                    f.write(f" {status} = {str(mission[1][status])}" '\n')
                f.write('Devices:' + '\n')
                for devices in mission[2]:
                    f.write(f" {devices} = {str(mission[2][devices])}" '\n')
            for i in range(3):
                f.write('\n')
            f.write("DEVICES FAILING THE MOST BY MISSION" + '\n')
            for mission in self.stats_generator.get_max_devices_unknown_status():
                f.write(f"------------------{mission[0]}------------------" + '\n')
                f.write(f"{mission[1][0]} = {mission[1][1]}" + '\n')
            for i in range(3):
                f.write('\n')
            f.write(f"KILLED DEVICES: {self.stats_generator.get_total_killed_devices()}" + '\n')