#coding:utf-8
phone_info = [{'name':'vivoX9','money':2799,'count':1},{'name':'iphone7(32G)','money':4888,'count':31},{'name':'iphone7(128G)','money':5668,'count':22},{'name':'iphone7P(128G)','money':6616,'count':29}]
    
# 查看所有手机品牌
def selecte_all_phone(is_detail):
    # 遍历列表
    for x in range(len(phone_info)):
        ph_dict = phone_info[x]
        # 判断is_detail值为Ture，则输出产品名称、价钱、库存
        if is_detail == True:
            print '%d：%s %d %d '%(x+1,ph_dict['name'],ph_dict['money'],ph_dict['count'])
        else:
            print '%d：%s'%(x+1,ph_dict['name'])
# 判断选择数字是否符合标准
def selecte_number(mix_num,max_num,a):
    selecte_number = input('请根据序号选择：')
    if a == True:
        while selecte_number != mix_num and selecte_number != max_num:
            selecte_number = input('请选择正确的选项：')
    else:
        while selecte_number <mix_num or selecte_number > max_num:
            selecte_number = input('请选择正确的选项：')
    # 返回最终的结果
    return selecte_number
# ----------------------购买、查看函数-------------------
# 详情或返回
def detail_back():
    print '666.选择产品序号查看详情\n888.返回'
    # 选择1，
    if selecte_number(666,888,True) == 666:
        # 输入序号，查看详情
        input_count()
    else:
        return
# 输入序号，查看详情
def input_count():
    selecte_all_phone(False)
    phone_count = selecte_number(0,len(phone_info),False)
    # 根据序号取出手机详情字典
    phone_dict = phone_info[phone_count-1]

    print '%d:名称:%s 价格:%d 库存:%d' % (phone_count,phone_dict['name'],phone_dict['money'],phone_dict['count'])
    # 执行购买或者返回函数，传入对应手机字典
    buy_back(phone_dict)
# 购买或者返回
def buy_back(dict_p):
    print '1.购买\n2.返回'
    
    if selecte_number(1,2,True) == 1:
        # 取出库存量
        count = dict_p['count']
        # 库存量-1
        dict_p['count'] = count -1

        if  dict_p['count'] == 0:
            # 把字典从列表中移除
            phone_info.remove(dict_p)

        print '购买支付成功！'

    else:
        return
# ----------------------修改、添加函数-------------------
def update_add():
    print '1.添加新产品\n2.修改原有产品'
    if selecte_number(1,2,True) == 1:
        add_phone()
    else:
        update_phone()
# 添加新产品
def  add_phone():
    p_name = raw_input('请输入产品名称：')
    p_money = input('请输入产品价格：')
    p_count = input('请输入产品库存：')

    # 判断产品库存是否小于等于0
    while p_count <= 0:
        p_count = input('请输入正确的库存数：')

    # 组装手机信息字典
    p_dict = {'name':p_name,'money':p_money,'count':p_count}

    # 追加到所有手机信息列表中
    phone_info.append(p_dict)
# 修改原有产品
def update_phone():
    # 查看所有手机库存详情
    selecte_all_phone(True)
    print '1.根据序号修改\n2.返回'
    
    if selecte_number(1,2,True) == 1:
        up_num = input('请选择修改序号：')
        while up_num <1 or up_num > len(phone_info):
            up_num = input('请选择正确的序号：')

        p_name = raw_input('请输入修改后的名称：')
        p_money = input('请输入修改后的价格：')
        p_count = input('请输入修改后的库存量：')
        while p_count <=0:
            p_count = input('请输入争正确的库存量：')
        # 根据选择序号取出字典
        p_dict = phone_info[up_num-1]
        # 修改
        p_dict['name'] = p_name
        p_dict['money'] = p_money
        p_dict['count'] = p_count

    else:
        return
# ---------------------移除产品库存信息
def delete_phone():
    print '1.查看所有产品，根据序号移除\n2.移除所有产品\n3.返回'
    sele_num =selecte_number(1,3,False)

    if sele_num == 1:
        selecte_all_phone(True)

        ph_count = selecte_number(1,len(phone_info),False)

        del phone_info[ph_count-1]

    elif sele_num == 2:
        # 清空所有手机信息
        while len(phone_info):
            phone_info.pop()
    else:
        return
#  print 输出语句，可以在控制台打印输出文字信息
# input 接收python表达式
# raw_input 把输入的所有内容以字符串的方式接收
# 输出多个内容时，可以用逗号隔开
# \n 回车换行符
# bool 布尔类型  True(1)  False(0)
while True:
    print '1.查看所有手机品牌\n2.更改产品库存信息\n3.移除产品库存信息\n4.退出程序'
    sele_num = selecte_number(1,4,False)
    # 判断选择的选项
    if sele_num == 1:
        selecte_all_phone(False)
        detail_back()

    elif sele_num == 2:
        update_add()

    elif sele_num == 3:
        
        delete_phone()
    else:
        # 退出程序
        break