'''
Created by zhousp on 18-9-13
'''

from connect import session
from user_modules import User

__author__ = 'zhousp'


##增
def add_user():
    # person = User(username = 'xps',password='123')
    # session.add(person)  #增加一条数据
    session.add_all([  # 增加多条数据
        User(username='xpss', password='123'),
        User(username='xpss', password='123'),
        User(username='xpsss', password='123'),
    ])
    session.commit()  # 提交


##查
def search__user():
    rows = session.query(User).all()  ###查询所有
    # rows = session.query(User).first()  ###查询一条
    print(rows)  ##打印出的是内存地址,  重写__repr__之后就可以直接读了


##改
def update_user():
    rows = session.query(User).filter(User.username == 'xpss').update({User.password: 1})  ##字典
    session.commit()


##删除
def delete_user():
    rows = session.query(User).filter(User.username == 'xpss')[0]
    print(rows)
    session.delete(rows)  # 删除第一条记录
    # rows.deleted()   #批量删除
    session.commit()


def query_user():
    row = session.query(User).filter(User.username == 'xpss')
    for i in row:
        print(i)


if __name__ == "__main__":
    # add_user()
    # search__user()
    # update_user()
    # delete_user()
    query_user()
