# Voice Enhancer Bot
Voice Enhancer Bot is a Telegram bot that processes audio files to enhance their quality using various audio effects. The bot uses the `pedalboard` library from Spotify for audio processing and `pydub` for audio format conversion.

## Features

- Noise Gate
- Compressor
- Low Shelf Filter
- Gain

## Prerequisites

- Docker
- Telegram Bot Token

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/voiceEnhancer.git
    cd voiceEnhancer
    ```

2. Create a `config.py` file with your Telegram bot token and whitelist of user IDs:
    ```python
    # config.py
    TOKEN = 'your-telegram-bot-token'
    WHITELIST = ['user_id_1', 'user_id_2']
    ```

3. Create a `requirements.txt` file with the necessary dependencies:
    ```txt
    python-telegram-bot==13.7
    pedalboard==0.2.0
    pydub==0.25.1
    ```

## Running with Docker

1. Build the Docker image:
    ```sh
    docker build -t voice-enhancer-bot .
    ```

2. Run the Docker container:
    ```sh
    docker run -d --name voice-enhancer-bot -p 5000:5000 voice-enhancer-bot
    ```

## Usage

1. Start a chat with your bot on Telegram.
2. Send the `/start` command to the bot.
3. Send an audio file or voice message to the bot.
4. The bot will process the audio and send back the enhanced version.

## Project Structure

- `main.py`: Main application code for the bot.
- `Dockerfile`: Docker configuration for the bot.
- `config.py`: Configuration file for the bot token and whitelist.
- `requirements.txt`: Python dependencies.

## License

This project is licensed under the MIT License.