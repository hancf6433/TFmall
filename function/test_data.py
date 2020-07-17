import os

# 获取订单券码
def get_code():
    '''获取订单券码'''
    filePath = os.path.dirname(__file__)
    data_path = os.path.dirname(filePath)
    data=os.path.join(data_path,'test data.txt')
    with open(data) as f:
        for i in f:
            s=i.split('：')
            if s[0]=='订单券码':
                code=s[1]
                break
    return code