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

## Running with Docker Compose

1. Create a `docker-compose.yml` file:
    ```yaml
    version: '3.8'

    services:
      voiceenhancer:
        build: .
        container_name: voiceenhancer
        ports:
          - "8000:8000"  # For health check
        environment:
          - TOKEN=${TOKEN}
          - WHITELIST=${WHITELIST}
        volumes:
          - .:/app
    ```

2. Run the Docker Compose:
    ```sh
    docker-compose up -d
    ```

## Usage

1. Start a chat with your bot on Telegram.
2. Send the `/start` command to the bot.
3. Send an audio file or voice message to the bot.
4. The bot will process the audio and send back the enhanced version.

## Output Files

- `files/audio.m4a`: The original audio file received from the user.
- `files/audio_enhanced.wav`: The enhanced audio file processed by the bot.

## Health Check System

A health check system is in place using Flask. The health check endpoint can be accessed at `/health` on port `8000`.

## Video Demo

Check out the video demo of the Voice Enhancer Bot in action:

https://github.com/user-attachments/assets/be379474-c89d-441b-9b04-01b97ecaec98

## Project Structure

- `main.py`: Main application code for the bot.
- `Dockerfile`: Docker configuration for the bot.
- `Dockerfile.koyeb`: Docker configuration for Koyeb deployment.
- `docker-compose.yml`: Docker Compose configuration.
- `config.py`: Configuration file for the bot token and whitelist.
- `requirements.txt`: Python dependencies.

## License

This project is licensed under the MIT License.
