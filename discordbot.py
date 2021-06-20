import discord
import random
import pickle
import os

TOKEN = "YOURTOKENHERE"
path = "Your project path here"

client = discord.Client()
@client.event
async def on_ready():
    print("Botchan Ready to serve")
text_path = os.path.join(path,"text.sav")
try:
    file = open(text_path,"rb")
    texten = pickle.load(file)
    file.close
except:
    texten = []
    texten.append("Hello")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    randomizer = random.randint(0,len(texten)-1)
    random2 = random.randint(1,1) #返信を行う頻度を変更可能 ex) ...randint(1,100) 1%の確立で返信
    if random2 == 1:
        await message.channel.send(texten[randomizer])
    if message.content.startswith("Save"):  #誰かがSaveと発言すると蓄積したデータが実際にファイルに保存される。
        file =open(text_path, "wb")
        pickle.dump(texten,file)
        file.close()
        print("textfile Saved!")
    else:
        texten.append(message.content)

client.run("ODU1ODI5NDExMTYwMTI5NTU4.YM4LQA.IJJDIoQwAgzUNLZhuZ3OBRjYYMM")
