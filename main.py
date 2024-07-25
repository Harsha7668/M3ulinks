from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "BlasterM3URecorderbot",
    bot_token = "7435365318:AAGK44A35gi6Blocx4DBMak_TWW41H7GkfU",
    api_id = 4857766,
    api_hash = "6c3c6facf5598a4b318e138f8c407028"
)



@app.on_message(filters.incoming & filters.command(['multirec']) & filters.incoming & filters.text)
def multirec_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return

    if len(message.text.split()) < 3:
        message.reply_text("<b>Syntax: </b>`/multirec [channelName] [duration] | [filename]`")
        return

    multi_rec(app, message)

@app.on_message(filters.incoming & filters.command(['channels']) & filters.text)
def show_channels_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return


    getChannels(app, message)


@app.on_message(filters.command(['start']) & filters.text)
def start_handler(app, message):

    if len(message.text.split()) < 3:
        message.reply_text("<b>A Mega Recording Telegram bot by Team Disney Cartoons</b>\n\n<b>Made with Love by @Free_De_La_Hoya_Official</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...
    
app.run()
