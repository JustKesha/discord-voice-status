import json
import modules
import utils

def main(dumps_indent = None) -> int:
    print("Starting...")

    print("Loading config...")
    try:
        config = utils.load_config()
        dumps_indent = config["logging"]["dumps_indent"]
    except FileNotFoundError:
        filename: str = utils.config.Default.YAML
        filepath: str = utils.config.Default.ROOT
        print(f"Couldnt find the \"{filename}\" file at \"{filepath}\"")
        return -1
    print(f"Status: {json.dumps(config['status'], indent=dumps_indent)}")

    print("Initializing Discord API...")
    modules.init_discord_api()
    print(f"Api: {json.dumps(config['api'], indent=dumps_indent)}")

    print("Starting the main loop...")
    print(f"Loop stopped with return code {loop(config)}")

    return 1

def iter(config: utils.Config) -> int:
    dumps_indent = config["logging"]["dumps_indent"]
    status = config["status"]
    record = config["recording"]

    print("Recording...")
    try:
        audio = modules.record_audio(
            duration_sec = status["update_interval"],
            source = modules.sr.Microphone(record["device_index"])
        )
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -1
    # TODO Should instead always record in the background
    print("Finished audio recording") 

    print("Running speech recognision...")
    try:
        text = modules.sound_to_text(
            audio,
            language = status["language"]
            )
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -2
    print(f"Raw result: \"{text}\"")
    
    print("Running filter...")
    try:
        if status["filter"]:
            text = modules.filter(
                text,
                status["language"],
                censor_mode=status["censor_mode"]
                )
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -3
    print(f"Result: \"{text}\"")
    
    print("Requesting Discord API...")
    try:
        response = modules.set_custom_status(
            text,
            status["emoji"]
            )
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -4
    if "code" in response:
        log_response = json.dumps(response, indent=dumps_indent)
        print(f"Discord responded with: {log_response}")
        return -4
    log_status = json.dumps(response["custom_status"], indent=dumps_indent)
    print(f"Updated your Discord status to: {log_status}")

    return 1

def loop(config: utils.Config) -> int:
    while True:
        iteration_return_code = iter(config)
        if iteration_return_code != 1:
            return iteration_return_code

if __name__ == "__main__":
    main()