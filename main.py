from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "MU3Link",
    bot_token = "7412278588:AAFKWhBga4p9sqXT9OcaYt41nQz14IVmQyA",
    api_id = 10811400,
    api_hash = "191bf5ae7a6c39771e7b13cf4ffd1279"
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
        message.reply_text("<b>A Mega Recording Telegram bot by Blaster</b>\n\n<b>Made with Love by @BlasterOriginals</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...
    
app.run()
