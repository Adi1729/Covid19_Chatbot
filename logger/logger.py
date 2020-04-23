from datetime import datetime
import pymongo

class Log:
    def __init__(self):
        pass

    def write_log(self, sessionID, log_message):
        self.file_object = open("conversationLogs/"+sessionID+".txt", 'a+')
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        self.file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message + "\n")
        self.file_object.close()

    def write_mongodb(self, sessionID, log_message):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['chatbot_log']
        self.collection = self.db['conversation_logs']
        self.comment = {"sessionID" : sessionID,
                        "time_stamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "message" : log_message
                        }
        self.collection.insert(self.comment)


