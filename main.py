import os
from subprocess import call

import time

def main():
    setting_keys = [
        "FRITZ_IP_ADDRESS",
        "FRITZ_USERNAME",
        "FRITZ_PASSWORD",
        "SAMPLE_PERIOD"
    ]
    # Check if all environment keys are suplied and if they aren't end the program via an exception
    missing_keys = [key for key in setting_keys if key not in os.environ]
    if len(missing_keys) > 0:
        raise Exception(f"You need to supply the environment variable(s): {', '.join(missing_keys)}")
    # Extract the settings into a dictionary
    settings = {key: os.environ[key] for key in setting_keys}

    # Set the sample period variable
    SAMPLE_PERIOD = float(settings["SAMPLE_PERIOD"])

    start = time.time()
    while True:
        call("python" + " telegrafFritzBox.py ", shell=True)
        call("python" + " telegrafFritzSmartHome.py ", shell=True)

    
        # Sleep the appropriate amount of time
        time.sleep(SAMPLE_PERIOD - (time.time()-start)%SAMPLE_PERIOD)

if __name__ == "__main__":
    main()
