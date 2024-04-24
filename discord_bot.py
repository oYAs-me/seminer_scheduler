import discord

import bot_token
import spreadsheet
import table

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot(
    intents=intents
)

@bot.event
async def on_ready():
    print("seminar.bot is on ready")

@bot.command(name="scheduler", description="ゼミ参加者の時間割を表示")
async def scheduler(ctx):
    seminar_name = ctx.channel.name
    worksheet = spreadsheet.connect_gspread()
    attendee = spreadsheet.seminar_attendee(worksheet, seminar_name)
    schedule = spreadsheet.attendee_schedule(worksheet, attendee)
    table.table_img(schedule)
    await ctx.send('第1タームの時間割', file=discord.File('schedules1.png'))
    await ctx.send('第2タームの時間割', file=discord.File('schedules2.png'))



bot.run(bot_token.TOKEN)