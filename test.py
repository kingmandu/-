import discord
import time
import asyncio
import os

text = "0"
repeat = 0
onOff = [False, False]
Te1xt = ""

client = discord.Client()


@client.event
async def on_message(message):
    global text, repeat
    if message.content == "와! 샌즈!":
        embed = discord.Embed(title="안녕? 꼬마!", description="핫도그 먹기 좋은날이야. 그렇지?", color=0x62c1cc)
        embed.set_thumbnail(url="https://i.imgur.com/4SL7iSB.png")
        await message.channel.send(embed=embed)

    if message.content == "샌즈 방어모드@":
        await message.channel.send("샌즈봇 방어모듈 해제")

    if message.content == "샌즈 전투모드@":
        await message.channel.send("샌즈봇 가스터블레스트 해제")
    # 디도스
    if message.content == "샌즈 사용자 인터페이스 확인":
        await message.channel.send("명령어의 작동이 감지되었습니다.")
        await asyncio.sleep(1)
        await message.channel.purge(limit=2)
        await message.channel.send("사용자를 확인합니다.")
        await asyncio.sleep(1)
        await message.channel.purge(limit=1)

    if message.content == "사용자를 확인합니다.":
        await asyncio.sleep(2)
        await message.channel.send("동의 하시려면 Y! 거부하시려면 N!를 입력해주세요")
        msg = await client.wait_for("message")
        if msg.content == "Y!":
            await message.channel.purge(limit=2)
            await message.channel.send("사용자를 확인중입니다.")
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
            await message.channel.send("5 Second")
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
            await message.channel.send("4 Second")
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
            await message.channel.send("3 Second")
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
            await message.channel.send("2 Second")
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
            await message.channel.send("1 Second")
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)

    if message.content == "1 Second":
        await asyncio.sleep(2)
        await message.channel.send("확인되었습니다.")
        msg = await client.wait_for("message")
        if msg.content == "샌즈 전투모드!":
            await message.channel.purge(limit=1)
            embed = discord.Embed(title="새는 지저귀고. 꽃들은 피어나고", description="정말 아름다운 날이야. 그렇지?", color=0x62c1cc)
            embed.add_field(name="이런날에", value="너같은 꼬마들은", inline=False)
            embed.add_field(name="지.옥.에.서.불.타.버.려.야.해", value="준비됐어?", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/5MCEnYA.gif")
            await message.channel.send(embed=embed)
            await message.channel.send("샌즈봇 가스터블레스트 장착")
            await message.channel.send("전투모듈 실행")
        elif msg.content == "샌즈 방어모드!":
            await message.channel.purge(limit=1)
            embed = discord.Embed(title="물어볼게 하나있어", description="가장 나쁜 사람이라 할지라도 바뀔 수 있을까...?", color=0x62c1cc)
            embed.add_field(name="노력만 한다면", value="모두가 착한 사람이 될 수 있을까", inline=False)
            embed.add_field(name="죄송해요, 아주머니.", value="이게 바로 제가 약속을 안 하는 이유예요", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/SniTvyM.jpg")
            await message.channel.send(embed=embed)
            await message.channel.send("샌즈봇 방어모듈 장착")

    if message.content == "N!":
        await message.channel.purge(limit=2)
        await message.channel.send("취소되었습니다.")

    global onOff
    if onOff[0]:
        if message.content == "전투모듈 실행":
            for x in range(1, 4):
                embed = discord.Embed(title="", description="", color=0x62c1cc)
                embed.set_image(url="https://i.imgur.com/SjQ6KlU.jpg")
                await message.channel.send(embed=embed)
    if onOff[1]:
        await message.delete()

    param = message.content.split()
    if message.content.startswith("샌즈봇"):  # 명령
        if not param[2] == "장착" and not param[2] == "해제":
            await message.channel.send("Error 00601 : 지원하지 않는 형식입니다. (on/off 만 입력 가능)")

        elif param[1] == "가스터블레스트":  # 기능 이름
            if param[2] == "해제":
                if onOff[0]:  # 나중에 함수로
                    onOff[0] = False
                    await message.channel.send("[" + param[1] + "의 착용을 해제했습니다.]")
                else:
                    await message.channel.send("Error 00603 : 중복명령어 사용됨.")
            elif param[2] == "장착":
                if not onOff[0]:
                    onOff[0] = True
                    await message.channel.send("[" + param[1] + "를 장착했습니다.]")
                else:
                    await message.channel.send("Error 00604 : 중복명령어 사용됨.")

        elif param[1] == "방어모듈":  # 기능 이름
            if param[2] == "해제":
                if onOff[1]:  # 나중에 함수로
                    onOff[1] = False
                    await message.channel.send("[" + param[1] + "의 착용을 해제했습니다.]")
                else:
                    await message.channel.send("Error 00603 : 중복명령어 사용됨.")
            elif param[2] == "장착":
                if not onOff[1]:
                    onOff[1] = True
                    await message.channel.send("[" + param[1] + "중복명령어 사용됨.]")
                else:
                    await message.channel.send("Error 00604 : 이미 켜져 있는 명령입니다.")
        else:
            await message.channel.send("Error 00602 : 알 수 없는 관리 명령입니다.")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
