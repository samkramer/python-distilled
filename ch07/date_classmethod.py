# 7.12 Class Variables and Methods
import time

class Date:
    # class variable that adjusts output from __str__()
    datefmt = '{year}-{month:02d}-{day:02d}'
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return self.datefmt.format(year=self.year,
                                   month=self.month,
                                   day=self.day)
    
    # factory method
    @classmethod
    def from_timestamp(cls, ts):
        tm = time.localtime(ts)
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
    @classmethod
    def today(cls):
        return cls.from_timestamp(time.time())
    
class MDYDate(Date):
    datefmt = '{month}/{day}/{year}'
    
class DMYDate(Date):
    datefmt = '{day}/{month}/{year}'
    

if __name__ == '__main__':  
    a = Date(1967, 4, 9)
    print(a)    # 1967-04-09
    
    b = MDYDate(1967, 4, 9)
    print(b)    # 4/9/1967
    
    c = DMYDate(1967, 4, 9)
    print(c)    # 9/4/1967
    
    bt = MDYDate.today()
    print(bt)
    
    ct = DMYDate.today()
    print(ct)