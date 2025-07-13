# Discord Voice Status Updater

A Python script that updates your Discord custom status in real-time with your voice input using speech recognition.

### Features

- Converts your speech to text in real-time
- Updates your Discord custom status automatically
- Configurable update interval to respect rate limits
- Supports both YAML config and .env file for token storage
- Lightweight with minimal dependencies

### Requirements

- Python 3.10.11 or higher
- Discord account
- Microphone for voice input

### Safety

While this uses the same technology as clients like Vencord or BetterDiscord which have remained undetected, Discord technically prohibits automated status updates. Use at your own risk.

## Installation

1. Clone this repository:<br>
`git clone https://github.com/JustKesha/discord-voice-status.git`<br>
`cd discord-voice-status`

4. Install the required dependencies:<br>
`pip install -r requirements.txt`

6. Set up your configuration (see [Configuration section](#configuration) below)

## Configuration

There are two ways to configure the bot:

### Method 1: Using config.yaml

Edit the config.yaml file with your preferred settings:

```yaml
# Discord Custom Status
status:
  update_interval: 10.0 # Seconds (Do not set below 4 seconds, 10-30 recommended)

# Environment Variables
# (If not specified here, will try to load from a .env file in the same directory)
env:
  DISCORD_TOKEN: "your_token_here"
```

### Method 2: Using .env file

Create a .env file in the root directory with your token:
```env
PY_TDS_DISCORD_TOKEN=your_token_here
```

### Getting Your Discord Token

Follow any of these guides to get your Discord token:
https://www.youtube.com/results?search_query=how+to+get+discord+token

> [!WARNING]
> Never share your token with anyone!

## Usage

To start the bot, run from the root directory:
`python src/main.py`

The bot will:
1. Start listening to your microphone
2. Once set time is out, run speech recognition
3. Request Discord's API to set your custom status with resulting message
4. Repeat unitl program terminated

### Troubleshooting

- Make sure you're using Python 3.10.11 or higher
- Verify your configuration and Discord token are correct
- Check your microphone permissions
- Ensure no other applications are using your microphone
- If status updates stop working, restart the bot

## Contributing

Want to help develop this project? Check out the [Issues tab](../../issues)!

Please follow these guidelines when contributing:
- Keep code style consistent
- Update documentation if needed
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

