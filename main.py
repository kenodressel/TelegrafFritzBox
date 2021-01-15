def main():
    setting_keys = [
        "FRITZ_ADDRESS",
        "FRITZ_USERNAME",
        "FRITZ_PASSWORD",
        "TELEGRAF_HOSTNAME",
        "TELEGRAF_PORT",
        "SAMPLE_PERIOD"
    ]
    # Check if all environment keys are suplied and if they aren't end the program via an exception
    missing_keys = [key for key in setting_keys if key not in os.environ]
    if len(missing_keys) > 0:
        raise Exception(f"You need to supply the environment variable(s): {', '.join(missing_keys)}")
    # Extract the settings into a dictionary
    settings: Dict[str, Any] = {key: os.environ[key] for key in setting_keys}
    
    # Print information about the current configuration
    print("Current configuration:")
    for key, value in settings.items():
        # The still leaks the length of the password to the log but I don't think that really matters
        censored_value = '*'*len(value) if "PASSWORD" in key else value
        print(f"\t{key}={censored_value}")
    print()
    
    # Create the telgraf client, this pip library doesn't really do much
    telegraf_client = TelegrafClient(
        host=settings["TELEGRAF_HOSTNAME"],
        port=int(settings["TELEGRAF_PORT"]))
    
    # Set the sample period variable
    SAMPLE_PERIOD = float(settings["SAMPLE_PERIOD"])
    print()
    print(f"Starting to poll metrics every {SAMPLE_PERIOD} seconds")
    
    while True:
        # Send the collected data to telegraf
        telegraf_client.metric("router", data)

        # Print the data depending on the settings
        if settings["PRINT_DATA"]:
            print(data)
    
        # Sleep the appropriate amount of time
        time.sleep(SAMPLE_PERIOD - (time.time()-start)%SAMPLE_PERIOD)

if __name__ == "__main__":
    main()
