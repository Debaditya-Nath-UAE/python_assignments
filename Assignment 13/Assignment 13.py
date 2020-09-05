'''
Problem Steps:Take Telephone company as a scenario:
Do the following stuff:
1) Get function to display person details such as name mobile number and balance
2) Create function for calling and monitor currency balance and call status left in is number
3) If balance is over and call is in call then display saying you don't have suffient balance to call please reacharge your number and try again to call
4) After function create function to cut the call
'''
class person:
    def __init__(self,name,money,status):
        self.name=name
        self.money=money
        self.status=status
person1=person('Indra','in call')
person2=person('Maya',0,'offline')
person3=person('')