import json
import modules
import utils

def main() -> int:
    print("Starting...")

    print("Loading config...")
    try:
        config = utils.load_config()
        status = config["status"]
        language = config.get("env", {}).get("LANGUAGE", "en")
        print(f"Language from config: {language}")
    except FileNotFoundError:
        print(f"Couldnt find the \"{utils.config.Default.YAML}\" file at \"{utils.config.Default.ROOT}\"")
        return -1
    print("Config file found")
    print(f"Status: {status}")

    print("Starting the main loop...")
    result = loop(config)
    print(f"Loop stopped with return code {result}")

    return 1

def loop(config: dict) -> int:
    status: dict = config["status"]

    while True:
        print("Recording...")
        try:
            audio = modules.record_audio(
                duration_sec = status["update_interval"]
            )
        except Exception as error:
            print(f"Something went wrong: \"{error}\"")
        # TODO Should instead always record in the background
        print("Finished audio recording") 
        print("Running speech recognision...")
        try:
            text = modules.sound_to_text(audio)
        except Exception as error:
            print(f"Something went wrong: \"{error}\"")
            return -1
        print(f"Raw result: \"{text}\"")
        
        print("Running filter...")
        try:
            text = filter(text, language)
        except Exception as error:  
            print(f"Something went wrong: \"{error}\"")
            return -1
        print(f"Result: \"{text}"\") 
        
        print("Requesting Discord API...")
        try:
            response = modules.set_custom_status(text)
        except Exception as error:
            print(f"Something went wrong: \"{error}\"")
            return -1
        if "code" in response:
            print(F"Discord responded with: {json.dumps(response, indent=2)}")
            return -1
        response_custom_status = response["custom_status"]
        print(f"Updated your Discord status to: {json.dumps(response_custom_status, indent=2)}")

    return 1

if __name__ == "__main__":
    print(f"Main returned {main()}")