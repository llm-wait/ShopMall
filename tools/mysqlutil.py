# -*- coding: utf-8 -*-
# @Time : 2021/9/22 14:27
# @Author : Corn
# @File : mysqlutil.py
import pymysql as pymysql
'''
对pymysql进行封装操作
'''
class DataBaseHandle:
    def __init__(self):
        '''
            实例方法共用的属性
            建立mysql的连接
        '''
        # 建立一个mysql的连接
        self.db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="study", port=3306)
        print(self.db)
    # 查询方法
    def selectDB(self,sql):
        '''
               sql语句就是正常的mysql的查询语句 原生的sql
               :param sql:
               :return:
               '''
        # 建立一个‘cursor游标’对象操作数据库
        cursor = self.db.cursor()
        # 写sql语句容易出现问题，所以用try...except...finally进行补获
        try:
            # 执行sql语句  用游标进行查询---返回结果---把结果保存在游标里面
            cursor.execute(sql)
            # 从游标里面读取数据，赋值给一个变量
            data=cursor.fetchall()
            return  data
        except Exception as e:
            raise e
        finally:
            # 把游标进行关闭
            cursor.close()

    # 新增方法
    def insertDB(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        try:
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            cursor.close()

    # 更新方法
    def updateDB(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        try:
            self.db.commit()
        except:
            self.db.rollback()
        finally:
            cursor.close()

    # 删除方法
    def deleteDB(self,sql):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            cursor.close()
    def closeDB(self):
        self.db.close()
if __name__ == '__main__':
    db =DataBaseHandle()
    selectsql = "select * from student;"
    data=db.selectDB(selectsql)
    insertsql='INSERT INTO student VALUES("125","测试121","男", "科学");'
    db.insertDB(insertsql)
    updatesql='UPDATE student SET name="测试九九九" WHERE id=123;'
    db.updateDB(updatesql)
    deletesql='delete from student where name="测试121";'
    db.deleteDB(deletesql)
    print(data)