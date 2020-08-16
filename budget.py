import math
class Category:
    def __init__(self, z):
        self.catname = z
        self.ledger = list()
        self.rem = 0.00
        self.withdrawals = 0.00
        
    def deposit(self,a,d=''):
        self.ledger.append({"amount": float(a), "description":d})
        self.rem += float(a)

    def withdraw(self,a,d=''):
        if self.check_funds(a):
            self.ledger.append({'amount': float(-1*a), 'description': d})
            self.rem -= float(a)
            self.withdrawals += float(a)
            return True
        return False

    def get_balance(self):
        return self.rem

    def transfer(self,a,b):
        if self.check_funds(a):
            b.deposit(a,'Transfer from '+self.catname)
            self.withdraw(a,'Transfer to '+b.catname)
            return True
        else :
            return False

    def check_funds(self,a):
        if(self.rem<float(a)):
            return False
        else:
            return True

    def __str__(self):
        op = []
        for i in range(math.floor((30-len(self.catname))/2)):
            op.append('*')
        op.append(self.catname)
        for i in range(30-len(self.catname)-math.floor((30-len(self.catname))/2)):
            op.append('*')
        
        op.append('\n')
        for i in range(len(self.ledger)):
            op += list(self.ledger[i]['description'])[:23]
            if(len(self.ledger[i]['description'])<23):
                for j in range(23-len(self.ledger[i]['description'])):
                    op.append(' ')
            if(len(str("{:.2f}".format(self.ledger[i]['amount'])))<7):
                for j in range(7-len(str("{:.2f}".format(self.ledger[i]['amount'])))):
                    op.append(' ')
            op += list("{:.2f}".format(self.ledger[i]['amount']))[:7]
            op.append('\n')
        op.append('Total: '+str(self.rem))
        op = ''.join(op)
        return op

def create_spend_chart(categories):
    total = 0.00
    percentages = []
    answer = ['Percentage spent by category\n']
    for i in range(len(categories)):
        total += categories[i].withdrawals
    for i in range(len(categories)):
        percentages.append(math.floor(categories[i].withdrawals*10/total)*10)
    for i in (range(11)):
        for j in range(3-len(str((10-i)*10))):
            answer.append(' ')
        answer += [str((10-i)*10),'|',' ']
        for j in range(len(percentages)):
            if (10-i)*10 <= percentages[j]:
                answer.append('o')
            else:
                answer.append(' ')
            answer += [' ',' ']
        answer.append('\n')
    answer += [' ',' ',' ',' ','-']
    for i in range(len(categories)*3):
        answer.append('-')
    answer.append('\n')
    maxlen = 0
    for i in range(len(categories)):
        if (maxlen<len(categories[i].catname)):
            maxlen = len(categories[i].catname)
    
    for i in range(maxlen):
        answer+= [' ',' ',' ',' ',' ']
        for j in range(len(categories)):
            if (len(categories[j].catname)>i):
                answer.append(categories[j].catname[i])
            else:
                answer.append(' ')
            answer += [' ',' ']
        answer.append('\n')

    answer.pop()
    return ''.join(answer)
#def create_spend_chart(categories):