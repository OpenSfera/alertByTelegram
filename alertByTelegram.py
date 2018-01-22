# sudo pip3 install telepot
import telepot
import json
import paho.mqtt.client as mqtt
import sferaconfig

def on_message(client, userdata, msg):
    message = json.loads(msg.payload.decode("UTF-8"))
    if message["type"] in set(["user_alert"]):
        alertMessage  = "Severity: "+message["severity"]+"\n"
        alertMessage += "Type: "+message["message_type"]+"\n"
        alertMessage += "Source: "+message["who"]+"\n"
        alertMessage += "hear `"+message["heared"]+"` expected was `"+message["expected"]+"`\n"
        try:
            config = sferaconfig.getConfig("alert_by_telegram", {"bot_api_key": "XXX", "chat_id":"123456"})
            bot = telepot.Bot(config["bot_api_key"])
            bot.sendMessage(config["chat_id"], alertMessage)
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

def on_connect(client, userdata, flags, rc):
    client.subscribe("local/alert")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        now=time.strftime("%Y-%m-%d %H:%M")
        print("Unexpected disconnection."+now)

client = mqtt.Client(client_id="alertByTelegram")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("localhost", 1883, 60)

client.loop_forever()
