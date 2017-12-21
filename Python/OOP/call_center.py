from datetime import datetime
class Call(object):
    def __init__(self, id, name, phone_number,reason_call):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time_call = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.reason_call = reason_call
    def display(self):
        print "Caller ID: " + str(self.id)
        print "Caller Name: "+self.name
        print "Caller Phone Number: "+ str(self.phone_number)
        print "Call Time: "+ self.time_call
        print "Reason: "+self.reason_call+"\n"

class callCenter(object):
    def __init__(self, *call):
        self.call_list = []
        for num, element in enumerate(call):
            self.call_list.append({})
            self.call_list[num]["Caller ID"]= element.id
            self.call_list[num]["Caller Name"]= element.name
            self.call_list[num]["Caller Phone Number"]= element.phone_number
            self.call_list[num]["Caller Time"]= element.time_call
            self.call_list[num]["Calling reason"]= element.reason_call
        self.queue_size = len(call)
        print self.queue_size
    def add(self, name, phone_number, reason_call):
        add_id = len(self.call_list) + 1
        time_call = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_value = [add_id, name, phone_number,time_call, reason_call]
        key = ["Caller ID","Caller Name","Caller Phone Number","Caller Time","Calling reason"]
        add_dict = dict(zip(key,add_value))
        print add_dict
        self.call_list.append(add_dict)
    def remove(self):
        self.call_list.pop[0]
    def info(self):
        for element in self.call_list:
            print element['Caller Name'] + "\t"+ str(element['Caller Phone Number']) +"\t Total waits in line are " + str(len(self.call_list))


call_1 = Call(1,"Yang",3145417645,"inquiry")
call_1.display()
call_2 = Call(2,"Ran",3146083927,"No Reason")
call_2.display()
center_1 = callCenter(call_1,call_2)
center_1.info()
center_1.add("Mickey",11111111,"fun")
center_1.info()
