# -*- coding:utf-8 -*-

# from db.models import JdDetail
from db.models import JdFirstCate, JdSecondCate, JdThirdCate, JdDetail, JdBrand
from db.mysql_helper import MySQLORMHelper

__author__ = 'xht'
__date__ = '2018/12/25 19:13'

minst = MySQLORMHelper()
session = minst.create_session()


# 京东
class JdPipeline(object):
    def process_item(self, item, spider):
        try:
            item_name = item.get_name()
            spider_name = spider.name

            # 添加一级菜单表
            if item_name == 'JdFirstCateItem' and spider_name == 'jd1':
                jd1 = JdFirstCate(
                    first_cate_id=item.get('first_cate_id'),
                    first_cate_name=item.get('first_cate_name'),
                    # first_url=item.get('first_url'),
                )
                minst.add_records(session, jd1)
                # 添加二级菜单表
            elif item_name == 'JdSecondCateItem' and spider_name == 'jd1':
                jd2 = JdSecondCate(
                    second_cate_id=item.get('second_cate_id'),
                    second_cate_name=item.get('second_cate_name'),
                    first_cate_id=item.get('first_cate_id')
                    # detail_fingerprint1 = item.get('detail_fingerprint1'),
                )
                minst.add_records(session, jd2)
                # 添加三级菜单表
            elif item_name == 'JdThirdCateItem' and spider_name == 'jd1':
                jd3 = JdThirdCate(
                    third_cate_id=item.get('third_cate_id'),
                    third_cate_name=item.get('third_cate_name'),
                    second_cate_id=item.get('second_cate_id'),
                    # detail_fingerprint1 = item.get('detail_fingerprint1'),
                )
                minst.add_records(session, jd3)
                # 添加详情表
            elif item_name == 'JdDetailItem' and spider_name == 'jd':
                jd4 = JdDetail(title=item.get('title'),
                               original_price=item.get('original_price'),
                               promote_price=item.get('promote_price'),
                               img_url=item.get('img_url'),
                               month_sales=item.get('month_sales'),
                               total_sales=item.get('total_sales'),
                               stock=item.get('stock'),
                               total_evaluates=item.get('total_evaluates'),
                               third_cate_id=item.get('third_cate_id'),
                               brand_name=item.get('brand_name')
                               )
                minst.add_records(session, jd4)
            # 添加品牌表
            elif item_name == 'JdBrandItem' and spider_name == 'jd':
                jd5 = JdBrand(
                    brand_name=item.get('brand_name'),
                    third_cate_id=item.get('third_cate_id'),
                )
                minst.add_records(session, jd5)
        except Exception as e:
            print(f"MySQLJDPipeLine:process_item has error: {e}")
        finally:
            return item
