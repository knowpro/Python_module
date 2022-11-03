class StringForMe:
    
    def __init__(self, stg):  # Args Constructor
        self.stg = stg
        
    def rev_in_print(self):
        lst = self.stg.split(sep="_")
        lst = lst[::-1]
        return " ".join(lst)
    
s1 = StringForMe("I_Love_my Bindiya")
print(s1.rev_in_print())