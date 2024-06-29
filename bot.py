import telebot
import zipfile
import os
import shutil
import subprocess
from werkzeug.urls import url_quote
API_TOKEN = '7380171310:AAFAhKYwYxjvTY7H6EDkTjJj6OXNyvPvKq4'
PYPI_TOKEN = 'pypi-AgEIcHlwaS5vcmcCJDc0MmE1YmU2LTgyOGYtNDc4YS04YTczLTIwOWExNDlkN2JkOQACKlszLCJhMzg1MjEyNC05YjU3LTRkM2QtYTBkNy0wMjkyYzQ1NmRkMmIiXQAABiBEQsbOT7TsEnpy74F5VNqn_iFRmsDRbbErjgqD0LSwGw'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    if message.document.mime_type == 'application/zip':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f"{message.document.file_name}"
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        with zipfile.ZipFile(src, 'r') as zip_ref:
            zip_ref.extractall("extracted_files")

        extracted_folder = os.path.join(os.getcwd(), "extracted_files")

        files_to_upload = []
        for root, dirs, files in os.walk(extracted_folder):
            for file in files:
                if file.endswith('.tar.gz') or file.endswith('.whl'):
                    file_path = os.path.join(root, file)
                    files_to_upload.append(file_path)

        if files_to_upload:
            for file_path in files_to_upload:
                print(f"Uploading file: {file_path}")
                command = [
                    'twine', 'upload', file_path,
                    '-u', '__token__',
                    '-p', PYPI_TOKEN
                ]
                subprocess.run(command, check=True)
            bot.reply_to(message, "تـم الـرفع بـنجاح . \n Golden . يكول احبك ياحلئ واحد يرفع مكتبة " )
        else:
            bot.reply_to(message, "اتاكد من ملفاتك لان اكو خطاء")

        os.remove(src)
        shutil.rmtree(extracted_folder)

bot.polling()
