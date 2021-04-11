import requests
import json
import time

auth = {
    "authorization": "put your token here"
}

ids = []

while True:
    getLastMessageJson = requests.get("https://discord.com/api/v8/channels/{channel.id}/messages?limit=1", headers=auth)
    lastMessage = json.loads(getLastMessageJson.text)
    lastMessage = lastMessage[0]['content']
    lastMessageId = json.loads(getLastMessageJson.text)
    lastMessageId = lastMessageId[0]['id']
    if lastMessageId in ids:
        pass
    if lastMessageId not in ids:
        ids.append(lastMessageId)
        if "https://www.youtube.com/watch?v=" in lastMessage:
            try:
                youtubeVideoId = lastMessage[lastMessage.find("https://www.youtube.com/watch?v=")+32:lastMessage.find("https://www.youtube.com/watch?v=")+11+32]
                getYoutubeVideo = requests.get("https://www.youtube.com/watch?v=" + youtubeVideoId)
                t1 = getYoutubeVideo.text.find("<title>")
                t2 = getYoutubeVideo.text.find("</title>")
                youtubeVideoTitle = getYoutubeVideo.text[t1 + 7:t2]
                messageContent = f"Video title: `{youtubeVideoTitle}`"
                payload = {
                    "content": messageContent
                }
                sendPacket = requests.post("https://discord.com/api/v8/channels/{channel.id}/messages", data=payload, headers=auth)
            except Exception as e:
                print(e)
    time.sleep(0.25)
