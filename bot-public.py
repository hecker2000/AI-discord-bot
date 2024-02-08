import random
import asyncio
import discord
import ffmpeg

intents = discord.Intents.default()
intents.message_content = True

from gpt4all import GPT4All
# you will have to install an LLM, any should do, but this is the default.
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")
client = discord.Client(intents=intents)

# DO NOT LEAVE THIS EMPTY, if you want the AI to at least be smart

system_template = 'you are a helpful assistant AI that helps users with any task they give'
AIname = 'assistant'

#enter your discord ID here
DISCORDid = ''
#enter the bot's token here
TOKEN = ''


prompt_template = '{1}: {0}\n{AIname}]: '
pro_template = '{1}: {0}\n{AIname}: {2}'
output = 'nul'

#this sould lead to some MP3 file, make sure that they are at most 5 seconds, anymore than that will break the bot
soundfile = [

]

#this should be the directory of ffmpeg.exe
ffm = """ffmpeg.exe"""

#dont touch this
me1 = ''
me2 = ''
me3 = ''
me4 = ''
me5 = ''

def cutforwardtext(message, cutafter, replacement):
    message = message.split(cutafter)[0]
    if replacement != '':
        message = message + replacement
    return message

async def yip(message, times):
    await client.change_presence(status=discord.Status.dnd, activity=discord.CustomActivity(name='In voice chat' ,emoji='🔊'))
    channel = message.author.voice.channel
    vc = await channel.connect()
    for x in range(times):
        await asyncio.sleep(random.randint(1,5))
        leng = random.randint(0, len(soundfile) - 1)
        vc.play(discord.FFmpegPCMAudio(executable=ffm, source=soundfile[leng]))
        await asyncio.sleep(random.randint(7,13))
    await vc.disconnect()
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Waiting' ,emoji='🖥️'))



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='{AIname} has started' ,emoji='🖥️'))


@client.event
async def on_message(message):
    await client.change_presence(status=discord.Status.dnd, activity=discord.CustomActivity(name='Typing' ,emoji='🖥️'))
    global me1
    global me2
    global me3
    global me4
    global me5
    if message.author == client.user:
        return
    if message.content == 'nul':
        return

    
    if message.author.id == int(DISCORDid):
        if message.content == ': clear':
            me1 = ''
            me2 = ''
            me3 = ''
            me4 = ''
            me5 = ''
            await message.channel.send('cleared message history')
        if message.content.startswith(': vc'):
            if message.content == ': vc':
                await yip(message, 1)
            else:
                temp = message.content.split(': vc ')[1]
                await yip(message, int(temp))

        if message.content == ": leave":
            to_leave = client.get_guild(message.guild.id)
            await to_leave.leave()

    if not message.content.startswith(':'):
        me1 = me2
        me2 = me3
        me3 = me4
        me4 = me5
        me5 = prompt_template.format(message.content, message.author.global_name)
        promt = system_template + "\n" + me1 + "\n" + me2 + "\n" + me3 + "\n" + me4 + "\n" + me5

        print(promt)
        print('generating')
        output = model.generate(promt, max_tokens=70, temp=0.27)
        print(output)
        output = cutforwardtext(output, "\n", "")
        print(output)
        me5 = pro_template.format(message.content, message.author.global_name, output)
        if output != 'nul':
            await message.channel.send(output)
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Waiting' ,emoji='🖥️'))
    if random.randint(1, 11) == 1:
        if message.author.voice.channel != None:
            await asyncio.sleep(5)
            await yip(message, random.randint(1, 2))

client.run(TOKEN)
