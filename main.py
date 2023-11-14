import subprocess
from telegram import Bot
from telegram import ParseMode

bot = Bot(token='YOUR_BOT_TOKEN')
chat_id = 'YOUR_CHAT_ID'

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    return result.stdout + result.stderr

def send_message(message):
    bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

if __name__ == "__main__":
    sensors_command = "sensors"

    header = "Ubuntu Home\n" #Header for output

    output = run_command(sensors_command)
    send_message(f"```\n{header}{output}\n```")
