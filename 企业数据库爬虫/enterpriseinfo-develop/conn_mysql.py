import pymysql
import time
def copyright(table):
##软件著作权
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_chanquan_copyright (entid,ent_uid,dengjiriq,ruanjianquanming,ruanjianjiancheng,dengjihao,fenleihao,banbenhao,zhuzuoquanren) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def copyrightworks(table):
##作品著作权
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_chanquan_copyrightworks (entid,ent_uid,zuopinming,dengjihao,leibie,wanchengriqi,dengjiriqi,faburiqi) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def icp(table):
##作品著作权
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_chanquan_icp (ent_uid,entid,icp_time,icp_name,icp_index,icp_url,icp_beian,icp_status,icp_danweix) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def patent(table):
##作品著作权
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_chanquan_patent (entid,ent_uid,shenqiri,zhuanliming,shenqinghao,shenqinggongbuhao,fenleihao) VALUES ( '%s', '%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def tmcount(table):
##商标信息
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_chanquan_tmcount (entid,ent_uid,zuopinming,dengjihao,leibie,wanchengriqi,dengjiriqi,faburiqi) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def abnormal(table):
##经营异常
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_abnormal (entid,ent_uid,lierutime,lieruyuanyin,juedingjiguan,yichutime,yichuyuanyin,yichujiguan) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def equity(table):
##股权出质
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_equity (entid,ent_uid,time,dengjibianhao,chuzhiren,zhiquanren,zhuangtai,caozuo) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def illegal(table):
##严重违法
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_illegal (entid,ent_uid,time,yuanyin,jiguan) VALUES ( '%s', '%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def judicialsale(table):
##司法拍卖
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_judicialsale (entid,ent_uid,paimaigonggao,paimaitime,zhixingfayuan,paimaibiaode) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def mortgage(table):
##动产抵押
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_mortgage (entid,ent_uid,dengjitime,dengjihao,beidanbaoleixing,beidanbaoshue,dengjijiguan,zhuangtai,caozuo) VALUES ( '%s', '%s','%s','%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def punish(table):
##行政处罚
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_punish (entid,ent_uid,juedingtime,juedingshuhao,type,juedingjiguan,caozuo) VALUES ( '%s', '%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def towntax(table):
##欠税公告
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jy_towntax (entid,ent_uid,fabutime,nashuihao,qianshuizhong,qianshuie,qianshuiyue,shuiwujiguan) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def bid(table):
##投标
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jytype_bid (entid,ent_uid,fabutime,biaoti,caigouren,content) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def certificate(table):
##资质证书
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jytype_certificate (entid,ent_uid,leixing,bianhao,fazhengriqi,jiezhiriqi) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def check(table):
##检查抽查
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jytype_check (entid,ent_uid,shijian,leixing,jieguo,jiguan) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def product(table):
##产品信息
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jytype_product (entid,entuid,tubiao,chanpinming,jianjie,fenlei,lingyu,caozuo) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def taxcredit(table):
##税务评级
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jytype_taxcredit (entid,ent_uid,nianfen,pingji,leixing,shibiehao,danwei) VALUES ( '%s', '%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def wechat(table):
##微信公众号
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_jytype_wechat (entid,ent_uid,tu,mingcheng,weixinhao,gongneng,url) VALUES ( '%s', '%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def announcementcourt(table):
##开庭公告
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_sifa_announcementcourt (entid,ent_uid,time,anyou,yuangao,beigao,caozuo) VALUES ( '%s', '%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def court(table):
##法院公告
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_sifa_court (entid,ent_uid,court_time,court_shang,court_bei,court_type,court_fayuan,court_text) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def dishonest(table):
    ##失信人
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标

    for i in table:
        sql = "INSERT INTO cmf_ent_sifa_dishonest (entid,ent_uid,mingcheng,fadingren,daihao,anhao,zhixingdanwei,yiwu,luxingqingkuang,zhixingfayuan,shengfen,lianshijian) VALUES ( '%s', '%s','%s','%s','%s','%s','%s', '%s','%s', '%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

def firmproduct(table):
##企业业务
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_bei_firmproduct (entid,ent_uid,tubiao,ming,leixing,beizhu) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def lawsuit(table):
        ##法律诉讼
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标

        for i in table:
            sql = "INSERT INTO cmf_ent_sifa_lawsuit (entid,ent_uid,lawsuit_time,lawsuit_caipan,lawsuit_anyou,lawsuit_anjian,lawsuit_anhao) VALUES ( '%s', '%s','%s','%s','%s','%s','%s')"
            try:
                cur.execute(sql % i)
                conn.commit()
            except:
                conn.rollback()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源

def zhixing(table):
#被执行人
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_sifa_zhixing (entid,ent_uid,lianriqi,zhixingbiaode,anhao,zhixingfayuan) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def teammember(table):
##公司团队
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_teammember (entid,ent_uid,ming,images,zhuwu,jianjie) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

def rongzi(table):
    # 时间 轮次 估值 金额 比例 投资方 新闻来源
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_bei_rongzi (entid,ent_uid, rongzi_time,rongzi_lunci,rongzi_guzhi,rongzi_jine,rongzi_bili,rongzi_touzifang,rongzi_laiyuan) VALUES ( '%s', '%s','%s','%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

def touzi(table):
    # 时间 轮次 金额 投资方 产品 地区 行业 业务
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标



    for i in table:
        sql = "INSERT INTO cmf_ent_bei_touzi (entid,ent_uid, touzi_time,touzi_lunci,touzi_jine,touzi_touzifang,touzi_chanpin,touzi_diqu,touzi_hangye,touzi_yewu) VALUES ( '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

def branch(table):
    # 名称 职位 公司名称  entuid
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标

    for i in table:
        sql = "INSERT INTO cmf_ent_bei_branch (entid,ent_uid, branch_name,branch_faren,branch_status,branch_time) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

def tminfo(table):
    # 名称 职位 公司名称  entuid
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标

    for i in table:
        sql = "INSERT INTO cmf_ent_knowledge (entid,ent_uid, k_time,k_logo,k_name,k_regno,k_type,k_liucheng) VALUES ( '%s', '%s','%s','%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

def staff(table):
    # 名称 职位 公司名称  entuid
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    for i in table:
        sql = "INSERT INTO cmf_ent_bei_staff (entid,ent_uid, staff_jibie, staff_name) VALUES ( '%s', '%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源

#
def change(table):
    # 名称 职位 公司名称  entuid
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标

    for i in table:
        sql = "INSERT INTO cmf_ent_bei_change (entid,ent_uid, change_time, change_type,change_sinfo,change_einfo) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def holder(table):
    # 并没有插入股东总量，出资从总额，认缴出资币种，直接从表格上爬取内容入库而已
    #  id ent_uid 股东名称 出资比例 认缴出资额
    pass
    #  conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    #  cur = conn.cursor()  # 获取一个游标
    # # data = list(map(tuple, table))
    #
    #
    #  for i in table:
    #
    #      a=i[2]
    #      a=a.split("\n")[0]
    #
    #      i = list(i)
    #
    #      #i=np.array(i)
    #      i[2]=a
    #      i=tuple(i)
    #
    #      sql = "INSERT INTO cmf_ent_bei_holder (entid,ent_uid, shaName, fundeRatio, subConam)" \
    #         "VALUES ( '%s' ,'%s','%s','%s','%s')"
    #
    #      try:
    #          cur.execute(sql % i)
    #          conn.commit()
    #      except:
    #          conn.rollback()
    #  cur.close()  # 关闭游标
    #  conn.close()  # 释放数据库资源
    # print("股东信息添加完成")

def invest(table):
    #  id ，ent_uid, 投资设立企业名称，法人，建立日期（姑且当做注册日期），出资金额，企业状态
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标

    for i in table:
        a = i[3]
        a = a.split("\n")[0]

        i = list(i)

        # i=np.array(i)
        i[3] = a
        i = tuple(i)
        sql = "INSERT INTO cmf_ent_bei_invest (entid,ent_uid, invest_company, invest_daibiao, invest_ziben, invest_edu,invest_bili,invest_time,invest_status)" \
            " VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s' )"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()

    cur.close()  # 关闭游标
    conn.close()


def base(table):
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    # 获取一个游标
    cur = conn.cursor()

    # 查询记录是否存在，如果存在，则修改记录，如果不存在，则插入新的记录
    query_sql = "SELECT id FROM cmf_ent_basic where ent_uid='%s'"
    try:
        effect_row = cur.execute(query_sql % table[0])
        if effect_row > 0:
            # 获取剩余结果的第一行数据
            row_1 = cur.fetchone()
            ent_id = row_1[0]
            # 执行更新的语句, 从2开始
            # sql = "UPDATE cmf_ent_basic SET entphone='%s',entemail='%s', ent_url='%s', ent_address='%s'," \
            #       "ent_time='%s',ent_ziben='%s',ent_status='%s', ent_desc='%s', ent_reg_no='%s',ent_org='%s'," \
            #       "tax_person_code='%s',ent_type='%s',tax_code='%s', ent_hangye='%s', entDeadline='%s'," \
            #       "hetime='%s',credit_code='%s', ent_english_name='%s',ent_reg_address='%s', ent_range='%s'," \
            #       "ent_faren='%s',update_time='%s'" \
            #       " WHERE id='%s'"
            # cur.execute(sql % (table[2], table[3], table[4], table[5], table[6], table[7], table[8], table[9], table[10],
            #                    table[11],table[12], table[13], table[14], table[15], table[16], table[17], table[18],
            #                    table[19], table[20],table[21], table[22], table[23], ent_id))
            sql = "UPDATE cmf_ent_basic SET entphone='1234567890' WHERE id=200"
            cur.execute(sql)
            # cur.execute(sql % (table[2], ent_id))
        else:
            # 执行插入的语句
            sql = "INSERT INTO cmf_ent_basic (ent_uid, ent_name,entPhone,entEmail, ent_url, ent_address,ent_time,ent_ziben,ent_status, ent_desc," \
                  " ent_reg_no,ent_org,tax_person_code,ent_type,tax_code, ent_hangye, entDeadline,hetime,credit_code, ent_english_name,ent_reg_address, ent_range ,ent_faren,create_time" \
                  ") VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s' )"
            cur.execute(sql % table)
        conn.commit()
        # 判断是否有记录
        # 执行SQL，并返回收影响行数
        # effect_row = cursor.execute("select * from tb7")

    except:
        conn.rollback()
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源

    # sql = "INSERT INTO cmf_ent_basic (ent_uid, ent_name,entPhone,entEmail, ent_url, ent_address,ent_time,ent_ziben,ent_status, ent_desc," \
    #     " ent_reg_no,ent_org,tax_person_code,ent_type,tax_code, ent_hangye, entDeadline,hetime,credit_code, ent_english_name,ent_reg_address, ent_range ,ent_faren,create_time" \
    #     ") VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s' )"

    # print(sql)
    # sql = "UPDATE cmf_ent_basic SET ent_uid='%s', ent_name='%s',entphone='%s',entemail='%s', ent_url='%s', ent_address='%s',ent_time='%s',ent_ziben='%s',ent_status='%s', ent_desc='%s'," \
    #       " ent_reg_no='%s',ent_org='%s',tax_person_code='%s',ent_type='%s',tax_code='%s', ent_hangye='%s', entDeadline='%s',hetime='%s',credit_code='%s', ent_english_name='%s',ent_reg_address='%s', ent_range='%s' ,ent_faren='%s',create_time='%s'" \
    #       " WHERE id ='%s'"


    # try:
    #     cur.execute(sql % table)
    #     conn.commit()
    # except:
    #     conn.rollback()
    #     cur.close()  # 关闭游标
    #     conn.close()  # 释放数据库资源


def hangye(table):

    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "SELECT * FROM cmf_hangye where  hangye=%s"
    selectRowNums=cur.execute(sql,table)

    if selectRowNums==0:
        sql1="INSERT INTO cmf_hangye (hangye) value ('%s')";
        cur.execute(sql1 % table)
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
def jingpin(table):
    # 注意数据表设计的时候id是整数还是字符串，其他字段的字符串类型需要选择utf8
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标

    for i in table:
        sql = "INSERT INTO cmf_ent_bei_jingpin ( entid,ent_uid,chanpinimages,diqu,lunci,hangye,yewu,shijian,guzhi) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s' ,'%s' )"

        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源