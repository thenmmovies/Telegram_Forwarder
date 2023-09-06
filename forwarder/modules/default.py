from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters
from telegram.constants import ParseMode

from forwarder import bot, OWNER_ID

PM_START_TEXT = """
Hey {}, I'm {}!
 I`M A Bot TO Provide Views ON Private Channels 
 
Contact @NmFajis For Buying Monthly Views Plans.
"""

PM_HELP_TEXT = """
Hey {}, I'm {}!
 I`M A Bot TO Provide Views ON Private Channels 
 
Contact @NmFajis For Plans And Pricing.
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    if not (chat and message and user):
        return

    if chat.type == "private":
        await message.reply_text(
            PM_START_TEXT.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
        )
    else:
        await message.reply_text("I'm up and running!")


async def help(update: Update, _):
    chat = update.effective_chat
    message = update.effective_message
    if not (chat and message):
        return

    if not chat.type == "private":
        await message.reply_text("Contact me via PM to get a list of usable commands.")
    else:
        await message.reply_text(PM_HELP_TEXT)


bot.add_handler(CommandHandler("start", start, filters=filters.User(OWNER_ID)))
bot.add_handler(CommandHandler("help", help, filters=filters.User(OWNER_ID)))
