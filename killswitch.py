import subprocess, time, os

def main_choice():
    mainchoice = input("Do you want to use the default settings? y/n: ")
    if mainchoice == "y":
        tmeout = 10
        rebsec = 0
        print("Settings Set - Starting")
    elif mainchoice == "n":
        tmeout = int(input("Ping timeout time: "))
        rebsec = int(input("Reboot Time: "))

        print("Settings Set - Starting")
    return tmeout, rebsec

def ping_google(tmeout, rebsec):
    try:
        result = subprocess.run(['ping', '8.8.8.8', '-c', '4'], capture_output=True,
                                text=True, timeout=tmeout)
        if result.returncode == 0:
            print("Ping successful!")
        else:
            print(f"Ping failed - Rebooting in {rebsec} seconds")
            time.sleep(rebsec)
            os.system('systemctl reboot')

    except subprocess.TimeoutExpired:
        print(f"Ping timed out after {tmeout} seconds - Rebooting in {rebsec} seconds")
        time.sleep(rebsec)
        os.system('systemctl reboot')

    while True:
        ping_google(tmeout, rebsec)
        time.sleep(60)

if __name__ == "__main__":
    tmeout, rebsec = main_choice()
    ping_google(tmeout, rebsec)
