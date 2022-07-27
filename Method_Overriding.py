class ineuron:
    def student(self):
        print("Print the details of all the students")
    def achievers(self):
        print("Print the list of all the achievers")
    def hall_of_fame(self):
        print("Print everyone from hall of fame")

class inueron_vision(ineuron):
    def student(self):
        print("These are the filtered students list")

iv=inueron_vision()
iv.student() #this method will be overridden