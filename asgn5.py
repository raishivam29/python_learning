class Board():
    board='cbse'

    def stud_name(self,name):
        self.nam=name 
    def stud_board(self,boar):
        self.board=boar
    def stud_info(self):
        print('student name :'+self.nam)
        print('student board :'+self.board)
S1=Board()
S2=Board()
S3=Board()
S4=Board()
S5=Board()
S6=Board()

S1.stud_name('diwakar')
S2.stud_name('shivam')
S3.stud_name('shubham')
S4.stud_name('tanmay')
S5.stud_name('shrikant')
S6.stud_name('gopal')

S2.stud_board('BIHAR')
S4.stud_board('ISCE')
S6.stud_board('UP')

S1.stud_info()
S2.stud_info()
S3.stud_info()
S4.stud_info()
S5.stud_info()
S6.stud_info()
