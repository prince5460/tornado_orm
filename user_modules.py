'''
Created by zhousp on 18-9-13
'''

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from connect import Base

__author__ = 'zhousp'


#####我们用类来表示数据库里面的表！！！
class User(Base):
    __tablename__ = 'user'  ##表名字
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20))
    password = Column(String(50))
    creatime = Column(DateTime, default=datetime.now)
    _locked = Column(Boolean, default=False, nullable=False)

    def __repr__(self):  ##
        return """<User(id=%s,username=%s,password=%s,creatime=%s,_locked=%s)>

        """ % (
            self.id,
            self.username,
            self.password,
            self.creatime,
            self._locked
        )


##创建表
if __name__ == "__main__":
    Base.metadata.create_all()  ##去数据库里面创建所有的表
