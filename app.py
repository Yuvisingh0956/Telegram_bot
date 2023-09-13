import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hello! Welcome to Yuvi Talks Bot.")

def helps(update, context):
    update.message.reply_text(
        '''
        Hi there! I am Telegram bot created by Yuvraj.Please follow this commands:

        /start - to start the conversation
        /content - Information about Yuvraj 
        /contact - Information about contact of Yuvraj
        /help - to get this help menu

I hope this help :)
        '''
    )   
     
def content(update, context):
    update.message.reply_text(
        '''
       Yuvraj Is currently 20 years old.
He is a great programmer.
He is good at flirting too if you don't believe give a call😂😂.
If you are using this bot it means you are a close friend of Yuvi. So cheers🍾🍾.

I hope this help :)
        '''
    ) 

def contact(update, context):
    update.message.reply_text(
        '''
       mail: yuvicode@gmail.com
Phone number: 3746376377
Address: Respect my privacy please😂😂
        '''
    ) 

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.CommandHandler('help',helps))
dispatch.add_handler(telegram.ext.CommandHandler('content',content))
dispatch.add_handler(telegram.ext.CommandHandler('contact',contact))
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()