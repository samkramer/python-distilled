# 7.12 Class Variables and Methods
from xml.etree.ElementTree import XML

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    # factory method
    @classmethod
    def from_xml(cls, data):
        doc = XML(data)
        return cls(doc.findtext('owner'), float(doc.findtext('amount')))
    
    def __repr__(self):
        return f'{type(self).__name__}({self.owner!r}, {self.balance!r})'
    
if __name__ == '__main__':  
    data = '''
    <account>
        <owner>Guido</owner>
        <amount>1000.00</amount>
    </account>
    '''
    
    a = Account.from_xml(data)
    print(str(a))