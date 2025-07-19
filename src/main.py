import json
import modules
import utils

def main() -> int:
    print("Starting...")
    dumps_indent = 2

    print("Loading config...")
    try:
        config = utils.load_config()
    except FileNotFoundError:
        print(f"Couldnt find the \"{utils.config.Default.YAML}\" file at \"{utils.config.Default.ROOT}\"")
        return -1
    print(f"Status: {json.dumps(config['status'], indent=dumps_indent)}")

    print("Initializing Discord API...")
    modules.init_discord_api()
    print(f"Api: {json.dumps(config['api'], indent=dumps_indent)}")

    print("Starting the main loop...")
    print(f"Loop stopped with return code {loop(config)}")

    return 1

def iter(config: dict) -> int:
    status: dict = config["status"]
    record: dict = config["recording"]
    
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
        text = modules.sound_to_text(audio, language = status["language"])
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -2
    print(f"Raw result: \"{text}\"")
    
    print("Running filter...")
    try:
        if status["filter"]:
            text = modules.filter(text, status["language"])
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -3
    print(f"Result: \"{text}\"")
    
    print("Requesting Discord API...")
    try:
        response = modules.set_custom_status(text)
    except Exception as error:
        print(f"Something went wrong: \"{error}\"")
        return -4
    if "code" in response:
        print(F"Discord responded with: {json.dumps(response, indent=2)}")
        return -4
    response_custom_status = response["custom_status"]
    print(f"Updated your Discord status to: {json.dumps(response_custom_status, indent=2)}")

    return 1

def loop(config: dict) -> int:
    while True:
        iteration_return_code = iter(config)
        if iteration_return_code < 0:
            return iteration_return_code

if __name__ == "__main__":
    main()