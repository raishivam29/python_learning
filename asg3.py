class Student:
    sub='python'
    def store_name(self,nam):
        self.name=nam
    def store_subj(self,subje):
        self.sub=subje
    def store_display(self):
        print("student name :",str(self.store_name))
        print("student subj :",str(self.store_subj))


S1=Student()
S2=Student()
S3=Student()
S1.store_name('shivam')
S2.store_name('mayank')
S3.store_name('diwakar')
S2.store_subj('java')
S1.store_display()
S2.store_display()
S3.store_display()


        