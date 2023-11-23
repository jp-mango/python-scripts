import platform
import psutil


def get_system_info():
    info = {
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "CPU Count": psutil.cpu_count(logical=False),
        "Total Physical Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
        "Memory Usage": f"{psutil.virtual_memory().percent}%",
        "Disk Total": f"{psutil.disk_usage('C:\\').total / (1024**3):.2f} GB",
        "Disk Used": f"{psutil.disk_usage('C:\\').used / (1024**3):.2f} GB",
        "Disk Usage": f"{psutil.disk_usage('C:\\').percent}%",
    }
    return info


def display_info(info):
    for key, value in info.items():
        print(f"{key}: {value}")


# Get and display system information
system_info = get_system_info()
display_info(system_info)
