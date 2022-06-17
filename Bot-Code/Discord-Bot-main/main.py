#Import required modules

import discord
import random
import time
from discord.ext import commands
from discord_slash import SlashCommand

client = discord.Client()

# Bot online, prefix & status-

client = commands.Bot(command_prefix='u.')
Slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="Hacked Accounts Spam | /help (Slash Command)"))
    print("Logged in successfully as Url Reaper#8450")
  
# Commands -

# Ping command (Normal) -
@client.command(aliases=["p", "latency"])
async def ping(ctx):
    await ctx.send(f'Pong! Your ping is {round(client.latency * 1000)}ms')

# Ping command (Slash) - 
@Slash.slash(name="Ping", description="Shows the current ping of the bot!")
async def ping(ctx):
    await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')


# Phishing detection and deletion function -

@client.event
async def on_message(message):
    msg_content = message.content.lower()

    # Spam Words Storage
    
    spamWord = ['https://discords', 'https://discrde', 'https://dlscords','https://steamdiscord', 'https://d!scord', 
    'https://steamdiscrod', 'https://clickdlscord-nitro', 'https://giftdlscorcl', 'https://dlsccrd', 'https://dissord', 
    'https://dlscord-game', 'https://shopdisccordapp', 'https://giftdiscod', 'https://discrods', 'https://discrods', 
    'https://discrox', 'https://discordsteamc.', 'https://disocrde', 'https://dilscord',  'https://diskord', 
    'https://gitxhub', 'https://gibthub', 'https://disecord', 'https://discord-subscribe.xyz', 'https://e-giftprime.com/',
    'https://get-3month.com/']
    
    # delete spam word if match with the list
    if any(word in msg_content for word in spamWord):
        await message.delete()

# Help Command (Normal) -

@client.command(pass_context=True)
async def help(ctx):
    #author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Help")
    embed.add_field(name="🏓 ping", value='Gives the current ping for the bot!', inline=True) #1
    embed.add_field(name="❔ help", value="Shows this message", inline=True) #2
    embed.add_field(name="👨‍💻 botdev", value="Shows developer's info", inline=True)
    #embed.add_field(name="🎫 ticket", value="Send the link to open a support ticket with Discord", inline=True) #3
    embed.add_field(name="🔧 support", value="Sends the link to Support Server", inline=True) #4
    embed.add_field(name="🛠 updates", value="Shows changelog of the bot", inline=True) #5
    #embed.add_field(name="🤖 botinfo", value="Shows the information about the bot", inline=True) #6
    #embed.add_field(name="📚 resources", value="Sends links to official Discord articles", inline=True) #7
    #embed.add_field(name="🌐 website", value="Get link to bot's official website", inline=True) #8
    embed.add_field(name="💀 hacked", value="Tells you what to do in-case the account is compromised", inline=True) #9
    embed.add_field(name="💡 invite", value="Sends a link to add the bot to your server", inline=True) #10
    #embed.add_field(name="🎴  misc", value="Shows the miscellous stuff like acknowledgements, future updates, etc", inline=True) #11
    #embed.add_field(name="🚨 remove", value="Sends an embed to tell you what to do you are getting spammed with fake links", inline=True) #12
    embed.add_field(name="⚡ Using only Slash commands", value = "Bot is using slash commands instead of traditional prefix+syntax command for better user experience", inline=False)
    embed.add_field(name="🚮 **About Link Deletion** - ", value="The links will be deleted as soon as the bot detects them. There is no need for any kind of setup :D", inline=False)

    await ctx.send(embed=embed)

# Help Command (Slash) -

@Slash.slash(name="Help", description="Gives information about all bot commands")
async def help(ctx):
    #author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.random()
    )
    embed.set_author(name="Help")
    embed.add_field(name="🏓 ping", value='Gives the current ping for the bot!', inline=True) #1
    embed.add_field(name="❔ help", value="Shows this message", inline=True) #2
    embed.add_field(name="👨‍💻 botdev", value="Shows developer's info", inline=True)
    #embed.add_field(name="🎫 ticket", value="Send the link to open a support ticket with Discord", inline=True) #3
    embed.add_field(name="🔧 support", value="Sends the link to Support Server", inline=True) #4
    embed.add_field(name="🛠 updates", value="Shows changelog of the bot", inline=True) #5
    #embed.add_field(name="🤖 botinfo", value="Shows the information about the bot", inline=True) #6
    #embed.add_field(name="📚 resources", value="Sends links to official Discord articles", inline=True) #7
    #embed.add_field(name="🌐 website", value="Get link to bot's official website", inline=True) #8
    embed.add_field(name="💀 hacked", value="Tells you what to do in-case the account is compromised", inline=True) #9
    embed.add_field(name="💡 invite", value="Sends a link to add the bot to your server", inline=True) #10
    #embed.add_field(name="🎴  misc", value="Shows the miscellous stuff like acknowledgements, future updates, etc", inline=True) #11
    #embed.add_field(name="🚨 remove", value="Sends an embed to tell you what to do you are getting spammed with fake links", inline=True) #12
    embed.add_field(name="⚡ Using only Slash commands", value = "Bot is using slash commands instead of traditional prefix+syntax command for better user experience", inline=False)
    embed.add_field(name="🚮 **About Link Deletion** - ", value="The links will be deleted as soon as the bot detects them. There is no need for any kind of setup :D", inline=False)

    await ctx.send(embed=embed)

# botdev Command (Normal) -

@client.command(aliases=["dev", "bd"])
async def botdev(ctx):

    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Developer Info")
    embed.add_field(name="🔰 Developer Tag -", value="```YΣ〆Prasadⁿᶻ#0068```", inline=False)
    embed.add_field(name="🆔 Developer ID -", value="756200102342688788", inline=False)
    embed.add_field(name="👀 About -", value="__**Prasad aka ItzzNeo13 is a Web Dev, CEH and CyberSecurity Enthusiast. He likes to listening songs and play games in his free time.**__", inline=False)
    embed.add_field(name="🌐 Webite -",value="[Click here!](https://itzzneo13.github.io)")


    #await ctx.send(embed=embed)

# botdev command (slash) - 
@Slash.slash(name="botdev", description="Shows information about bot developer!")
async def botdev(ctx):

    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Developer & Website Developer's Info")
    embed.add_field(name="🔰 Bot Developer Tag -", value="```YΣ〆Prasadⁿᶻ#0068```", inline=False)
    embed.add_field(name="🆔 Developer ID -", value="756200102342688788", inline=False)
    embed.add_field(name="👀 About -", value="__**Prasad aka ItzzNeo13 is a Web Dev, CEH and CyberSecurity Enthusiast. He likes to listening songs and play games in his free time.**__", inline=False)
    embed.add_field(name="🌐 Webite -",value="[Click here!](https://itzzneo13.github.io)")
    embed.add_field(name="-------", value="▫", inline=False)
    embed.add_field(name="🔰 Website Developer Tag -", value="```debug_it#0296```", inline=False)
    embed.add_field(name="🆔 Developer ID -", value="811555750866321429", inline=False)
    embed.add_field(name="👀 About -", value="__**Debug it as his name says likes to code different things. He helped me develop the bot's website.**__", inline=False)
    embed.add_field(name="🌐 Github -",value="[Click here!](https://github.com/DebugIt)")


    await ctx.send(embed=embed)

# Discord Support Command (Normal) - 

@client.command(aliases=["dcsup"])
async def ticket(ctx):

    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Discord Support Resources")
    embed.add_field(name="Official Webite -", value="[Click here!](https://support.discord.com/hc/en-us/requests/new)", inline=False)
    embed.add_field(name="Support Email - ", value="`support@discordapp.com`")
    embed.set_footer(text="P.S. - The time of reply can be longer because of various things like current number of tickets etc. The best way of contacting is though mail.")

    #await ctx.send(embed=embed)



# Support Command (Normal) -
@client.command(aliases=["sup"])
async def support(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Support Resources")
    embed.add_field(name="🗄 Discord Support Server - ", value="[Click here!](https://discord.gg/XEzMJrWB65)", inline=False)
    embed.add_field(name="🌐 Developer Website - ", value="[Click here!](https://itzzneo13.github.io)", inline=False)

    #await ctx.send(embed=embed)


# Support Command (Slash) - 

@Slash.slash(name="Support", description="Sends a link to join the support server of the bot")
async def support(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Support Resources")
    embed.add_field(name="🗄 Discord Support Server", value="[Click here!](https://discord.gg/XEzMJrWB65)"  ,)
    embed.add_field(name="🌐 Developer Website", value="[Click here!](https://itzzneo13.github.io)")

    await ctx.send(embed=embed)

# Updates Command (Normal) - 

@client.command(aliases=["up"])
async def updates(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Updates & Change Log")
    embed.add_field(name="Url Reaper v1.0.2(Stable) changelog-", value="**1]New Spam links added\n2]Improved latency time\n3]Changed Host from Repl.it to Railway to prevent the bot from going offline again & again**")
    #embed.set_footer(text="Update Date 22/03/2022 | Update Release Time - 20:20 hrs IST")

    #await ctx.send(embed=embed)

# Updates Command (Slash) -
@Slash.slash(name="updates", description="Shows changelog of the bot")
async def updates(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Updates & Change Log")
    embed.add_field(name="Url Reaper v1.0.2(Stable) changelog-", value="**1] New Spam links added\n2] Improved latency time\n3] Changed the hosting method from Repl.it + UptimeRobot to Railway**")
    #embed.set_footer(text="Update Date 22/03/2022 | Update Release Time - 20:20 hrs IST")

    await ctx.send(embed=embed)

  
# Invite Command (Normal) -

@client.command(aliases=["inv"])
async def invite(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Invite Link")
    embed.add_field(name="Click below to add me to your server!!", value="[Add me!](https://discord.com/api/oauth2/authorize?client_id=932145526751768606&permissions=2147608640&scope=bot%20applications.commands)", inline=False)
    embed.set_footer(text="Don't worry, I do not need any dangerous perms like administrator to work & make sure you have Manage Server Permission to add me")

    #await ctx.send(embed=embed)

# Invite Command (Slash) -

@Slash.slash(name="invite", description="sends the bot invite link")
async def invite(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot Invite Link")
    embed.add_field(name="Click below to add me to your server!!", value="[Add me!](https://discord.com/api/oauth2/authorize?client_id=932145526751768606&permissions=2147608640&scope=bot%20applications.commands)", inline=False)
    embed.set_footer(text="Don't worry, I do not need any dangerous perms like administrator to work & make sure you have Manage Server Permission to add me")

    await ctx.send(embed=embed)

# Botinfo Command (Normal) -

@client.command(aliases=["info"])
async def botinfo(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Bot's Basic stats")
    embed.add_field(name="🗃 Code Library - ", value="discord.py", inline=False)
    embed.add_field(name="🔠 Modules used - ", value="Flask, Discord, Slash-Commands, OS, Random", inline=False)
    embed.add_field(name="❌ Current Errors - ", value="1", inline=False)
    embed.add_field(name="🚫 Errors Fixed - ", value="19", inline=False)
    embed.add_field(name="🤝 Developers - ", value="__**Bot Dev**__ = Prasad - <@756200102342688788> | __**Website Dev**__ = Debug_it - <@811555750866321429>")

    #await ctx.send(embed=embed)



# Resources Command (Normal) -

@client.command(aliases=["res"])
async def resources(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Some Of Discord's Official Articles")
    embed.add_field(name="Tips to Prevent Spam & Hacking", value="[Click here!!](https://discord.com/safety/360044104071-Tips-against-spam-and-hacking)", inline=False)
    embed.add_field(name="Four steps for Super Safe Account", value="[Click here!!](https://discord.com/safety/360043857751-Four-steps-to-a-super-safe-account)", inline=False)
    embed.add_field(name="Four steps for Super Safe Server", value="[Click here!!](https://discord.com/safety/360043653152-Four-steps-to-a-super-safe-server)", inline=False)
    embed.add_field(name="Discord Transparancy Report 2021", value="[Click here!](https://discord.com/blog/discord-transparency-report-h1-2021)", inline=False)
    embed.set_footer(text="These articles will be updated occasionally. If you have any recent articles feel free to suggest them on the support server")

    #await ctx.send(embed=embed)

# Resources Command (Slash) -

# Compromised Command (Normal) -

@client.command(aliases=["h"])
async def hacked(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Here is what you should do if account is compromised")
    embed.add_field(name="Initial Steps", value="First of all: Run an antivirus on your computer or phone to check if you device has any mallicious software.\nAfter that please change your password if you can. Also make sure to change your password on every other platform you are using it too!!!\nIf you can please contact your Discord Friends and Owners of the server you are in to warn them that your account has been compromised. This can help prevent others falling for the malicious links that may be sent with your account.", inline=False)
    embed.add_field(name="Getting Account and/or Refund Back", value='Please contact Discord Support [here](https://dis.gd/support) (There is a reason called "hacked account") and let them do their things. There is no guarantee that you will get your account back and it can take some time before your Ticket will be answered so be patient. You can also contact Discord Billing [here](https://dis.gd/billing) (There is a reason called "Unauthorized Transaction")The more information you can provide to prove that this is in fact your account, the better.', inline=False)
    embed.add_field(name="Someone whom i know got hacked, what should i do?", value="If you notice someone elses account got hacked try to contact him using an alternative method than Discord (because the attackers can just delete your warning or the person has no access to their account anymore)If you can't do that or after you have done this you can report the user to Discord so that they can stop the attackers from doing more damage [here](https://dis.gd/support) (There is a reason called 'hacked account')", inline=False)
    embed.set_footer(text="I used a reddit post as reference for this command.")

    #await ctx.send(embed=embed)

# Compromised Command (Slash) -
@Slash.slash(name="hacked", description="Tells you what to do if account is hacked")
async def hacked(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )

    embed.set_author(name="Here is what you should do if account is compromised")
    embed.add_field(name="Initial Steps", value="First of all: Run an antivirus on your computer or phone to check if you device has any mallicious software.\nAfter that please change your password if you can. Also make sure to change your password on every other platform you are using it too!!!\nIf you can please contact your Discord Friends and Owners of the server you are in to warn them that your account has been compromised. This can help prevent others falling for the malicious links that may be sent with your account.", inline=False)
    embed.add_field(name="Getting Account and/or Refund Back", value='Please contact Discord Support [here](https://dis.gd/support) (There is a reason called "hacked account") and let them do their things. There is no guarantee that you will get your account back and it can take some time before your Ticket will be answered so be patient. You can also contact Discord Billing [here](https://dis.gd/billing) (There is a reason called "Unauthorized Transaction")The more information you can provide to prove that this is in fact your account, the better.', inline=False)
    embed.add_field(name="Someone whom i know got hacked, what should i do?", value="If you notice someone elses account got hacked try to contact him using an alternative method than Discord (because the attackers can just delete your warning or the person has no access to their account anymore)If you can't do that or after you have done this you can report the user to Discord so that they can stop the attackers from doing more damage [here](https://dis.gd/support) (There is a reason called 'hacked account')", inline=False)
    embed.set_footer(text="I used a reddit post as reference for this command")

    await ctx.send(embed=embed)

# Misc command (Normal) -

@client.command(alias=["m"])
async def misc(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )
    embed.set_author(name="Links to external sources and possible future updates here")
    embed.add_field(name="Spam Sites Name List - ", value="[Github Repo](https://github.com/nikolaischunk/discord-phishing-links)", inline=False)
    embed.add_field(name="Hacked command Post Link - ", value="[Reddit Post Link](https://www.reddit.com/r/discordapp/comments/nsghpc/explanation_my_account_was_stolenhacked_what/?utm_medium=android_app&utm_source=share)", inline=False)
    embed.add_field(name="Thanks to both of you guys ❤", value="Let's fight this spam together :D", inline=False)
    embed.add_field(name="Possible Future Updates", value="1] Custom emojis for command\n 2]More aggressive moderation training\n 3]Adding More Content to Resources Command")
    embed.set_footer(text="Thank you for using Url Reaper, Stay Tuned for more amazing updates!!")

    #await ctx.send(embed=embed)

# Misc Command (Slash) -


# Remove command (Normal) -

@client.command(aliases=["r"])
async def remove(ctx):
    embed = discord.Embed(
        colour = discord.Colour.random()
    )
    embed.set_author(name="Getting Spammed by Bots or users? Here's what you must do")
    embed.add_field(name="To get rid of the bot -", value="Block it & Report It [Guide to report](https://dis.gd/howtoreport)", inline=False)
    embed.add_field(name="If these types of bots are repeatedly sending you messages, then - ", value="1] Use Mutual Servers to determine the server(s) they share with you, and disable Direct Messages from server members for those servers.\n2]If you cannot find any common servers, you can disable DMs from all servers under your User Settings")
    
    #await ctx.send(embed=embed)


# Token -
try:
    client.run('bot_token_was_here')
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')
