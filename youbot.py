import requests
import json
import time

auth = {
    "authorization": "token"
}

ids = []

channelId = input("Channel ID: ")

while True:
    getLastMessageJson = requests.get(f"https://discord.com/api/v8/channels/{channelId}/messages?limit=1", headers=auth)
    lastPacket = json.loads(getLastMessageJson.text)
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
                youtubeVideoTitle = youtubeVideoTitle.replace("- YouTube", "")
                messageContent = f"Video title: `{youtubeVideoTitle}`"
                payload = {
                    "content": messageContent
                }
                sendPacket = requests.post(f"https://discord.com/api/v8/channels/{channelId}/messages", data=payload, headers=auth)
                if sendPacket.status_code != 200:
                    waitTime = json.loads(sendPacket.text)
                    waitTime = waitTime['retry_after']
                    time.sleep(int(waitTime))
                    sendPacket = requests.post(f"https://discord.com/api/v8/channels/{channelId}/messages", data=payload, headers=auth)
                print(messageContent)
            except Exception as e:
                print(e)
        if "https://youtu.be/" in lastMessage:
            try:
                youtubeVideoId = lastMessage[lastMessage.find("https://youtu.be/") + 17:lastMessage.find("https://youtu.be/") + 17 + 11]
                getYoutubeVideo = requests.get("https://youtu.be/" + youtubeVideoId)
                t1 = getYoutubeVideo.text.find("<title>")
                t2 = getYoutubeVideo.text.find("</title>")
                youtubeVideoTitle = getYoutubeVideo.text[t1 + 7:t2]
                youtubeVideoTitle = youtubeVideoTitle.replace("- YouTube", "")
                messageContent = f"Video title: `{youtubeVideoTitle}`"
                payload = {
                    "content": messageContent
                }
                sendPacket = requests.post(f"https://discord.com/api/v8/channels/{channelId}/messages", data=payload, headers=auth)
                if sendPacket.status_code != 200:
                    waitTime = json.loads(sendPacket.text)
                    waitTime = waitTime['retry_after']
                    time.sleep(int(waitTime))
                    sendPacket = requests.post(f"https://discord.com/api/v8/channels/{channelId}/messages", data=payload, headers=auth)
                print(messageContent)
            except Exception as e:
                print(e)
    time.sleep(0.25)
