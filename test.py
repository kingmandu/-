import asyncio
import discord

text = "0"
repeat = 0
Te1xt = ""
client = discord.Client()

욕설 = ("젠장", "대머", "닥쳐", "야발", "ㅅㅂ", "시발", "씨발", "새끼", "병신", "썅년", "1발", "@발", " 발", "!발", "1끼", "@끼", "!끼","창년", "애미", "기미", "느금", "발!", "찌발")


@client.event
async def on_message(message):
    global text, repeat

    if message.content == "도움말!":
        embed = discord.Embed(title="클리어! 숫자", description="지정한 값만큼 체팅을 지웁니다.", color=0x62c1cc)
        embed.add_field(name="타이머! 숫자", value="지정한 값만큼 카운트를 세어줍니다.", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/GkHolcc.png")
        await message.channel.send(embed=embed)

    for i in range(0, len(message.content) - 1):
        part = message.content[i:i + 2]
        if part in 욕설:
            embed = discord.Embed(title="욕설 감지됨", description="욕설 사용 자제", color=0x62c1cc)
            embed.set_thumbnail(url="https://i.imgur.com/5kvan9P.png")
            await message.channel.send(embed=embed)
            await message.delete()
            break

    if message.content == "클리어! all":
        await message.channel.purge(limit=1000)

    if message.content.startswith("타이머!"):

        learn = message.content.split()
        sec = int(learn[1])

        for i in range(sec, 0, -1):
            await message.channel.send(embed=discord.Embed(description='타이머 : ' + str(i) + ' Second'))
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
        await message.channel.send(embed=discord.Embed(description='타이머 종료'))

    if message.content.startswith("클리어!"):

        learn = message.content.split(" ")
        sec = int(learn[1])

        for i in range(sec + 1, 0, -1):
            await message.channel.purge(limit=1)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
