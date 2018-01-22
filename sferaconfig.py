from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.sfera

def getConfig(key, defaultValue):
    result = db.config.find_one({"key": key})
    if result == None:
        return defaultValue
    else:
        return result["value"]

def addDefaultConfig():
    # default = [
    #     {
    #         "key": "alert_by_telegram",
    #         "value": {
    #             "bot_api_key": "XXXX",
    #             "chat_id": 123456
    #         }
    #     }
    # ]
    # for doc in default:
    #     db.config.update_one({"key": doc["key"]}, {"$set": doc}, upsert=True)
    pass
