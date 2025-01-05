import os

from flask import Flask
from threading import Thread

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, filters, AIORateLimiter, ContextTypes, MessageHandler

from pedalboard import Pedalboard, NoiseGate, Compressor, LowShelfFilter, Gain
from pedalboard.io import AudioFile
from pydub import AudioSegment

from config import TOKEN, WHITELIST

# Flask app for health check
health_app = Flask(__name__)

@health_app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

def run_health_check_server():
    health_app.run(host="0.0.0.0", port=8000)

class VoiceEnhancer:
     def __init__(self):
          self.app = ApplicationBuilder() \
          .token(TOKEN) \
          .rate_limiter(AIORateLimiter(overall_max_rate=10, overall_time_period=60)) \
          .build()
          self.setup_handlers()

     def setup_handlers(self):
          self.app.add_handler(CommandHandler('start', self.start))
          self.app.add_handler(MessageHandler(filters.AUDIO, self.handle_audio))
          self.app.add_error_handler(self.error_handler)
    
     async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
          print(f'An error occurred: {context.error}')
     
     async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
          if str(update.message.chat_id) not in WHITELIST:
               await update.message.reply_text('not in service')
               return
          await update.message.reply_text('Prepare to sound like a radio DJ... or a chipmunk on helium. Your choice!')
     
     async def handle_audio(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
          if str(update.message.chat_id) not in WHITELIST:
               await update.message.reply_text('not in service')
               return
          # fetch the audio file
          file_name = os.path.join('files', 'audio.m4a')
          audio_file = await (update.message.voice or update.message.audio).get_file()
          await audio_file.download_to_drive(file_name)
          await update.message.reply_text(f"Audio file saved successfully! Injecting helium...")
          
          # convert audio 
          audio = AudioSegment.from_file(file_name, format="m4a")        
          audio.export('files/new.wav', format="wav")
          
          # Process Audio
          with AudioFile('files/new.wav') as file:
               audio = file.read(file.frames)
               sample_rate = file.samplerate
          board = Pedalboard([
               NoiseGate(threshold_db=-40, ratio=1.5, release_ms=250),
               Compressor(threshold_db=-16, ratio=2.5),
               LowShelfFilter(cutoff_frequency_hz=440, gain_db=10, q=1),
               Gain(gain_db=4),
          ])
          processed_audio = board(audio, sample_rate)
          with AudioFile('files/enhanced.wav', 'w', sample_rate, processed_audio.shape[0]) as f:
               f.write(processed_audio)
               
          # send the enhanced audio file
          chat_id = update.effective_chat.id
          enhanced_file = open('files/enhanced.wav', 'rb')
          await context.bot.send_audio(chat_id, enhanced_file)
          enhanced_file.close()
          del enhanced_file  
          
          # Delete the files created
          os.remove('files/audio.m4a')
          os.remove('files/new.wav')
          os.remove('files/enhanced.wav')
     
     def run(self):
          print('---- Bot is running ----') 
          Thread(target=run_health_check_server).start()
          self.app.run_polling(poll_interval=5)
               
if __name__ == "__main__":
    bot = VoiceEnhancer()
    bot.run()