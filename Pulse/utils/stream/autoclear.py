# Copyright (c) 2025 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: sudeepgithub@gmail.com

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass

from Pulse.platforms.Youtube import is_autoplay_on
from Pulse import YouTube
from Pulse.misc import db

async def auto_turn(chat_id, popped):
    if not popped or "vidid" not in popped:
        return
    if is_autoplay_on(chat_id):
        try:
            nxt = await YouTube.autoplay_next(popped["vidid"], chat_id)
            if nxt:
                db[chat_id] = [{
                    "file": f"vid_{nxt['vidid']}",
                    "title": nxt["title"],
                    "by": "Autoplay [Bot]",
                    "chat_id": popped.get("chat_id", chat_id),
                    "streamtype": "audio",
                    "vidid": nxt["vidid"],
                    "played": 0,
                    "dur": nxt["duration_min"],
                    "seconds": 0,
                }]
        except Exception:
            pass
