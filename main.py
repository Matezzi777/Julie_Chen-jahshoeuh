import discord
from config import TOKEN, SERVERS
from classes import Bot, BotEmbed

bot = Bot()

@bot.event
async def on_ready() -> None:
	print("\nBot connected and ready to Rock n' Roll !\n")

@bot.slash_command(guild_ids=SERVERS, name="ping", description="PONG !")
async def ping(interaction: discord.Interaction):
	print(f"COMMAND : /ping used by @{interaction.user.name} in {interaction.guild.name} (@{interaction.channel.name})")
	await interaction.response.send_message(embed=BotEmbed(title="PONG !").remove_footer(), ephemeral=True)

bot.run(TOKEN)