import pymysql
import time
def rongzi(table):
    # 时间 轮次 估值 金额 比例 投资方 新闻来源
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    print(table)


    for i in table:
        sql = "INSERT INTO cmf_ent_rongzi (entid,ent_uid, rongzi_time,rongzi_lunci,rongzi_guzhi,rongzi_jine,rongzi_bili,rongzi_touzifang,rongzi_laiyuan) VALUES ( '%s', '%s','%s','%s','%s','%s','%s','%s','%s')"
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
    print(table)


    for i in table:
        sql = "INSERT INTO cmf_ent_touzi (entid,ent_uid, touzi_time,touzi_lunci,touzi_jine,touzi_touzifang,touzi_chanpin,touzi_diqu,touzi_hangye,touzi_yewu) VALUES ( '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s')"
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
    print(table)
    for i in table:
        sql = "INSERT INTO cmf_ent_branch (entid,ent_uid, branch_name,branch_faren,branch_status,branch_time) VALUES ( '%s', '%s','%s','%s','%s','%s')"
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
    print(table)
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
    print(table)
    for i in table:
        sql = "INSERT INTO cmf_person (ent_uid, name, role,entName,entUid) VALUES ( '%s', '%s','%s','%s','%s')"
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
    print(table)
    for i in table:
        sql = "INSERT INTO cmf_ent_change (entid,ent_uid, change_time, change_type,change_sinfo,change_einfo) VALUES ( '%s', '%s','%s','%s','%s','%s')"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    print("变更信息添加完成")

def holder(table):
    # 并没有插入股东总量，出资从总额，认缴出资币种，直接从表格上爬取内容入库而已
    #  id ent_uid 股东名称 出资比例 认缴出资额
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
   # data = list(map(tuple, table))


    for i in table:

        a=i[2]
        a=a.split("\n")[0]

        i = list(i)

        #i=np.array(i)
        i[2]=a
        i=tuple(i)

        sql = "INSERT INTO cmf_ent_holder (entid,ent_uid, shaName, fundeRatio, subConam)" \
           "VALUES ( '%s' ,'%s','%s','%s','%s')"

        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    print("股东信息添加完成")

def invest(table):
    #  id ，ent_uid, 投资设立企业名称，法人，建立日期（姑且当做注册日期），出资金额，企业状态
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    print(table)

    for i in table:
        a = i[3]
        a = a.split("\n")[0]

        i = list(i)

        # i=np.array(i)
        i[3] = a
        i = tuple(i)
        sql = "INSERT INTO cmf_ent_invest (entid,ent_uid, invest_company, invest_daibiao, invest_ziben, invest_edu,invest_bili,invest_time,invest_status)" \
            " VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s' )"
        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()

    cur.close()  # 关闭游标
    conn.close()


def base(table):
    t = time.time()
    create_time =int(round(t * 1000))
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='luhao35', port=3306, charset='utf8')
    cur = conn.cursor()  # 获取一个游标
    sql = "INSERT INTO cmf_ent_basic (ent_uid, ent_name,entPhone,entEmail, ent_url, ent_address,ent_time,ent_ziben,ent_status, ent_desc," \
          " ent_reg_no,ent_org,tax_person_code,ent_type,tax_code, ent_hangye, entDeadline,hetime,credit_code, ent_english_name,ent_reg_address, ent_range ,create_time" \
          ") VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',create_time )"
    print(table)



    try:
        cur.execute(sql % table)
        conn.commit()
    except:
        conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
    print("工商信息添加完成")
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
    print(table)
    for i in table:
        sql = "INSERT INTO cmf_ent_competor ( idd,product, region, turn, industry, service, creat_time," \
            " estimate_value) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s','%s' )"

        try:
            cur.execute(sql % i)
            conn.commit()
        except:
            conn.rollback()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源