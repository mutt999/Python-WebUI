import json
import os.path

class IEventService:

    def __init__(self):
        self.data_file ='events.json'
        self.last_id = 0
        self.value = [
            {"id": 1, "name": "C++ Kurs", "participantCount": 1},
            {"id": 3, "name": "Java Kurs", "participantCount": 10},
            {"id": 5, "name": "C# Kurs", "participantCount": 20},
        ]
        self.Read()
        if len(self.value):
            item = max(self.value, key=lambda x: x.get('id'))
            self.last_id = item.get('id')
            self.last_id = self.last_id + 1

    def Read(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.value = json.load(f)

    def Write(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.value,indent=2))

    def AddEvent(self, name, count):
        self.value.append(
            {"id": self.last_id, "name": name, "participantCount": count}
        )
        self.last_id = self.last_id + 1
        self.Write()
        return self.value

    def RemoveEvent(self, id):
        self.value = [item for item in self.value if item.get("id") != id]
        self.Write()
        return self.value

    def UpdateEvent(self, event):
        found = next((item for item in self.value if item.get("id") == event.get("id")),None)
        if found:
            found['name']=event.get('name')
            found['participantCount']=event.get('participantCount')
            self.Write()   
        return self.value     

    def GetEvents(self, month):
        return self.value
