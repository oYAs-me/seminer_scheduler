import discord
from discord import app_commands

import bot_token
import spreadsheet
import table

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(
    intents=intents
)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("seminar.bot is on ready")
    await tree.sync()

@tree.command(name="scheduler", description="ゼミ参加者の時間割を表示")
async def scheduler(interaction):
    await interaction.response.defer(thinking=True)
    seminar_name = interaction.channel.name
    worksheet = spreadsheet.connect_gspread()
    attendee = spreadsheet.seminar_attendee(worksheet, seminar_name)
    schedule = spreadsheet.attendee_schedule(worksheet, attendee)
    table.table_img(schedule)
    await interaction.followup.send('第1タームの時間割', file=discord.File('schedules1.png'))
    await interaction.followup.send('第2タームの時間割', file=discord.File('schedules2.png'))



client.run(bot_token.TOKEN)