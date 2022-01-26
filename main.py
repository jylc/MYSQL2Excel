# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymysql
from pymysql import cursors
from loguru import logger
import items
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Convert:
    def __init__(self, school_url):
        self.connection = None
        self.school_url = school_url

    def query_item(self, query_item, cursor):
        sql = "SELECT  `s2.school_name`,`p.school_url`,    `p.related_title`,    `p.brief_introduction`,   " \
              "` p.related_url`,    `p.release_time`" \
              " FROM (SELECT `s.school_name`,`s.school_url` FROM `school_entities` AS `s` GROUP BY `s.school_url`)" \
              " AS `s2` AND `party_info_entities` AS `p` " \
              "WHERE `s2.school_url`=`p.school_url`"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) != 0:
                return True, results
            else:
                return False, None
        except:
            logger.error('cannot select {}', query_item)
            return False, None

    def _is_connected(self):
        try:
            self.connection.ping(reconnect=True)
            logger.info("database is connecting")
        except:
            self.connection = self._to_connect()
            logger.info("database is reconnecting")

    def _to_connect(self):
        return pymysql.connect(host='10.16.77.184',
                               user='root',
                               password='Password123@mysql',
                               database='partyhistoryspider')

    # mysql数据转换为excel数据
    def convertToExcel(self):
        logger.info('start convert')
        self._is_connected()
        with self.connection:
            with self.connection.cursor() as cursor:
                ok, results = self.query_item(self.school_url, cursor)
                if ok:
                    for result in results:
                        logger.info("{}".format(result))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    toExcel = Convert('pku.edu.cn')
    toExcel.convertToExcel()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
