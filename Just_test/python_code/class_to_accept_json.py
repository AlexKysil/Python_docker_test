class class_to_accept_json():
    list = None
    value = None
    username = None
    end = None

    def __init__(self,list, value, username, end):
        self.list = list
        self.value = value
        self.username = username
        self.end = end

    def print_parametrs(self):
        print(" list: %s \n value: %s, \n username: %s, \n end: %s" %(self.list, self.value, self.username, self.end))

    def say(self):
        print('\n hello')
