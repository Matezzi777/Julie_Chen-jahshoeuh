import discord
from discord.ext import commands
from config import VERSION
from database import add_confessional, remove_confessional

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="%", intents=discord.Intents.all(), description=f"Julie Chen v{VERSION} by @matezzi75. Send me a DM for your own custom bot.", help_command=None)

#==================== COLOURS & INFOS ===================
BOT_EMBED_RGB = discord.Colour.from_rgb(172, 59, 241)

#======================== EMBEDS ========================
class BotEmbed(discord.Embed):
    def __init__(self, *, colour=BOT_EMBED_RGB, color=BOT_EMBED_RGB, title="TITLE", type='rich', url=None, description=None, timestamp=None):
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp)
        self.set_footer(text=f"Julie Chen v{VERSION}")

#========================= VIEW =========================
class SetConfView(discord.ui.View):
    def __init__(self, user: discord.Member, new_channel_id: str):
        super().__init__(timeout=None)
        self.add_item(DoNothingButton(user))
        self.add_item(ModifyConfButton(user, new_channel_id))

class UnlinkConfView(discord.ui.View):
    def __init__(self, user: discord.Member):
        super().__init__(timeout=None)
        self.add_item(ConfirmButton(user))
        self.add_item(CancelButton(user))

#======================== BUTTON ========================
class DoNothingButton(discord.ui.Button):
    def __init__(self, user: discord.Member):
        super().__init__(style=discord.ButtonStyle.green,
                         label="Do Nothing",
                         emoji="✅")
        self.selected_user: discord.Member = user
        
    async def callback(self, interaction: discord.Interaction):
        return await interaction.response.edit_message(embed=BotEmbed(title="CONFESSIONAL UNCHANGED", description=f"{self.selected_user.mention}'s confessional unchanged.", colour=discord.Colour.green()), view=None)

class ModifyConfButton(discord.ui.Button):
    def __init__(self, user: discord.Member, new_channel_id: str):
        super().__init__(style=discord.ButtonStyle.blurple,
                         label="Modify",
                         emoji="♻️")
        self.selected_user: discord.Member = user
        self.new_channel_id: str = new_channel_id
        
    async def callback(self, interaction: discord.Interaction):
        remove_confessional(self.selected_user)
        add_confessional(self.selected_user, self.new_channel_id)
        return await interaction.response.edit_message(embed=BotEmbed(title="CONFESSIONAL MODIFIED", description=f"{self.selected_user.mention}'s confessional successfuly modified.", colour=discord.Colour.green()), view=None)

class ConfirmButton(discord.ui.Button):
    def __init__(self, user: discord.Member):
        super().__init__(style=discord.ButtonStyle.green,
                         label="Confirm",
                         emoji="✅")
        self.selected_user: discord.Member = user

    async def callback(self, interaction: discord.Interaction):
        remove_confessional(self.selected_user)
        return await interaction.response.edit_message(embed=BotEmbed(title="CONFESSIONAL REMOVED", description=f"{self.selected_user.mention}'s confessional removed from database.", colour=discord.Colour.green()), view=None)

class CancelButton(discord.ui.Button):
    def __init__(self, user: discord.Member):
        super().__init__(style=discord.ButtonStyle.red,
                         label="Cancel",
                         emoji="❌")
        self.selected_user: discord.Member = user

    async def callback(self, interaction: discord.Interaction):
        return await interaction.response.edit_message(embed=BotEmbed(title="CONFESSIONAL UNCHANGED", description=f"{self.selected_user.mention}'s confessional unchanged", colour=discord.Colour.green()), view=None)