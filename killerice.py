import subprocess
import os

def ping_google():
    try:
        result = subprocess.run(['ping', 'google.com', '-c', '4'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("Ping successful!")
        else:
            print("Ping failed.")
            os.system('reboot')
    except subprocess.TimeoutExpired:
        print("Timeout: Ping took too long.")

        # Add an infinite loop
        while True:
            ping_google()
            time.sleep(60)  # Wait for 60 seconds before the next ping attempt
