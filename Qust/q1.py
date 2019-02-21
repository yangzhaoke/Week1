phone=input('请输入手机号:')
str=['136','150','176','137','152','123']
try:
    int(phone)
    if phone[:3] in str:
        if len(phone)==11:
            print("1")
        else:
            print('0')
except:
        print('必须数字')


