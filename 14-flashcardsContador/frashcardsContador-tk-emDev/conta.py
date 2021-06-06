
class Conta:
    def __init__(self):
        self.total = 0
        
    def somar(self, n):
        self.total += n
        
    def get_total(self):
        return self.total
    
    