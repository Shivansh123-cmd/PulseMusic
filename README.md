<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=PulseMusic&fontSize=80&animation=fadeIn&fontAlignY=35&desc=A%20Modern,%20Fast%20and%20Secure%20Telegram%20Music%20Bot&descAlignY=55&descAlign=50" />
</p>

<p align="center">
<a href="https://github.com/SUDEEPBOTS/PulseMusic/stargazers"><img src="https://img.shields.io/github/stars/SUDEEPBOTS/PulseMusic?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/SUDEEPBOTS/PulseMusic/network/members"> <img src="https://img.shields.io/github/forks/SUDEEPBOTS/PulseMusic?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/SUDEEPBOTS/PulseMusic/issues"> <img src="https://img.shields.io/github/issues/SUDEEPBOTS/PulseMusic?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/SUDEEPBOTS/PulseMusic/pulls"> <img src="https://img.shields.io/github/issues-pr/SUDEEPBOTS/PulseMusic?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/SUDEEPBOTS/PulseMusic/blob/main/LICENSE"> <img src="https://img.shields.io/github/license/SUDEEPBOTS/PulseMusic?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<br>
<a href="https://t.me/Zcziiyy"><img src="https://img.shields.io/badge/Join-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/Zcziiyy"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=25&pause=1000&color=F700FF&center=true&vCenter=true&width=435&lines=Powered+by+Pyrogram;Powered+by+PyTgCalls;Advanced+Security+Guards;Modern+%26+Fast+Music+Bot" alt="Typing SVG" />
</p>

---

## 🌟 ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs 

- **🔥 ʟᴀᴛᴇsᴛ ᴘʏʀᴏɢʀᴀᴍ & ᴘʏᴛɢᴄᴀʟʟs sᴜᴘᴘᴏʀᴛ:** Uses the newest, fastest, and most stable libraries for seamless voice chat streaming.
- **🛡️ ᴀᴅᴠᴀɴᴄᴇᴅ sᴇᴄᴜʀɪᴛʏ:** Built-in RCE/Shell-injection blocks & NSFW query filters to keep your bot safe.
- **✨ ᴘʀᴇᴍɪᴜᴍ ᴜɪ:** Beautiful inline keyboards with modern custom emojis and formatted text.
- **♾️ sᴍᴀʀᴛ ᴀᴜᴛᴏᴘʟᴀʏ:** Never let the music stop! Auto-queues related songs perfectly.
- **⚡️ ᴍᴏᴅᴇʀɴ & ʟɪɢʜᴛᴡᴇɪɢʜᴛ:** Optimized for speed, utilizing `cloudflared` & lightweight async methods.
- **🚀 ʀᴇɴᴅᴇʀ & ʜᴇʀᴏᴋᴜ ʀᴇᴀᴅʏ:** Built-in keeping-alive web server for seamless free-tier hosting on Render & Heroku.

---

## 🚀 ᴅᴇᴘʟᴏʏᴍᴇɴᴛ

<details>
<summary><b>🔥 ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ & ʀᴇɴᴅᴇʀ</b></summary>
<br>
<p align="center">
<a href="https://dashboard.heroku.com/new?template=https://github.com/SUDEEPBOTS/PulseMusic">
  <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-008000?style=for-the-badge&logo=heroku" width="200" height="40"/>
</a>
<a href="https://render.com/deploy?repo=https://github.com/SUDEEPBOTS/PulseMusic">
  <img src="https://img.shields.io/badge/Deploy%20to%20Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" width="200" height="40"/>
</a>
</p>
</details>

<details>
<summary><b>💻 ᴅᴇᴘʟᴏʏ ᴏɴ ᴠᴘs / ʟᴏᴄᴀʟ</b></summary>
<br>

**1. Clone the Repository:**
```bash
git clone https://github.com/SUDEEPBOTS/PulseMusic
cd PulseMusic
```

**2. Install Dependencies:**
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install python3-pip ffmpeg -y
pip3 install -U -r requirements.txt
```

**3. Configure Environment:**
```bash
cp sample.env .env
nano .env # Fill in your API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI
```

**4. Start the Bot:**
```bash
python3 -m Pulse
# OR keep it running in background
tmux new-session -d -s pulsebot "bash start"
```
</details>

---

## ⚙️ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ᴠᴀʀɪᴀʙʟᴇs

- `API_ID` - Get this from my.telegram.org.
- `API_HASH` - Get this from my.telegram.org.
- `BOT_TOKEN` - Get this from @BotFather.
- `MONGO_DB_URI` - Your MongoDB cluster URI from mongodb.com.
- `OWNER_ID` - Your Telegram User ID.
- `LOGGER_ID` - A Telegram Group ID where the bot will send logs (Add bot as admin).
- `RENDER` - Set this to `True` if deploying on Render to activate keep-alive.
- `PING_URL` - Your Render application URL for keep-alive ping.

---

## 📞 sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇs

For all updates, features requests, and bug reports, join our support channels:

<p align="center">
  <a href="https://t.me/Zcziiyy"><img src="https://img.shields.io/badge/Join%20Support%20Group-blue.svg?style=for-the-badge&logo=Telegram" width="250"></a>
</p>

---
<p align="center">
  <b>Made with ❤️ by <a href="https://github.com/SUDEEPBOTS">SUDEEPBOTS</a></b><br>
  Licensed under the <a href="LICENSE">MIT License</a>.
</p>
