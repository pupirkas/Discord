import discord
import config as conf
import youtube_dl
from discord.ext import commands
from discord.utils import get
import random
import os

'''
@client.event
async def om_member_join(member):
	await ctx.send(f'reaction1')
	role  = discord.utils.get(member.server.roles, name = "new role")
	await Bot.add_roles(member, role)

@client.event
async def on_message(ctx, message):
	print('Message from {0.author}: {0.content}'.format(message))


'''
client = commands.Bot(command_prefix='.')

players = {}

@client.event
async def on_ready():
	print('Bot is ready')

@client.command()

# ping(ms)
async def ping(ctx):
	await ctx.send(f'Your ping is {round(client.latency * 1000)} ms')

@client.command(aliases = ['1question', 'test'])

# questions
async def _1question(ctx, *, question):
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(conf.responce)}')

@client.command()

# clear
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount+1)
	print('\n\nБот очистил {0} сообщений'.format(amount))


@client.command(pass_context = True, aliases = ['j','joi'])

async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild= ctx.guild)

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
	await voice.disconnect()

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		print(f'The bot has connected to {channel}\n')

	await ctx.send(f'Joined {channel}')

@client.command(pass_context = True, aliases = ['l','lea'])

async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild= ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		print(f'The bot has left {channel}')
		await ctx.send(f'Left {channel}')
	else:
		print('Bot was told to leave voice channel, but was not in one')
		await ctx.send("Don't think I am in a voice channel")

@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

	song_there = os.path.isfile("song.mp3")
	try:		 
		if song_there:
			os.remove("song.mp3")
			print("Removed old song file")
	except PermissionError:
		print("Trying to delete song file, but it's being played")
		await ctx.send("ERROR: Music playing")
		return

	await ctx.send("Getting everything ready now")

	voice = get(client.voice_clients, guild=ctx.guild)



	with youtube_dl.YoutubeDL(conf.ydl_opts) as ydl:
		print("Downloading audio now\n")
		ydl.download([url])

	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			name = file
			print(f"Renamed File: {file}\n")
			os.rename(file, "song.mp3")

	voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 2

	nname = name.rsplit("-", 2)
	await ctx.send(f"Playing: {nname[0]}")
	print("playing\n")

@client.command()
async def pause(ctx):
	voice = get(client.voice_clients, guild= ctx.guild)
	if voice.is_playing():
		voice.pause()
	else:
		await ctx.send('Currently no audio is playing')

@client.command()
async def resume(ctx):
	voice = get(client.voice_clients, guild= ctx.guild)
	if voice.is_paused():
		voice.resume()
	else:
		await ctx.send('The audio is not paused')
@client.command()
async def stop(ctx):
	voice = get(client.voice_clients, guild= ctx.guild)
	voice.stop()

	#continue
'''
@client.command(pass_context = True)

# join
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)

@client.command(pass_context = True)

# leave
async def leave(ctx):
	guild = ctx.message.guild
	voice_client = guild.voice_client
	await voice_client.disconnect()

@client.command(pass_context = True)

# play
async def play(ctx, url):
	guild = ctx.message.guild
	voice_client = guild.voice_client
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	player.start()
'''
client.run(conf.TOKEN)