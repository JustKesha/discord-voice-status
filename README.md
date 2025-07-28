# Discord Voice Status Updater

Small Python application that updates your Discord custom status in real-time using your voice input & speech recognition to display what you're currently talking about.

### Features

- Fully configurable
- Converts your speech to text in real-time
- Updates your Discord status in the background with what you said

### Requirements

- Discord account
- Microphone for voice input
- Python 3.10 or higher

### Safety

While this uses the same technology as clients like Vencord or BetterDiscord which have remained undetected, Discord technically prohibits automated status updates. Use at your own risk.

> [!NOTE]
> We are using a message filter to make sure no naughty words accidentally slip into your discord status.

## Installation

1. Clone or install this repository:<br>
`git clone https://github.com/JustKesha/discord-voice-status.git`<br>
`cd discord-voice-status`

2. Install the required dependencies:<br>
`pip install -r requirements.txt`

3. Set up your configuration (see [Configuration section](#configuration) below)

## Configuration

There are two steps in configuration:

### Step 1:

Create a `.env` file in the root directory with your token:
```env
PY_DVS_DISCORD_TOKEN=paste_your_token_here
```

#### Getting Your Discord Token

Follow any of these guides to get your Discord token:<br>
https://www.youtube.com/results?search_query=how+to+get+discord+token

> [!WARNING]
> Never share your token or `.env` file with anyone!

### Step 2:

Edit the config.yaml file with your preferred settings:

```yaml
# Discord Custom Status
status:
  language: "en"
  filter: on
  censor_mode: "first_last_visible" # Can be "full", "first_last_visible" or "first_visible"
  update_interval: 10.0 # Seconds (Do not set below 4 seconds, 10-30 recommended)

# Input Settings
recording:
  device_index: NULL # Set to null to use default mic, otherwise 0-N
```

#### Config Parameters

| Parameter | Description | Accepted Values | Example |
|-|-|-|-|
| language | Language to use for speech recognition & filter | ISO 639 language code | `"en"` |
| filter | Whether or not to use naughty words filter,<br>Currently supports the following languages: `"en"`, `"ru"` | Boolean: `on`/`off` | `on` |
| censor_mode | Censoring mode to use for filter | `"full"`, `"first_last_visible"` or `"first_visible"` | `"first_visible"` |
| update_interval | How long each speech recording will take in seconds | Float: `1.0` - `30.0` | `6.0` |
| device_index | Preferred microphone's [device index](#getting-device-index) (0-N), use `NULL` for default | `0`, `1`, `2` ... or `NULL` | `NULL` |

#### Getting Device Index

Device index is a number from 0-N, where N is the total number of connected devices.<br>
On windows you can get it by simply clicking RMK on your microphone / sound icon on the bottom right, then going to "Sounds" → "Recording" → Find your active microphone.
Under the name it should controller information with device index at the start of the line, like so: `10- USB PnP Audio Device`, `10` here is the device index.

## Usage

To start the bot, run from root:
`python src/main.py`

The bot will:
1. Start listening to your microphone
2. Once set time is out, run speech recognition
3. Request Discord's API to set your custom status with resulting message
4. Repeat until program terminated

### Troubleshooting

- Make sure you're using Python 3.10 or higher
- Verify that your configuration and Discord token are correct
- Make sure the application is using the correct device
- If status updates stop working, restart the bot

## Contributing

Want to help develop this project? Check out the [Issues tab](../../issues)!

Please follow these guidelines when contributing:
- Keep code style consistent
- Update documentation if needed
- Add any important values to config
- Test your changes thoroughly

## Other

### Rate Limits

Discord has strict rate limits for status updates:
- Maximum 1 update per 4 seconds (hard limit)
- Recommended update interval: 10-30 seconds
- Maximum custom status length: 128 characters

The bot automatically handles these limits based on your config.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Support

To support the project, just open an issue on GitHub to describe problems with your experience!

