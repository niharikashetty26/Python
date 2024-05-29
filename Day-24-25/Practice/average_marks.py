class Score:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_score(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("Hi," ,self.name, "your avg marks are: ",sum/3)
s1=Score("Niharika",[90,98,93])
s1.get_score()