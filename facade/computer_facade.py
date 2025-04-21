class CPU:
    def power_on(self):
        return "CPU powered on"
    
    def execute_boot_sequence(self):
        return "CPU executing boot sequence"

class Memory:
    def initialize(self):
        return "RAM initialized"
    
    def load_kernel(self):
        return "Kernel loaded into memory"

class HardDrive:
    def read_boot_sector(self):
        return "Reading boot sector from drive"
    
    def load_os_files(self):
        return "Loading OS files"

class ComputerFacade:
    def __init__(self, cpu, memory, hard_drive):
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive
    
    def start(self):
        results = []
        results.append(self.cpu.power_on())
        results.append(self.memory.initialize())
        results.append(self.hard_drive.read_boot_sector())
        results.append(self.cpu.execute_boot_sequence())
        results.append(self.memory.load_kernel())
        results.append(self.hard_drive.load_os_files())
        return "\n".join(results)