import os

class BasicOperatingSystem:
    def __init__(self):
        self.processes = []
        self.memory = {}
        self.filesystem = {}

    def create_process(self, process_id, process_data):
        self.processes.append({'id': process_id, 'data': process_data})
        print(f"Process {process_id} created.")

    def allocate_memory(self, process_id, memory_size):
        if process_id not in self.memory:
            self.memory[process_id] = memory_size
            print(f"Allocated {memory_size}MB memory to process {process_id}.")
        else:
            print(f"Process {process_id} already has allocated memory.")

    def create_file(self, filename, content):
        self.filesystem[filename] = content
        print(f"File {filename} created with content: {content}")

    def read_file(self, filename):
        if filename in self.filesystem:
            print(f"Reading file {filename}: {self.filesystem[filename]}")
        else:
            print(f"File {filename} not found.")

    def list_processes(self):
        print("Current processes:")
        for process in self.processes:
            print(f"Process ID: {process['id']}, Data: {process['data']}")

    def list_files(self):
        print("Current files:")
        for filename in self.filesystem:
            print(f"Filename: {filename}, Content: {self.filesystem[filename]}")


# some os operations. create process, allocate memory, create file, read file, list processes, list files
# change to your liking
os = BasicOperatingSystem()
os.create_process(1, "Process 1 data")
os.allocate_memory(1, 256)
os.create_file("file1.txt", "Hello, World!")
os.read_file("file1.txt")
os.list_processes()
os.list_files()
