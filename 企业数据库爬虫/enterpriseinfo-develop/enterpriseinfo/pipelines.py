# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
import conn_mysql


class EnterpriseinfoPipeline(object):
    def __init__(self):
        pass
        # self.connect = pymysql.connect(
        #     user="root",
        #     password="root",
        #     port=3306,
        #     host="127.0.0.1",
        #     db="luhao35",
        #     charset="utf8"
        # )

    def process_item(self, item, spider):
        title = item['op_type']
        # if title == 'baseInfo':
        #     self.base(item)
        #     # pass
        # elif title == 'staff':
        #     self.staff(item['staff_info'])
        # elif title == 'holder':
        #     self.holder(item['holder_info'])
        # elif title == 'invest':
        #     self.invest(item['invest_info'])
        # elif title == 'changeinfo':
        #     self.change_info(item['changeinfo'])
        # elif title == 'branch':
        #     self.branch_info(item['branch_info'])
        # elif title == 'rongzi':
        #     self.rongzi_info(item['rongzi_info'])
        # elif title == 'teamMember':
        #     self.team_member_info(item['team_member_info'])
        # elif title == 'firmProduct':
        #     self.firm_product_info(item['firm_product_info'])
        # elif title == 'lawsuit':
        #     self.law_suit_info(item['lawsuit_info'])
        # elif title == 'taxcredit':
        #     print(title)
        #
        #     self.taxcredit_info(item['taxcredit_info'])
        # elif title == 'punish':
        #     print(title)
        #
        #     self.punish_info(item['punish_info'])
        # elif title == 'equity':
        #     print(title)
        #     self.equity_info(item['equity_info'])
        return item

    def base(self, item):
        cur = self.connect.cursor()  # 获取游标
        # 查询记录是否存在，如果存在，则修改记录，如果不存在，则插入新的记录
        # query_sql = "SELECT id FROM cmf_ent_basic where ent_uid='%s'"
        # 旧表
        # query_sql = "SELECT id FROM cmf_qiye where id='%s'"
        query_sql = "SELECT id FROM cmf_ent_basic where qiye_id='%s'"
        try:
            # 创建或更新时间
            create_or_update_time = time.strftime("%Y-%m-%d")

            # create_or_update_time = time.strftime("%Y-%m-%d %H:%M:%S")
            # effect_row = cur.execute(query_sql % item['ent_uid'])
            effect_row = cur.execute(query_sql % item['qiye_id'])
            if effect_row > 0:
                # 获取剩余结果的第一行数据
                row_1 = cur.fetchone()
                ent_id = row_1[0]
                sql = "UPDATE cmf_ent_basic SET entphone='%s',entemail='%s', ent_url='%s', ent_address='%s'," \
                      "ent_time='%s',ent_ziben='%s',ent_status='%s', ent_desc='%s', ent_reg_no='%s',ent_org='%s'," \
                      "unified_social_credit_code='%s',ent_type='%s',tax_code='%s', ent_hangye='%s', entDeadline='%s'," \
                      "hetime='%s', ent_english_name='%s',ent_reg_address='%s', ent_scope_of_business='%s'," \
                      "ent_faren='%s', qiye_id='%s', reg_org='%s', update_time='%s'," \
                      "legal_person_supplement_top='%s', legal_person_supplement_bottom='%s'" \
                      " WHERE id='%s'"
                cur.execute(sql % (item['tel'], item['email'], item['web'], item['address'], item['reg_time'],
                                   item['reg_ziben'], item['status'], item['summary'], item['business_reg_code'],
                                   item['org_code'], item['unified_social_credit_code'], item['ent_type'],
                                   item['tax_code'], item['industry'], item['deadline'], item['checkdate'],
                                   item['english_name'], item['reg_address'], item['scope_of_business'],
                                   item['legal_person'], item['qiye_id'], item['reg_org'], create_or_update_time,
                                   item['ent_faren_supplement_top'], item['ent_faren_supplement_bottom'], ent_id))
            else:
                # 执行插入的语句
                sql = "INSERT INTO cmf_ent_basic (ent_uid, qiye_id, ent_name, entPhone, entEmail, ent_url, ent_address," \
                       "ent_time, ent_ziben, ent_status, ent_desc, ent_reg_no," \
                       "ent_org, ent_type, tax_code, ent_hangye,reg_org," \
                       "entDeadline, hetime, unified_social_credit_code, ent_english_name," \
                       "ent_reg_address, ent_scope_of_business, ent_faren, create_time, update_time," \
                       "legal_person_supplement_top, legal_person_supplement_bottom) " \
                       "VALUES ('%s','%s','%s','%s','%s','%s','%s'," \
                       "'%s','%s','%s','%s','%s'," \
                       "'%s','%s','%s','%s','%s'," \
                       "'%s','%s','%s','%s'," \
                       "'%s','%s','%s','%s','%s'," \
                       "'%s', '%s')"
                cur.execute(sql % (item['ent_uid'], item['qiye_id'], item['name'], item['tel'], item['email'], item['web'], item['address'],
                                          item['reg_time'], item['reg_ziben'], item['status'], item['summary'], item['business_reg_code'],
                                          item['org_code'], item['ent_type'], item['tax_code'], item['industry'], item['reg_org'],
                                          item['deadline'], item['checkdate'], item['unified_social_credit_code'], item['english_name'],
                                          item['reg_address'], item['scope_of_business'], item['legal_person'], create_or_update_time, create_or_update_time,
                                          item['ent_faren_supplement_top'], item['ent_faren_supplement_bottom']
                                      ))

        except:
            pass

    def staff(self, table):
        """
        插入公司主要人员的信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            staff_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_staff where staff_md5='%s'"
            effect_row = cur.execute(query_sql % staff_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_staff (staff_md5, ent_uid, staff_name, staff_jibie ) " \
                             "VALUES ( '%s', '%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def holder(self, table):
        """
        @todo 后续添加
        插入公司主要人员的信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            holder_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_holder where holder_md5='%s'"
            effect_row = cur.execute(query_sql % holder_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_holder (holder_md5, ent_uid, shaname, funderatio, subconam) " \
                             "VALUES ( '%s', '%s','%s','%s', '%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def invest(self, table):
        """
        添加对外投资信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标

        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            staff_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_invest where invest_md5='%s'"
            effect_row = cur.execute(query_sql % staff_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_invest (invest_md5, ent_uid, invest_company, invest_daibiao, invest_ziben," \
                             " invest_edu, invest_bili, invest_time, invest_status ) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def change_info(self, table):
        """
        插入变更信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            change_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_change where change_md5='%s'"
            effect_row = cur.execute(query_sql % change_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_change (change_md5, ent_uid, change_time, change_type, change_sinfo," \
                             " change_einfo ) VALUES ( '%s', '%s', '%s','%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def branch_info(self, table):
        """
        插入分支机构信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            branch_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_branch where branch_md5='%s'"
            effect_row = cur.execute(query_sql % branch_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_branch (branch_md5, ent_uid, branch_name, branch_faren, branch_status," \
                             " branch_time ) VALUES ( '%s', '%s', '%s','%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass
        pass


    def rongzi_info(self, table):
        """
        插入变更信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            rongzi_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_rongzi where rongzi_md5='%s'"
            effect_row = cur.execute(query_sql % rongzi_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_change (rongzi_md5, ent_uid, rongzi_time, rongzi_lunci, rongzi_guzhi," \
                             " rongzi_jine, rongzi_bili, rongzi_tousifang, rongzi_laiyuan ) " \
                             "VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def team_member_info(self, table):
        """
        插入变更信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            product_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_firmproduct where product_md5='%s'"
            effect_row = cur.execute(query_sql % product_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_firmproduct (product_md5, entid, beizhu) " \
                             "VALUES ( '%s', '%s', '%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def firm_product_info(self, table):
        """
        插入变更信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            team_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_teammember where team_md5='%s'"
            effect_row = cur.execute(query_sql % team_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_teammember (team_md5, entid, member_name, title, jianjie) " \
                             "VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def touzi_info(self, table):
        """
        插入变更信息
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            touzi_md5 = i[0]
            query_sql = "select id from cmf_ent_bei_touzi where touzi_md5='%s'"
            effect_row = cur.execute(query_sql % touzi_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_ent_bei_touzi (touzi_md5, entid, touzi_time, touzi_lunci, touzi_jine," \
                             " touzi_touzifang, touzi_chanpin, touzi_diqu, touzi_hangye, touzi_yewu) " \
                             "VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                except:
                    pass

    def law_suit_info(self, table):
        """
        法律诉讼，对应的是信用信息中的司法信息
        @todo 需要完善
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            justice_info_md5 = i[0]
            query_sql = "select id from cmf_justice_info where justice_info_md5='%s'"
            effect_row = cur.execute(query_sql % justice_info_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_justice_info (justice_info_md5, ent_uid, case_date, judgement, case_reason," \
                             " case_status, case_num, ent_id) " \
                             "VALUES ( '%s', '%s', '%s','%s','%s','%s','%s', '%s')"
                try:
                    cur.execute(insert_sql % i)
                    # 提交
                    self.connect.commit()
                except:
                    # 回滚
                    self.connect.rollback()
                    pass

    def taxcredit_info(self, table):
        """
        税务评级，对应的是信用信息中的税务信息
        @todo 需要完善
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            tax_info_md5 = i[0]
            query_sql = "select id from cmf_tax_info where tax_info_md5='%s'"
            effect_row = cur.execute(query_sql % tax_info_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_tax_info (tax_info_md5, ent_uid, year, tax_level, tax_type, tax_payer, audit_unit, ent_id) " \
                             "VALUES ( '%s', '%s', '%s', '%s','%s','%s','%s', '%s')"
                try:
                    cur.execute(insert_sql % i)
                    # 提交
                    self.connect.commit()
                except:
                    # 回滚
                    self.connect.rollback()
                    pass

    def punish_info(self, table):
        """
        行政处罚，对应的是信用信息中的行政处罚
        @todo 需要完善
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            penalty_md5 = i[0]
            query_sql = "select id from cmf_administrative_penalty where penalty_md5='%s'"
            effect_row = cur.execute(query_sql % penalty_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_administrative_penalty (penalty_md5, ent_uid, penalty_date, penalty_num, type, org, ent_id) "\
                             "VALUES ( '%s', '%s', '%s','%s','%s', '%s','%s')"
                print(insert_sql)
                try:
                    cur.execute(insert_sql % i)
                    # 提交
                    self.connect.commit()
                except:
                    # 回滚
                    self.connect.rollback()
                    pass

    def equity_info(self, table):
        """
        股权出质，对应的是信用信息中的股权质押
        @todo 需要完善
        :param table:
        :return:
        """
        cur = self.connect.cursor()  # 获取游标
        for i in table:
            # 查询对应的staff_md5是否存在,如果存在,则不插入,如果不存在,则插入
            stock_md5 = i[0]
            query_sql = "select id from cmf_stock_pledge where stock_md5='%s'"
            effect_row = cur.execute(query_sql % stock_md5)
            if effect_row == 0:
                insert_sql = "INSERT INTO cmf_stock_pledge (stock_md5, ent_uid, advice_date, reg_num, pledgor, pledgee, status, ent_id) " \
                             "VALUES ( '%s', '%s', '%s','%s','%s', '%s', '%s','%s')"
                try:
                    cur.execute(insert_sql % i)
                    # 提交
                    self.connect.commit()
                except:
                    # 回滚
                    self.connect.rollback()
                    pass

    def inser_sql(self, title, table):
        """
        @deprecated 已经废弃
        :param title:
        :param table:
        :return:
        """
        if title == 'baseInfo':
            conn_mysql.base(table)
        # elif title == 'staff':
        #     conn_mysql.staff(table)
        # elif title == 'lawsuit':
        #     conn_mysql.lawsuit(table)
        elif title == 'announcementcourt':
            conn_mysql.announcementcourt(table)
        elif title == 'bid':
            conn_mysql.bid(table)
        # elif title == 'rongzi':
        #     conn_mysql.rongzi(table)
        elif title == 'certificate':
            conn_mysql.certificate(table)
        elif title == 'copyright':
            conn_mysql.copyright(table)
        elif title == 'rongzi':
            conn_mysql.rongzi(table)
        elif title == 'branch':
            conn_mysql.branch(table)
        elif title == 'touzi':
            conn_mysql.touzi(table)
        elif title == 'holder':
            pass
            # conn_mysql.holder(table)
        # elif title == 'invest':
        #     conn_mysql.invest(table)
        elif title == 'jingpin':
            conn_mysql.jingpin(table)
        elif title=='hangye':
            conn_mysql.hangye(table)
        elif title=='changeinfo':
            conn_mysql.change(table)
        elif title=='tmInfo':
            conn_mysql.tminfo(table)
        elif title == 'court':
            conn_mysql.court(table)
        elif title == 'punish':
            conn_mysql.punish(table)
        elif title == 'equity':
            conn_mysql.equity(table)
        elif title == 'firmproduct':
            conn_mysql.firmproduct(table)
        elif title == 'teammember':
            conn_mysql.teammember(table)
        elif title == 'copyrightworks':
            conn_mysql.copyrightworks(table)
        elif title == 'icp':
            conn_mysql.icp(table)
        elif title == 'patent':
            conn_mysql.patent(table)
        elif title == 'tmcount':
            conn_mysql.tmcount(table)
        elif title == 'abnormal':
            conn_mysql.abnormal(table)
        # elif title == 'equity':
        #     conn_mysql.equity(table)
        elif title == 'illegal':
            conn_mysql.illegal(table)
        elif title == 'judicialsale':
            conn_mysql.judicialsale(table)
        elif title == 'mortgage':
            conn_mysql.mortgage(table)
        elif title == 'towntax':
            conn_mysql.towntax(table)
        elif title == 'check':
            conn_mysql.check(table)
        elif title == 'product':
            conn_mysql.product(table)
        # elif title == 'taxcredit':
        #     conn_mysql.taxcredit(table)
        elif title == 'taxcredit':
            conn_mysql.taxcredit(table)
        elif title == 'wechat':
            conn_mysql.wechat(table)
        elif title == 'dishonest':
            conn_mysql.dishonest(table)
        elif title == 'zhixing':
            conn_mysql.zhixing(table)
