class Friend():
    dest='goa'

    def frnd_name(self,nam):
         self.name=nam
    def frnd_dest(self,destin):
        self.dest=destin
    def frnd_tr(self):
        print('friend name        :'+self.name)
        print('friend destination :'+self.dest) 

S1=Friend()
S2=Friend()
S3=Friend()
S4=Friend()
S5=Friend()

S1.frnd_name('ram')
S2.frnd_name('shyam')
S3.frnd_name('sita')
S4.frnd_name('gita')
S5.frnd_name('rita')

S1.frnd_dest('shimla')
S2.frnd_dest('shimla')

S1.frnd_tr()
S2.frnd_tr()
S3.frnd_tr()
S4.frnd_tr()
S5.frnd_tr()







           
            