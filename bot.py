"""
Tommy.py 1.0.0
A bot for sever management.
Author : Merwin

Commands starts with ++
"""


import os
import json
import random
import discord
import requests
import datetime
import numpy as np
from discord import File
from discord import Game
from discord import Status
from discord import Embed
from discord.ext import commands
from matplotlib import pyplot as plt


# Getting the bot-token.
token_file = open("token.txt","r")
TOKEN = token_file.read().replace("\n","")
token_file.close()

# vars
DB_FILE_NAME = "BOT_DB.json"

cli = commands.Bot(command_prefix="++")

def read_db(filename,server,value_of):
    db_file = open(filename,"r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    return db_data[server][value_of]
def append_db(filename,server,add_to,data):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    if type(db_data[server][add_to]) == list:
        db_data[server][add_to].append(data)
    else:
        db_data[server][add_to].setdefault(data[0],data[1])
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def append_to_db(filename,server,cat,var,data):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    if type(db_data[server][cat][var]) == list:
        db_data[server][cat][var].append(data)
    else:
        db_data[server][cat][var].setdefault(data[0],data[1])
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def append_to_db_sp(filename,server,cat,var,data):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    if type(db_data[server][cat][0][var]) == list:
        db_data[server][cat][0][var].append(data)
    else:
        db_data[server][cat][0][var].setdefault(data[0],data[1])
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def remove_db(filename,server,var_,data):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    db_data[server][var_].remove(data)
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def clear_db(filename,server,var_):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    if type(db_data[server][var_]) == list:
        db_data[server][var_] = []
    else:
        db_data[server][var_] = {}
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def set_in_Cat_db(filename,server,cat,var,data):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    db_data[server][cat][var] = data
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def add_vote_db(filename,server,name,num):
    elec = "ELECTION_CANDIDATES"
    elec_vo = "votes"
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    c = 0
    for e  in db_data[server][elec]:
        if e["name"] == name:
            break
        c+=1
    try:
        db_data[server][elec][c][elec_vo]+=num
        db_data = json.dumps(db_data)
        db_file.write(db_data)
        db_file.close()
    except:
        pass
def reset_db_server(filename,server):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    if db_data == "":
        db_data = '{}'
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    db_data[server] = {}
    db_data[server].setdefault("SETTINGS", {"SCAN_LINK": False})
    db_data[server].setdefault("BANNED_WORDS", [])
    db_data[server].setdefault("TOPICS", [])
    db_data[server].setdefault("AUTO_ROLES", [])
    db_data[server].setdefault("REACTION_MSG_IDS", [])
    db_data[server].setdefault("CURRENT_REACTION_ROLE_PAYLOAD", [])
    db_data[server].setdefault("ELECTION_ROLE_TRANSLATIONS", {})
    db_data[server].setdefault("CURRENT_ELECTION_MSG_ID", [])
    db_data[server].setdefault("GIVE_AWAY", [])
    db_data[server].setdefault("GIVE_AWAY_ID", [])
    db_data[server].setdefault("ELECTION_CANDIDATES",[])
    db_data[server].setdefault("ROLE_TRANSLATIONS", {})
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
def new_server(filename,server):
    db_file = open(filename, "r")
    db_data = db_file.read()
    db_file.close()
    if db_data == "":
        db_data = '{}'
    db_data = json.loads(db_data)
    db_file = open(filename, "w")
    db_data.setdefault(server,{})
    db_data[server].setdefault("SETTINGS",{"SCAN_LINK":False})
    db_data[server].setdefault("BANNED_WORDS",[])
    db_data[server].setdefault("TOPICS",[])
    db_data[server].setdefault("AUTO_ROLES",[])
    db_data[server].setdefault("ELECTION_ROLE_TRANSLATIONS",{})
    db_data[server].setdefault("CURRENT_ELECTION_MSG_ID",[])
    db_data[server].setdefault("REACTION_MSG_IDS",[])
    db_data[server].setdefault("CURRENT_REACTION_ROLE_PAYLOAD",[])
    db_data[server].setdefault("GIVE_AWAY",[])
    db_data[server].setdefault("GIVE_AWAY_ID", [])
    db_data[server].setdefault("ELECTION_CANDIDATES",[])
    db_data[server].setdefault("ROLE_TRANSLATIONS",{})
    db_data = json.dumps(db_data)
    db_file.write(db_data)
    db_file.close()
@cli.event
async def on_ready():
    await cli.change_presence(status=Status.idle,activity=Game("I am Tommy..."))
    print("Ready")
@cli.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to  {member.guild.name} !'
    )
@cli.event
async def on_member_remove(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Bye {member.name} !'
    )
@cli.event
async def  on_guild_join(guild):
    new_server(DB_FILE_NAME,guild.name)
@cli.event
async def on_raw_reaction_add(payload):
    msg_id = payload.message_id
    if int(msg_id) in read_db(DB_FILE_NAME,payload.member.guild.name,"REACTION_MSG_IDS"):
        guild = payload.member.guild
        role = discord.utils.get(guild.roles, name=read_db(DB_FILE_NAME,payload.member.guild.name,"ROLE_TRANSLATIONS").get(payload.emoji.name))
        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
    elif int(msg_id) in  read_db(DB_FILE_NAME,payload.member.guild.name,"GIVE_AWAY_ID"):
        print("ADDED")
        append_to_db_sp(DB_FILE_NAME,payload.member.guild.name,"GIVE_AWAY","members",payload.member.name)
    elif msg_id == read_db(DB_FILE_NAME,payload.member.guild.name,"CURRENT_ELECTION_MSG_ID"):
        name = read_db(DB_FILE_NAME,payload.guild.name,"ELECTION_ROLE_TRANSLATIONS").get(payload.emoji.name)
        add_vote_db(DB_FILE_NAME,payload.member.guild.name,name,1)
@cli.event
async def on_raw_reaction_remove(payload):
    msg_id = payload.message_id
    guild = await cli.fetch_guild(payload.guild_id)
    if msg_id in read_db(DB_FILE_NAME,guild.name,"REACTION_MSG_IDS"):
        name = read_db(DB_FILE_NAME,guild.name,"ROLE_TRANSLATIONS").get(payload.emoji.name)
        role = None
        for e in guild.roles:
            if e.name == name:
                role = e
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.add_removes(role)
        elif msg_id == read_db(DB_FILE_NAME, payload.member.guild.name, "CURRENT_ELECTION_MSG_ID"):
            name = read_db(DB_FILE_NAME, payload.guild.name, "ELECTION_ROLE_TRANSLATIONS").get(payload.emoji.name)
            add_vote_db(DB_FILE_NAME, payload.member.guild.name, name,-1)

@cli.command()
async def add_banned_word(ctx,word):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        if word not in  read_db(DB_FILE_NAME,ctx.guild.name,"BANNED_WORDS"):
            append_db(DB_FILE_NAME,ctx.guild.name,"BANNED_WORDS",word)
        await ctx.channel.send("Done...")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def scan_link(ctx,link,*,line):
    if line.lower() in  requests.get(link).text.lower():
        await ctx.channel.send(f"The link contains **{line}**")
    else:
        await ctx.channel.send(f"The link doesn't contains **{line}**")
@cli.command()
async def delete_links_with_banned_words(ctx,on_off):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials", "mod", "owner", "admin", "staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        if on_off == "on":
            on_off = True
        else:
            on_off = False
        set_in_Cat_db(DB_FILE_NAME,ctx.guild.name,"SETTINGS","SCAN_LINK",on_off)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def remove_banned_word(ctx,word):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        try:
            remove_db(DB_FILE_NAME,ctx.guild.name,"BANNED_WORDS",word)
            await ctx.channel.send("Done...")
        except:
            await ctx.channel.send(f"{word} not found in  **Banned Word**.")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def add_auto_role(ctx,role):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        if role not in read_db(DB_FILE_NAME,ctx.guild.name,"AUTO_ROLES"):
            append_db(DB_FILE_NAME,ctx.guild.name,"AUTO_ROLES",role)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def remove_auto_role(ctx,role):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        try:
            remove_db(DB_FILE_NAME,ctx.guild.name,"AUTO_ROLES",role)
        except:
            await ctx.channel.send(f"No **role** named **{role}** found..")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def add_reaction_roles(ctx,role,emoji):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        append_db(DB_FILE_NAME, ctx.guild.name, "CURRENT_REACTION_ROLE_PAYLOAD", {"role":role,"emoji":emoji})
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def reaction_roles_send(ctx):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        role_channel_id = None
        for e in ctx.guild.channels:
            if e.name == "roles":
                role_channel_id = e.id
        if role_channel_id == None:
            await ctx.channel.send("Channel named **roles** not found...")
        else:
            role_channel = cli.get_channel(role_channel_id)
            # making embed
            allowed_mentions = discord.AllowedMentions(everyone=True)
            embed = Embed(
                title="Choose A Role",
                description=" Choose a role by reacting with provided emoji..",
                colour=0x84f542,
                allowed_mentions=allowed_mentions
            )
            embed.set_author(name="Staff",
                             icon_url="https://cdn.discordapp.com/attachments/954697390366031912/956517639256154172/img.png")
            for e in read_db(DB_FILE_NAME, ctx.guild.name, "CURRENT_REACTION_ROLE_PAYLOAD"):
                embed.add_field(name=e["role"], value=e["emoji"], inline=False)
                append_db(DB_FILE_NAME,ctx.guild.name,"ROLE_TRANSLATIONS",[e["emoji"],e["role"]])
            a = await role_channel.send(embed=embed)
            append_db(DB_FILE_NAME,ctx.guild.name,"REACTION_MSG_IDS",a.id)
            clear_db(DB_FILE_NAME,ctx.guild.name,"CURRENT_REACTION_ROLE_PAYLOAD")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def make_give_away(ctx,*,reward):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        allowed = False
        if read_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY") == []:
            allowed = True
        if allowed:
            giveaway_channel_id = None
            for e in ctx.guild.channels:
                if e.name == "giveaway":
                    giveaway_channel_id = e.id
            if giveaway_channel_id == None:
                await ctx.channel.send("Channel named **giveaway** not found...")
            else:
                giveaway_channel = cli.get_channel(giveaway_channel_id)
                # making embed
                embed = Embed(
                    title=":tada::tada:Giveaway:tada::tada:",
                    description="react to join giveaway!",
                    colour= 0x84f542
                )
                embed.set_author(name="Staff",
                                 icon_url="https://cdn.discordapp.com/attachments/954697390366031912/956517639256154172/img.png")
                embed.add_field(name="Reward", value=reward, inline=False)
                a = await giveaway_channel.send(embed=embed)
                append_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY_ID",a.id)
                append_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY",{"reward":reward,"members":[]})
        else:
            await ctx.channel.send("One giveaway on list , Try again after the current giveaway ends..")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def end_give_away(ctx):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials", "mod", "owner", "admin", "staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        members  =  read_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY")[0]["members"]
        if members == []:
            members = ["NO ONE, LOL"]
        winner = random.choice(members)
        clear_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY")
        clear_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY_ID")
        await ctx.channel.send("Giveaway ended...")
        await ctx.channel.send(f":tada::tada: Winner is {winner}  :tada::tada:")
        giveaway_channel_id = None
        for e in ctx.guild.channels:
            if e.name == "giveaway":
                giveaway_channel_id = e.id
        if giveaway_channel_id == None:
            await ctx.channel.send("Channel named **giveaway** not found...")
        else:
            giveaway_channel = cli.get_channel(giveaway_channel_id)
            await giveaway_channel.send("Giveaway ended.... ")
            await giveaway_channel.send(f":tada::tada: Winner is {winner}  :tada::tada:")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def cancel_give_away(ctx):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials", "mod", "owner", "admin", "staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        clear_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY_ID")
        clear_db(DB_FILE_NAME,ctx.guild.name,"GIVE_AWAY")
        await ctx.channel.send("Giveaway cancelled...")
        giveaway_channel_id = None
        for e in ctx.guild.channels:
            if e.name == "giveaway":
                giveaway_channel_id = e.id
        if giveaway_channel_id == None:
            await ctx.channel.send("Channel named **giveaway** not found...")
        else:
            giveaway_channel = cli.get_channel(giveaway_channel_id)
            await giveaway_channel.send("Giveaway cancelled...")
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def topic(ctx):
    topics = read_db(DB_FILE_NAME,ctx.guild.name,"TOPICS")
    if len(topics) != 0:
        await ctx.channel.send(random.choice(topics))
    else:
        await ctx.channel.send("No Topic Found")
@cli.command()
async def clear(ctx,amount=5):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def show_channel_activity(ctx):
    users_msg = {}
    after = datetime.datetime.now() - datetime.timedelta(days=7)
    async for message in ctx.channel.history(after=after):
        if message.author != cli.user:
            try:
                users_msg[message.author.name]+=1
            except:
                if not message.author.bot:
                    users_msg.setdefault(message.author.name,1)
    users_msg = sorted(users_msg.items(), key=lambda x: x[1])
    a = 10
    if len(users_msg) < 10:
        a = len(users_msg)
    user_msg_ranking = dict(users_msg[0:a])
    x = list(user_msg_ranking.keys())
    h = list(user_msg_ranking.values())
    plt.barh(x, h)
    plt.title = "User activity"
    plt.xlabel = "Members"
    plt.ylabel = "Msgs"
    plot_name = "PLOT_CURRENT_"
    files = os.listdir()
    c = 0
    while True:
        if plot_name+str(c)+".png" not  in files:
            break
        c+=1
    plt.savefig(plot_name+str(c)+".png")
    await ctx.channel.send(file=File(plot_name+str(c)+".png"))
    os.remove(plot_name+str(c)+".png")
    plt.close()
@cli.command()
async def show_user_activity(ctx,member:discord.Member):
    if member == None:
        ctx.channel.send("User not found...")
    else:
        user = member
        count = {}
        after = datetime.datetime.now() - datetime.timedelta(days=7)
        async for message  in ctx.channel.history(after=after):
            if message.author == user:
                date_time = message.created_at.strftime("%d%H")
                try:
                    count[str(date_time)] +=1
                except:
                    count.setdefault(str(date_time),1)
        x_ = list(count.keys())
        x = []
        for e in range(len(x_)):
            x.append(e)
        y = list(count.values())
        x = np.array(x)
        y = np.array(y)
        plt.plot(x,y)
        plt.title = "User activity"
        plt.xlabel = "TIME"
        plt.ylabel = "Chats"
        plt.legend(["Chats"])
        plot_name = "PLOT_CURRENT_"
        files = os.listdir()
        c = 0
        while True:
            if plot_name + str(c) + ".png" not in files:
                break
            c += 1
        plt.savefig(plot_name + str(c) + ".png")
        await ctx.channel.send(file=File(plot_name + str(c) + ".png"))
        os.remove(plot_name + str(c) + ".png")
        plt.close()
@cli.command(alias=["run_and_kick","free_throw"])
async def kick(ctx,member:discord.Member ,*, Reason=None):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        await member.kick(reason=Reason)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def make_election(ctx):
    if read_db(DB_FILE_NAME,ctx.guild.name,"ELECTION_CANDIDATES") == []:
        append_db(DB_FILE_NAME,ctx.guild.name,"ELECTION_CANDIDATES",{"name":ctx.author.name,"emoji":None,"votes":0})
        await ctx.channel.send("Done...")
    else:
        await ctx.channel.send("Currently a election is being conducted, try again later...")
@cli.command()
async def add_to_election(ctx,name,emoji):
    maker = read_db(DB_FILE_NAME,ctx.guild.name,"ELECTION_CANDIDATES")[0]
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION or ctx.author.name == maker:
        append_db(DB_FILE_NAME,ctx.guild.name,"ELECTION_CANDIDATES",{"name":name,"emoji":emoji,"votes":0})
        append_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_ROLE_TRANSLATIONS",[emoji,name])
    else:
        await ctx.channel.send("Only ppl with roles staff , officals, mod , owner , admin and the person who made the election can use this command... ")
@cli.command()
async def start_election(ctx):
    maker = read_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_CANDIDATES")[0]
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials", "mod", "owner", "admin", "staff"]:
            PERMISSION = True
            break
    if PERMISSION or ctx.author.name == maker:
        # making embed
        embed = Embed(
            title="Election",
            description="Elect your candidate by reacting using their emoji.",
            colour= 0x03fc73,
        )
        embed.set_author(name="Staff",
                         icon_url="https://cdn.discordapp.com/attachments/954697390366031912/956517639256154172/img.png")

        c = 0
        for e in read_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_CANDIDATES"):
            if c != 0:
                embed.add_field(name=e["name"], value=e["emoji"], inline=False)
                append_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_ROLE_TRANSLATIONS", [e["emoji"], e["name"]])
            c+=1
        a = await ctx.channel.send(embed=embed)
        append_db(DB_FILE_NAME, ctx.guild.name, "CURRENT_ELECTION_MSG_ID", a.id)
        await ctx.channel.send("Election Started..!!")
    else:
        await ctx.channel.send("Only ppl with roles staff , officials, mod , owner , admin and the person who made the election can use this command... ")
@cli.command()
async def cancel_election(ctx):
    maker = read_db(DB_FILE_NAME,ctx.guild.name,"ELECTION_CANDIDATES")[0]
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION or ctx.author.name == maker:
        clear_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_CANDIDATES")
        clear_db(DB_FILE_NAME, ctx.guild.name, "CURRENT_ELECTION_MSG_ID")
        clear_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_ROLE_TRANSLATIONS")
        await ctx.channel.send("Election Cancelled!!")
    else:
        await ctx.channel.send("Only ppl with roles staff , officials, mod , owner , admin and the person who made the election can use this command... ")
@cli.command()
async def get_election_results(ctx):
    maker = read_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_CANDIDATES")[0]
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials", "mod", "owner", "admin", "staff"]:
            PERMISSION = True
            break
    if PERMISSION or ctx.author.name == maker:
        await ctx.channel.send("Election Stopped!!")
        user_votes_ = read_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_CANDIDATES")
        user_votes_.remove(user_votes_[0])
        user_votes = {}
        for e in user_votes_:
            user_votes.setdefault(e["name"], e["votes"])
        user_votes = sorted(user_votes.items(), key=lambda x: x[1])
        a = 10
        if len(user_votes) < 10:
            a = len(user_votes)
        user_vote_ranking = dict(user_votes[0:a])
        x = list(user_vote_ranking.keys())
        h = list(user_vote_ranking.values())
        plt.barh(x, h)
        plt.title = "Election results"
        plt.xlabel = "Candidate"
        plt.ylabel = "Votes"
        plot_name = "PLOT_CURRENT_"
        files = os.listdir()
        c = 0
        while True:
            if plot_name + str(c) + ".png" not in files:
                break
            c += 1
        plt.savefig(plot_name + str(c) + ".png")
        await ctx.channel.send(file=File(plot_name + str(c) + ".png"))
        os.remove(plot_name + str(c) + ".png")
        plt.close()
        user_votes.reverse()
        winner = user_votes[0]
        await ctx.channel.send(f":tada: The election was won by {winner} :tada:")
        clear_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_CANDIDATES")
        clear_db(DB_FILE_NAME, ctx.guild.name, "CURRENT_ELECTION_MSG_ID")
        clear_db(DB_FILE_NAME, ctx.guild.name, "ELECTION_ROLE_TRANSLATIONS")

    else:
        await ctx.channel.send("Only ppl with roles staff , officials, mod , owner , admin and the person who made the election can use this command... ")
@cli.command()
async def add_topic(ctx,*,topic):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        append_db(DB_FILE_NAME,ctx.guild.name,"TOPICS",topic)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command()
async def reset_bot(ctx):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in [ "owner", "admin"]:
            PERMISSION = True
            break
    if PERMISSION:
        reset_db_server(DB_FILE_NAME,ctx.guild.name)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command(alias=["Bann","ban_the_guy"])
async def ban(ctx,member:discord.Member , *, Reason=None):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        await member.ban(reason=Reason)
    else:
        await ctx.send("Permission Not Granted..")
@cli.command(alias=["run_and_kick","free_throw"])
async def unban(ctx,*, member):
    PERMISSION = False
    for e in ctx.author.roles:
        if e.name.lower() in ["officials","mod","owner","admin","staff"]:
            PERMISSION = True
            break
    if PERMISSION:
        banned_ppl = await ctx.guild.bans()
        name,tag = member.split("#")
        for e in banned_ppl:
            if (e.user.name , e.user.discriminator) == (name , tag):
                await ctx.guild.unban(e.user)
    else:
        await ctx.send("Permission Not Granted..")


@cli.command()
async def bot_commands(ctx):
    help_embed = Embed(title="Bot-commands",
                description="Gives description of all commands.",
                colour=0x84f542)
    help_embed.set_author(name="Staff",icon_url="https://cdn.discordapp.com/attachments/954697390366031912/956517639256154172/img.png")
    commands = [
        ["++bot_commands","Gives description of all commands."],
        ["++ban <mention the user>","Ban a User"],
        ["++Unban <mention the user>","UnBan a User"],
        ["++kick <mention the user>", "Kick the User"],
        ["++clear <count of msgs>(optional)", "Deletes Msgs"],
        ["++add_banned_word <Word>", "Add To Banned Words"],
        ["++remove_banned_word <Word>", "Remove From Banned Words"],
        ["++delete_links_with_banned_words <on/off>", "If`on` links will be scanned for banned words"],
        ["++reset_bot","Resets the bot"],
        ["++add_topic <Topic>","Adds a topic for the server"],
        ["++topic", "Gives a topic to discuss on"],
        ["++show_user_activity <mention user>", "Gives graphs on the activity of a user"],
        ["++show_channel_activity", "Gives graphs on the activity of the current channel"],
        ["++make_election", "Makes a election"],
        ["++start_election", "Start the election"],
        ["++cancel_election", "Cancels the election"],
        ["++get_election_results", "End and Announces the results of election"],
        ["++add_to_election <candidate>", "Add candidate"],
        ["++make_give_away <reward>", "Make a giveaway"],
        ["++cancel_give_away", "Cancel a giveaway"],
        ["++stop_give_away", "Stop a giveaway and get results"],
        ["++reaction_roles_send", "Sent reaction role(to role channel)"],
        ["++add_reaction_roles <role-name> <role-emoji>", "Adds a reaction role"],
        ["++add_auto_role <role-name>", "Adds to auto-role , these get randomly given"],
        ["++remove_auto_role <role-name>", "Remove from the list of auto-roles"],
        ["++scan_link <link> <phrase>", "Scans a link for a given phrase"]]
    for e in commands:
        help_embed.add_field(name=e[0],value=e[1],inline=True)
    await ctx.channel.send(embed=help_embed)


def get_link(msg):
    msg = str(msg)
    links = []
    try:
        msg = msg.split("http")
        msg.remove("")
        for e in msg:
            if e[0] == ":" or e[0:2] == "s:":
                links.append("http" + e)
        links_ = []
        for e in links:
            e = e.split(" ")
            links_.append(e[0])
        if len(links_) == 0:
            return False
        return links_
    except:
        return False
@cli.event
async def on_message(msg):
    await cli.process_commands(msg)
    BANNED_WORDS = read_db(DB_FILE_NAME, msg.guild.name, "BANNED_WORDS")
    for e in msg.content.lower().split(" "):
        if e in BANNED_WORDS:
            await msg.delete()
            break
    if read_db(DB_FILE_NAME,msg.guild.name,"SETTINGS")["SCAN_LINK"]:
        links = get_link(msg.content)
        f = False
        if links != False:
            for e in links:
                if f:
                    break
                for x in BANNED_WORDS:
                    if  x in str(requests.get(e).text.lower()):
                        await msg.delete()
                        await msg.channel.send("Inappropriate content found in the link...")
                        f = True
                        break
    try:
        AUTO_ROLES = read_db(DB_FILE_NAME,msg.guild.name,"AUTO_ROLES")
        rand_role = random.randint(0,100)
        if rand_role == 77:
            role_name = random.choice(AUTO_ROLES)
            guild = msg.guild
            role = discord.utils.get(guild.roles, name=role_name)
            member = msg.author
            if member is not None:
                await member.add_roles(role)
    except:
        pass

cli.run(TOKEN)

