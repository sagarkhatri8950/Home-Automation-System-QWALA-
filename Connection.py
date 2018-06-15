import pymysql

class Config:
    
    def __init__(self):
        self.db=pymysql.connect("localhost","root","123","qwala")
        self.cursor=self.db.cursor()

#connectionObj=Connection()  #use to initialise the constructor
#cursor=connectionObj.cursor # put this when you want to use the cursor in your code 
#connectionObj.close()   #put this when you want to close the database connecion
#del connectionObj    #delete the constructor

