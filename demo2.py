# Simple CapScan Starter Code - Easy to Understand

import psutil  # Library to get system information like drives

def scan_devices():
    print("=== CapScan: Basic Storage Scanner ===\n")

    # Get list of connected storage partitions
    partitions = psutil.disk_partitions()

    if not partitions:
        print("No storage devices found.")
        return

    # Loop through each detected storage device
    for p in partitions:
        print(f"Device Path     : {p.device}")
        print(f"Mount Location  : {p.mountpoint}")
        print(f"File System Type: {p.fstype}")

        try:
            # Get usage details like total, used and free space
            usage = psutil.disk_usage(p.mountpoint)
            total_gb = round(usage.total / (1024**3), 2)
            used_gb = round(usage.used / (1024**3), 2)
            free_gb = round(usage.free / (1024**3), 2)

            print(f"Total Space     : {total_gb} GB")
            print(f"Used Space      : {used_gb} GB")
            print(f"Free Space      : {free_gb} GB")
        except PermissionError:
            print("⚠ Unable to access this drive due to permission issue.")

        print("-" * 50)  # Just a separator line

# Start point of the program
scan_devices()
