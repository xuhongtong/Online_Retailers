# -*- coding: utf-8 -*-
from datetime import datetime

__author__ = 'zhougy'
__date__ = '2018/12/19 上午9:59'

'''
自定义orm业务模型类
'''

from db.mysql_helper import Base, MySQLORMHelper
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Float



# #############定义京东数据库模型 start ######################

# 一级菜单
class JdFirstCate(Base):
    __tablename__ = 'Jd_FirstCate'
    # id = Column(Integer, primary_key=True)
    first_cate_id = Column(Integer, primary_key=True)
    first_cate_name = Column(String(100))
    # first_url=Column(String(200))


# 二级菜单
class JdSecondCate(Base):
    __tablename__ = 'Jd_SecondCate'
    # id = Column(Integer, primary_key=True)
    second_cate_id = Column(Integer, primary_key=True)
    second_cate_name = Column(String(100))
    first_cate_id = Column(Integer)
    # second_url = Column(String(200))


# 三级菜单
class JdThirdCate(Base):
    __tablename__ = 'Jd_ThirdCate'
    # id = Column(Integer, primary_key=True)
    third_cate_id = Column(Integer, primary_key=True)
    third_cate_name = Column(String(100))
    second_cate_id = Column(Integer)
    # third_url=Column(String(200))


# 品牌表
class JdBrand(Base):
    __tablename__ = 'jd_brand'
    brand_id=Column(Integer,primary_key=True)
    brand_name=Column(String(64))
    third_cate_id = Column(Integer)

# 详情表
class JdDetail(Base):
    __tablename__ = 'jd_shop'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    original_price = Column(Float(5, 2))
    promote_price = Column(Float(5, 2))
    img_url = Column(String(200))
    month_sales = Column(Integer)
    total_sales = Column(Integer)
    stock=Column(Integer)
    total_evaluates = Column(Integer)
    third_cate_id = Column(Integer)
    create_time= Column(DateTime,default=datetime.now())
    brand_name=Column(String(100))

def synchronous():
    minst = MySQLORMHelper()
    session = minst.create_session()
    print(session)


if __name__ == "__main__":
    synchronous()
