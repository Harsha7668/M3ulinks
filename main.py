from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels, webdl_command_handler

from datetime import datetime, timedelta



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




# Function to handle the /webdl command
@app.on_message(filters.incoming & filters.command(['webdl']) & filters.text)
def webdl_handler(app, message):
    auth_user = check_user(message)
    if auth_user is None:
        return

    cmd_parts = message.text.split()
    channel = None
    start_time = None
    end_time = None
    title = None

    for i, part in enumerate(cmd_parts):
        if part == '-c':
            channel = cmd_parts[i + 1]
        elif part == '-ss':
            start_time = cmd_parts[i + 1]
        elif part == '-to':
            end_time = cmd_parts[i + 1]
        elif part == '-title':
            title = " ".join(cmd_parts[i + 1:])
            break

    if not channel or not start_time or not end_time or not title:
        message.reply_text("<b>Syntax: </b>`/webdl -c [channel] -ss [start_time] -to [end_time] -title [title]`")
        return

    # Convert start_time and end_time to datetime objects
    try:
        start_time = datetime.strptime(start_time, "%d/%m/%Y+%H:%M:%S")
        end_time = datetime.strptime(end_time, "%d/%m/%Y+%H:%M:%S")
    except ValueError:
        message.reply_text("<b>Error:</b> Invalid date format. Use `dd/mm/yyyy+HH:MM:SS`.")
        return

    # Check if the start_time is within the last 7 days
    if start_time < datetime.now() - timedelta(days=7):
        message.reply_text("You can only record sessions within the last 7 days.")
        return

    # Check if the end time is after the start time
    if end_time <= start_time:
        message.reply_text("End time must be after start time.")
        return

    # Call the recording function
    webdl_command_handler(app, message, channel, start_time, end_time, title)



    

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
