'''
Created by zhousp on 18-9-13
'''

#### ORM  对象关系映射  (只是一个概念)
### Python里面使用非常广的orm ： SQLAlchemy 连接数据库

# 导入模块
from sqlalchemy import create_engine

__author__ = 'zhousp'

# 数据库数据
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'Test'
USERNAME = 'root'
PASSWORD = '251120714'

##连接数据连接 URL
Db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    PORT,
    DATABASE,

)
## 连接数据库
engine = create_engine(Db_url)

##创建Moudle

## 表
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(engine)  ####基类

##增删改查
# 创建会话
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()  # 实例

##测试
if __name__ == "__main__":
    conection = engine.connect()
    result = conection.execute('select 1')
    print(result.fetchone())
