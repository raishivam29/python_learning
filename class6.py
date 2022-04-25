class City():
    count='India'
    city='delhi'
    def pax_name(self,nam):
        self.name=nam
    def pax_city(self,cit):
        self.city=cit
    def pax_doc(self):
        print('pax name is    :'+self.name)
        print('pax city is    :'+self.city)
        print('pax country is :'+self.count)

S1=City()
S2=City()
S3=City()
S4=City()
S5=City()
S6=City()
S7=City()
S8=City()

S1.pax_name('SHIVAM')
S2.pax_name('RAJ')
S3.pax_name('AADARSH')
S4.pax_name('ABHIST')
S5.pax_name('AMBUJ')
S6.pax_name('MOHIT')
S7.pax_name('HARSH')
S8.pax_name('YASH')

S1.pax_city('BOMBAY')
S2.pax_city('VARANASI')
S3.pax_city('PATNA')

S1.pax_doc()
S2.pax_doc()
S3.pax_doc()
S4.pax_doc()
S5.pax_doc()
S6.pax_doc()
S7.pax_doc()
S8.pax_doc()    