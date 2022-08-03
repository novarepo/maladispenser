import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.ui import Modal, InputText
from discord.utils import get

import random
import sys
import json
import os

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again!")
else:
    with open("config.json") as file:
        config = json.load(file)

ASTRAL_GUILD_ID = config["guildID"]
BOT_TOKEN = config['token']
ROLE_NAME = config['permRole']
CHANNEL_BOT_ID =  config['reportingChannel']


intents = discord.Intents().all()

bot = discord.Bot(debug_guilds=[ASTRAL_GUILD_ID], intents=intents)



def reset():
    with open('users.json', "w") as myfile:
        myfile.write("[]")


def randum(fname, user):
    data = json.load(open('users.json'))
    for i in data:
        try:
            if i['Name'] == user:
                links = data[data.index(i)]['Links']
                print("Links are: {0}".format(links))
        except:
            pass
    lines=open(fname).read().splitlines()
    lines = list(set(lines)-set(links))
    print(lines)
    if len(lines)>0:
        return random.choice(lines)
    else:
        return "ERROR, this was caused due to no unique links available. Contact staff immediately."

def addlink(link, user):
    print(link, user)
    data = json.load(open('users.json'))
    for i in data:
        try:
            if i['Name'] == user:
                data[data.index(i)]['Links'].append(link)
        except:
            pass
    os.remove("users.json")
    with open("users.json", "w") as final:
        json.dump(data, final)


def limiter(user, boost):
    data = json.load(open('users.json'))
    for i in data:
        try:
            if i['Name'] == user:
                if i['Left'] > 0:
                    data[data.index(i)]['Left'] -= 1
                    os.remove("users.json")
                    with open("users.json", "w") as final:
                        json.dump(data, final)
                    return False
                else:
                    return True
        except:
            pass
    if boost:
        data.append({"Name":user, "Left":5, "Links":[]})
    else:
        data.append({"Name":user, "Left": 2, "Links":[]})
    os.remove("users.json")
    with open("users.json", "w") as final:
        json.dump(data, final)
    return False


class ReportModal(Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_item(InputText(label="Enter your username", placeholder="Eg: SirMalamute#7289"))
        self.add_item(InputText(label="Enter the domain you wish to report", placeholder="Eg: voidiscool.com"))

    async def callback(self, interaction:discord.Interaction):
        channel = bot.get_channel(CHANNEL_BOT_ID)
        await channel.send("The URL {0} has been reported by {1} Please address soon.".format(self.children[1].value, self.children[0].value) )
        await interaction.response.send_message("Reported {0}".format(self.children[1].value), ephemeral=True)



class ReportView(discord.ui.View):
    @discord.ui.button(label="Report Domain", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        modal = ReportModal(title="Report Domains")
        await interaction.response.send_modal(modal)
        #await interaction.response.send_message("To report this domain, please follow the following steps. Message /report followed by the name of the faulty domain you received. If we acknowledge this as legitimate, then we will give you an extra proxy use.", ephemeral=True)

class LucidView(discord.ui.View):
    @discord.ui.button(label="Lucid Links", style=discord.ButtonStyle.primary) 
    async def button_callback(self, button, interaction):
        BOOST_ROLE = discord.utils.get(interaction.user.guild.roles, name=config['boostRoleName'])
        if limiter(str(interaction.user), (BOOST_ROLE in interaction.user.roles)):
            await interaction.response.send_message("Sorry, your links are up!", ephemeral=True)
        else:
            try:
                link = randum("lucid.txt", str(interaction.user))
                if link == "ERROR, this was caused due to no unique links available. Contact staff immediately.":
                    await interaction.response.send_message("so sorry, no unique links available. please contact staff immediately", ephemeral=True)
                    raise Exception("No unique links available.")
                else:
                    addlink(link, str(interaction.user))
                await interaction.response.send_message("Here is your link! {0}".format(link), ephemeral=True, view=ReportView()) 
            except:
                data = json.load(open('users.json'))
                for i in data:
                    try:
                        if i['Name'] == str(interaction.user):
                            data[data.index(i)]['Left'] += 1
                            os.remove("users.json")
                            with open("users.json", "w") as final:
                                json.dump(data, final)
                    except:
                        pass
                await interaction.response.send_message("error, contact staff", ephemeral=True)

class VoidView(discord.ui.View):
    @discord.ui.button(label="Void Links", style=discord.ButtonStyle.primary) 
    async def button_callback(self, button, interaction):
        BOOST_ROLE = discord.utils.get(interaction.user.guild.roles, name=config['boostRoleName'])
        if limiter(str(interaction.user), (BOOST_ROLE in interaction.user.roles)):
            await interaction.response.send_message("Sorry, your links are up!", ephemeral=True)
        else:
            try:
                link = randum("void.txt", str(interaction.user))
                if link == "ERROR, this was caused due to no unique links available. Contact staff immediately.":
                    await interaction.response.send_message("so sorry, no unique links available. please contact staff immediately", ephemeral=True)
                    raise Exception("No unique links available.")
                else:
                    addlink(link, str(interaction.user))
                await interaction.response.send_message("Here is your link! {0}".format(link), ephemeral=True, view=ReportView()) 
            except:
                data = json.load(open('users.json'))
                for i in data:
                    try:
                        if i['Name'] == str(interaction.user):
                            data[data.index(i)]['Left'] += 1
                            os.remove("users.json")
                            with open("users.json", "w") as final:
                                json.dump(data, final)
                    except:
                        pass
                await interaction.response.send_message("error, contact staff", ephemeral=True)


class RammerheadView(discord.ui.View): 
    @discord.ui.button(label="Coffee Links", style=discord.ButtonStyle.primary) 
    async def button_callback(self, button, interaction):
        BOOST_ROLE = discord.utils.get(interaction.user.guild.roles, name=config['boostRoleName'])
        if limiter(str(interaction.user), (BOOST_ROLE in interaction.user.roles)):
            await interaction.response.send_message("Sorry, your links are up!", ephemeral=True)
        else:
            try:
                link = randum("coffee.txt", str(interaction.user))
                if link == "ERROR, this was caused due to no unique links available. Contact staff immediately.":
                    await interaction.response.send_message("so sorry, no unique links available. please contact staff immediately", ephemeral=True)
                    raise Exception("No unique links available.")
                else:
                    addlink(link, str(interaction.user))
                await interaction.response.send_message("Here is your link! {0}".format(link), ephemeral=True, view=ReportView()) 
            except:
                data = json.load(open('users.json'))
                for i in data:
                    try:
                        if i['Name'] == str(interaction.user):
                            data[data.index(i)]['Left'] += 1
                            os.remove("users.json")
                            with open("users.json", "w") as final:
                                json.dump(data, final)
                    except:
                        pass
                await interaction.response.send_message("error, contact staff", ephemeral=True)

@bot.event 
async def on_ready():
    print('bot online')

@bot.slash_command()
async def openweb(ctx):
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def reset_limits(ctx):
    reset()
    await ctx.response.send_message("succesfully resetted", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def initialize_links(ctx):
    await ctx.respond("Lucid, the webproxy of the future!", view=LucidView()) # Send a message with our View class that contains the button
    await ctx.respond("Enter the void!", view=VoidView()) # Send a message with our View class that contains the button
    await ctx.respond("Coffee, a revolutionary proxy developed on top of rammerhead!", view=RammerheadView()) # Send a message with our View class that contains the button

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def addvoid(ctx, url: str = None):
    file_object = open('void.txt', 'a+')
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(url)
    file_object.close()
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def addcoffee(ctx, url: str = None):
    file_object = open('coffee.txt', 'a+')
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(url)
    file_object.close()
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def addlucid(ctx, url: str = None):
    file_object = open('lucid.txt', 'a+')
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(url)
    file_object.close()
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def counter(ctx):
    with open(r"void.txt", 'r') as fp:
        void = len(fp.readlines())
    with open(r"lucid.txt", 'r') as fp:
        lucid = len(fp.readlines())
    with open(r"coffee.txt", 'r') as fp:
        coffee = len(fp.readlines())
    await ctx.response.send_message("Void: {0}, Lucid: {1}, Coffee: {2}".format(void, lucid, coffee), ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def removevoid(ctx, url: str = None):
    with open("void.txt", "r") as f:
        lines = f.readlines()
    with open("void.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != url:
                f.write(line)   
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def removecoffee(ctx, url: str = None):
    with open("coffee.txt", "r") as f:
        lines = f.readlines()
    with open("coffee.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != url:
                f.write(line)   
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def removelucid(ctx, url: str = None):
    with open("lucid.txt", "r") as f:
        lines = f.readlines()
    with open("lucid.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != url:
                f.write(line)   
    await ctx.response.send_message("succesful", ephemeral=True)

@bot.slash_command()
@commands.has_role(ROLE_NAME)
async def addproxy(ctx, name:str = None):
    data = json.load(open('users.json'))
    for i in data:
        try:
            if i['Name'] == name:
                data[data.index(i)]['Left'] += 1
                os.remove("users.json")
                with open("users.json", "w") as final:
                    json.dump(data, final)
                await ctx.response.send_message("succesfully given one more proxy", ephemeral=True)
        except:
            pass
    await ctx.response.send_message("there is an error in the code or in the JSON file not having the user itself. check the json file or tell the user to make a singular proxy request first before using tokens.", ephemeral=True)



bot.run(BOT_TOKEN)