from datetime import datetime
from datetime import date
from math import floor
from sqlite3 import Timestamp
import time
import interactions
from interactions.ext.tasks import IntervalTrigger, create_task
import sqlite3

conn = sqlite3.connect('Countdowns.db')
try:
    conn.execute('''CREATE TABLE Countdowns (timestamp int,msgid int,channelid int,guildid int,roleid int,times int,length int,messagestart varchar(255),messageend varchar(255));''')
    print ("table made")
except:
    print("Table probably alredy there")

bot = interactions.Client(token="TOKEN")


allzones ={
  "UTC" : {"add": "0"},  
  "GMT" : {"add": "0"},
  "IBST" : {"add": "0"},
  "WET" : {"add": "0"},
  "Z" : {"add": "0"},
  "EGST" : {"add": "0"},
  "BST" : {"add": "1"},
  "CET" : {"add": "1"},
  "DFT" : {"add": "1"},
  "IST" : {"add": "1"},
  "MET" : {"add": "1"},
  "WAT" : {"add": "1"},
  "WEDT" : {"add": "1"},
  "WEST" : {"add": "1"},
  "CAT" : {"add": "2"},
  "CEDT" : {"add": "2"},
  "CEST" : {"add": "2"},
  "EET" : {"add": "2"},
  "HAEC" : {"add": "2"},
  "IST" : {"add": "2"},
  "MEST" : {"add": "2"},
  "SAST" : {"add": "2"},
  "USZ1" : {"add": "2"},
  "WAST" : {"add": "2"},
  "AST" : {"add": "3"},
  "EAT" : {"add": "3"},
  "EEDT" : {"add": "3"},
  "EEST" : {"add": "3"},
  "FET" : {"add": "3"},
  "IDT" : {"add": "3"},
  "IOT" : {"add": "3"},
  "MSK" : {"add": "3"},
  "SYOT" : {"add": "3"},
  "IRST" : {"add": "3.5"},
  "AMT" : {"add": "4"},
  "AZT" : {"add": "4"},
  "GET" : {"add": "4"},
  "GST" : {"add": "4"},
  "MUT" : {"add": "4"},
  "RET" : {"add": "4"},
  "SAMT" : {"add": "4"},
  "SCT" : {"add": "4"},
  "VOLT" : {"add": "4"},
  "AFT" : {"add": "4.5"},
  "IRDT" : {"add": "4.5"},
  "HMT" : {"add": "5"},
  "MAWT" : {"add": "5"},
  "MVT" : {"add": "5"},
  "ORAT" : {"add": "5"},
  "PKT" : {"add": "5"},
  "TFT" : {"add": "5"},
  "TJT" : {"add": "5"},
  "TMT" : {"add": "5"},
  "UZT" : {"add": "5"},
  "YEKT" : {"add": "5"},
  "IST" : {"add": "5.5"},
  "SLST" : {"add": "5.5"},
  "NPT" : {"add": "5.75"},
  "BDT" : {"add": "6"},
  "BIOT" : {"add": "6"},
  "BST" : {"add": "6"},
  "BTT" : {"add": "6"},
  "KGT" : {"add": "6"},
  "OMST" : {"add": "6"},
  "VOST" : {"add": "6"},
  "CCT" : {"add": "6.5"},
  "MMT" : {"add": "6.5"},
  "MST" : {"add": "6.5"},
  "CXT" : {"add": "7"},
  "DAVT" : {"add": "7"},
  "HOVT" : {"add": "7"},
  "ICT" : {"add": "7"},
  "KRAT" : {"add": "7"},
  "THA" : {"add": "7"},
  "WIT" : {"add": "7"},
  "ACT" : {"add": "8"},
  "AWST" : {"add": "8"},
  "BDT" : {"add": "8"},
  "CHOT" : {"add": "8"},
  "CIT" : {"add": "8"},
  "CST" : {"add": "8"},
  "CT" : {"add": "8"},
  "HKT" : {"add": "8"},
  "IRKT" : {"add": "8"},
  "MST" : {"add": "8"},
  "MYT" : {"add": "8"},
  "PST" : {"add": "8"},
  "SGT" : {"add": "8"},
  "SST" : {"add": "8"},
  "ULAT" : {"add": "8"},
  "WST" : {"add": "8"},
  "CWST" : {"add": "8.75"},
  "AWDT" : {"add": "9"},
  "EIT" : {"add": "9"},
  "JST" : {"add": "9"},
  "KST" : {"add": "9"},
  "TLT" : {"add": "9"},
  "YAKT" : {"add": "9"},
  "ACST" : {"add": "9.5"},
  "CST" : {"add": "9.5"},
  "AEST" : {"add": "10"},
  "ChST" : {"add": "10"},
  "CHUT" : {"add": "10"},
  "DDUT" : {"add": "10"},
  "EST" : {"add": "10"},
  "PGT" : {"add": "10"},
  "VLAT" : {"add": "10"},
  "ACDT" : {"add": "10.5"},
  "CST" : {"add": "10.5"},
  "LHST" : {"add": "10.5"},
  "AEDT" : {"add": "11"},
  "BST" : {"add": "11"},
  "KOST" : {"add": "11"},
  "LHST" : {"add": "11"},
  "MIST" : {"add": "11"},
  "NCT" : {"add": "11"},
  "PONT" : {"add": "11"},
  "SAKT" : {"add": "11"},
  "SBT" : {"add": "11"},
  "SRET" : {"add": "11"},
  "VUT" : {"add": "11"},
  "NFT" : {"add": "11"},
  "FJT" : {"add": "12"},
  "GILT" : {"add": "12"},
  "MAGT" : {"add": "12"},
  "MHT" : {"add": "12"},
  "NZST" : {"add": "12"},
  "PETT" : {"add": "12"},
  "TVT" : {"add": "12"},
  "WAKT" : {"add": "12"},
  "CHAST" : {"add": "12.75"},
  "NZDT" : {"add": "13"},
  "PHOT" : {"add": "13"},
  "TKT" : {"add": "13"},
  "TOT" : {"add": "13"},
  "CHADT" : {"add": "13.75"},
  "LINT" : {"add": "14"},
  "AZOST" : {"add": "-1"},
  "CVT" : {"add": "-1"},
  "EGT" : {"add": "-1"},
  "BRST" : {"add": "-2"},
  "FNT" : {"add": "-2"},
  "GST" : {"add": "-2"},
  "PMDT" : {"add": "-2"},
  "UYST" : {"add": "-2"},
  "NDT" : {"add": "-2.5"},
  "ADT" : {"add": "-3"},
  "AMST" : {"add": "-3"},
  "ART" : {"add": "-3"},
  "BRT" : {"add": "-3"},
  "CLST" : {"add": "-3"},
  "FKST" : {"add": "-3"},
  "FKST" : {"add": "-3"},
  "GFT" : {"add": "-3"},
  "PMST" : {"add": "-3"},
  "PYST" : {"add": "-3"},
  "ROTT" : {"add": "-3"},
  "SRT" : {"add": "-3"},
  "UYT" : {"add": "-3"},
  "NST" : {"add": "-3.5"},
  "NT" : {"add": "-3.5"},
  "AMT" : {"add": "-4"},
  "AST" : {"add": "-4"},
  "BOT" : {"add": "-4"},
  "CDT" : {"add": "-4"},
  "CLT" : {"add": "-4"},
  "COST" : {"add": "-4"},
  "ECT" : {"add": "-4"},
  "EDT" : {"add": "-4"},
  "FKT" : {"add": "-4"},
  "GYT" : {"add": "-4"},
  "PYT" : {"add": "-4"},
  "VET" : {"add": "-4.5"},
  "ACT" : {"add": "-5"},
  "CDT" : {"add": "-5"},
  "COT" : {"add": "-5"},
  "CST" : {"add": "-5"},
  "EASST" : {"add": "-5"},
  "ECT" : {"add": "-5"},
  "EST" : {"add": "-5"},
  "PET" : {"add": "-5"},
  "CST" : {"add": "-6"},
  "EAST" : {"add": "-6"},
  "GALT" : {"add": "-6"},
  "MDT" : {"add": "-6"},
  "MST" : {"add": "-7"},
  "PDT" : {"add": "-7"},
  "AKDT" : {"add": "-8"},
  "CIST" : {"add": "-8"},
  "PST" : {"add": "-8"},
  "AKST" : {"add": "-9"},
  "GAMT" : {"add": "-9"},
  "GIT" : {"add": "-9"},
  "HADT" : {"add": "-9"},
  "MART" : {"add": "-9.5"},
  "MIT" : {"add": "-9.5"},
  "CKT" : {"add": "-10"},
  "HAST" : {"add": "-10"},
  "HST" : {"add": "-10"},
  "TAHT" : {"add": "-10"},
  "NUT" : {"add": "-11"},
  "SST" : {"add": "-11"},
  "BIT" : {"add": "-12"}
}

def writeinfile(mention, timestamp,msg,guildid,times,length, messagestart, messageend="!"):
    if msg.id == None:
        return True
    if msg.channel_id == None:
        return True
    if guildid == None:
        return True
    if mention != "0":
        roleid = mention.id
    else:
        roleid = 0
    messagestart = messagestart.replace("'", "’")
    messageend = messageend.replace("'", "’")
    conn.execute("INSERT INTO Countdowns (timestamp,msgid,channelid,guildid,roleid,times,length,messagestart,messageend) VALUES ("+str(timestamp)+","+str(msg.id)+","+str(msg.channel_id)+","+str(guildid)+","+str(roleid)+","+str(times)+","+str(length)+", '"+str(messagestart)+"' , '"+str(messageend)+"');")
    conn.commit()
    return False

def timezonemath(timestamp, zone):
    timestamp = timestamp + 3600
    try:
        difference = (int(allzones[(zone.upper())]["add"])*3600)
        timestamp = timestamp - difference
        return timestamp
    except KeyError:
        return("Timezone doesn't exist")


@bot.command(
    name="help",
    description="Shows a help message",
)

async def help(ctx: interactions.CommandContext):
    await ctx.send(f"```Help message```\nThis bot got 6 commands: Countdown, timer, channel, delete, deleteallinchannel and help.\n**Countdown**\nCountdown will show the remaining time until the date you entered. It defaults to 12 (noon) the current day and timezone is UTC.\n**Timer**\nTimer will allow you to start a timer that will run for the duration you enter. Timers can be repeated by using the times option. (I.e starting a timer for 7 minutes will notify you in 7 minutes)\n**Channel**\nIt will show you all active countdowns in this channel.\n**Delete**\nEnter the message id for the countdown you want to delete and it will stop. You can find message id as the last number when using /channel\n**Deleteallinchannel**\nDeletes all countdowns in the channel\n**Help**\nShows this help message.")


@bot.command(
    name="countdown",
    description="Countdown to an exact date. (hour and minute means hour and minute of the day)",
    options = [
        interactions.Option(
            name="day",
            description="What day (default to current)",
            type=4,
            required=False,
            max_value=31,
        ),
        interactions.Option(
            name="month",
            description="What month (defaults to current)",
            type=4,
            required=False,
            max_value=12,
        ),
        interactions.Option(
            name="year",
            description="What year (defaults to current)",
            type=4,
            required=False,
        ),
        interactions.Option(
            name="hour",
            description="What hour (defaults to 12)",
            type=4,
            required=False,
            max_value=23,
        ),
        interactions.Option(
            name="minute",
            description="What minute (defaults to 00)",
            type=4,
            required=False,
            max_value=59,
        ),
        interactions.Option(
            name="messagestart",
            description="Custom message before timer",
            type=3,
            max_length=100,
            required=False,
        ),
        interactions.Option(
            name="messageend",
            description="Custom message after timer",
            type=3,
            max_length=100,
            required=False,
        ),
        interactions.Option(
            name="mention",
            description="Who to mention",
            type=9,
            required=False,
        ),
        interactions.Option(
            name="timezone",
            description="What timezone",
            type=3,
            required=False,
        ),
    ],
)

async def countdown(ctx: interactions.CommandContext, day="", month="", year="", hour="12", minute="00", messagestart="Countdown will end", messageend="", mention="0", timezone="UTC"):

    try:
        int(day)
    except:
        day = str(date.today().day)
    
    try:
        int(month)
    except:
        month = str(date.today().month)

    try:
        int(year)
    except:
        year = str(date.today().year)

    working = False
    try:
        wholedate = datetime.strptime( str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":00,00", "%Y-%m-%d %H:%M:%S,%f")  
        timestamp = floor(wholedate.timestamp())
        timestamp = timezonemath(timestamp,timezone)
        currenttime = floor(time.time())
        try:
            if int(currenttime) < int(timestamp):
                response = messagestart + " <t:" + str(timestamp) + ":R> " + messageend
                working = True
            
            else: 
                response = "You cant set time in the past. You can try adding in more variables."
        except:
            response = "not a valid timezone"
    except:
        response ="not a valid date. Remember that it need to be a date!"

    msg = await ctx.send(f"{response}!")
    guildid = ctx.guild_id
    if working == True:
        writeerror = writeinfile(mention,timestamp,msg,guildid,"0","0", messagestart, messageend)
        if writeerror:
            await ctx.send(f"SOMETHING WENT WRONG")


@bot.command(
    name="timer",
    description="Lets add a timer",
    options = [
        interactions.Option(
            name="minute",
            description="How many minutes",
            type=4,
            required=False,
        ),
        interactions.Option(
            name="hour",
            description="How many hours",
            type=4,
            required=False,
        ),
        interactions.Option(
            name="day",
            description="How many days",
            type=4,
            required=False,
        ),
        interactions.Option(
            name="week",
            description="How many weeks",
            type=4,
            required=False,
        ),
        interactions.Option(
            name="messagestart",
            description="Custom message before timer",
            type=3,
            max_length=100,
            required=False,
        ),
        interactions.Option(
            name="messageend",
            description="Custom message after timer",
            type=3,
            max_length=100,
            required=False,
        ),
        interactions.Option(
            name="mention",
            description="Who to mention",
            type=9,
            required=False,
        ),  
        interactions.Option(
            name="times",
            description="Number of times to repeat",
            type=4,
            required=False,
        ),
    ],
)

async def timer(ctx: interactions.CommandContext, day="0", week="0", hour="0", minute="0", messagestart="Timer will end", messageend="", mention="0", times="0"):
    currenttime = floor(time.time())
    length = int(minute) * 60 + int(hour) * 3600 + int(day) * 86400 + int(week) * 604800
    timestamp = currenttime + length
    response = messagestart + " <t:" + str(timestamp) + ":R> " + messageend
    msg = await ctx.send(f"{response}!")
    guildid = ctx.guild_id
    writeerror = writeinfile(mention,timestamp,msg,guildid,times,length, messagestart, messageend)
    if writeerror:
        await ctx.send(f"SOMETHING WENT WRONG")
    
@bot.command(
    name="channel",
    description="Show countdowns for this channel",
)

async def channel(ctx: interactions.CommandContext):
    channelid = str(ctx.channel_id)
    cursor = conn.execute("SELECT timestamp,msgid,guildid FROM Countdowns WHERE channelid = "+str(channelid)+" ORDER BY timestamp ASC;")
    result = "Active countdowns in this channel: \n"
    for row in cursor:
        msgid = int(row[1])
        timeid = int(row[0])
        guildid = int(row[2])
        if len(result) < 1800:
            result = result + "<t:"+str(timeid)+":R> https://discord.com/channels/" + str(guildid) +"/"+str(channelid)+"/"+str(msgid)+"\n"
        else:
            result = result + "There are more active countdowns, but not enough space to show them in this message."
            break
    if result == "Active countdowns in this channel: \n":
        result = "No countdowns in this channel"
    await ctx.send(result)


@bot.command(
    name="delete",
    description="Delete a countdown in this channel",
    options = [
        interactions.Option(
            name="msgid",
            description="Enter message ID that you want to delete.",
            type=3,
            required=True
        )
    ]   
)

async def delete(ctx: interactions.CommandContext, msgid):
    channelid = str(ctx.channel_id)
    check = conn.total_changes
    conn.execute("DELETE from Countdowns WHERE msgid = "+str(msgid)+" AND channelid = "+str(channelid)+";")
    conn.commit()
    if check == conn.total_changes:
        result = "An error occourd"
    else:
        result = "Countdown Deleted"
    await ctx.send(result)


@bot.command(
    name="deleteallinchannel",
    description="Delete all countdowns in this channel",  
)

async def delete(ctx: interactions.CommandContext):
    result = "Not deleted"
    channelid = str(ctx.channel_id)
    check = conn.total_changes
    conn.execute("DELETE from Countdowns WHERE channelid = "+str(channelid)+";")
    conn.commit()
    if check == conn.total_changes:
        result = "An error occourd"
    else:
        result = "Countdown(s) Deleted"
    await ctx.send(result)


@create_task(IntervalTrigger(5))
async def timer_check():
    currenttime = time.time()
    cursor = conn.execute("SELECT timestamp,msgid,channelid,guildid,roleid,times,length,messagestart,messageend FROM Countdowns WHERE timestamp < "+str(currenttime)+";")
    for row in cursor:
        messageend = str(row[8])
        messagestart = str(row[7])
        length = int(row[6])
        times = int(row[5])
        roleid = int(row[4])
        guildid = int(row[3])
        channelid = int(row[2])
        msgid = int(row[1])
        timestamp = int(row[0])

        channel = interactions.Channel(**await bot._http.get_channel(channelid), _client=bot._http)
        content = messagestart + " <t:" + str(timestamp) + "> " + messageend
        if roleid != 0:
            try:
                await interactions.get(bot, interactions.User, object_id=roleid)
                await channel.send("<@" + str(roleid)+"> A countdown mentioning you is done! It said:\n"+content)
            except:
                await channel.send(" A countdown mentioning" + f"{'<@&' + str(roleid) + '>' if roleid != guildid else '@everyone'}" + "is done! It said:\n"+content, allowed_mentions={"parse":["roles", "everyone"]})
        else:
            await channel.send("A countdown is done! It said:\n" + content)
        if times != 0:
            times = times-1
            timestamp = timestamp + length
            await channel.send("This countdown will be repeated " + str(times) + " time(s) more. next time is: <t:" + str(timestamp) + ":R>")
            conn.execute("UPDATE Countdowns set times = "+str(times)+" where msgid = "+str(msgid)+";")
            conn.execute("UPDATE Countdowns set timestamp = "+str(timestamp)+" where msgid = "+str(msgid)+";")
            conn.commit()
        else:
            conn.execute("DELETE from Countdowns WHERE msgid = "+str(msgid)+" AND channelid = "+str(channelid)+";")
            conn.commit()
    

timer_check.start()

bot.start()