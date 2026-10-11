# 1. 找到未加密的参数
    # :path: /weapi/comment/resource/comments/get?csrf_token= 代表
    # https://music.163.com/weapi/comment/resource/comments /get?csrf_token=是请求评论的
    # 两个重要参数params 加密后的参数  和encSecKey  解码钥匙？
    # 在选定的评论栈中直接搜索encSecKey直接定位至data加密位置
    # window.asrsea代表加密函数
    # bVC2x.encText 和 bVC2x.encSecKey 是加密函数返回的对象中的两个属性，分别包含了加密后的文本和密钥。
# 2. 想办法把参数模拟网易云逻辑进行加密，params， encSecKey
# 3. 请求网易云接口，获取评论
# 4. 解析数据，保存到本地
import requests, json
from Crypto.Cipher import AES
from base64 import b64encode



"""    function a(a = 16) { # 生成16位随机字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) # 循环16次，每次生成一个随机字符
            e = Math.random() * b.length,
            e = Math.floor(e),  #取整
            c += b.charAt(e);   #拼接字符
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)   // 使用CryptoJS库进行AES加密的相关代码// 定义加密密钥，使用UTF8编码解析变量b的值,b是key
          , d = CryptoJS.enc.Utf8.parse("0102030405060708") // 使用CryptoJS库进行AES加密的相关代码// 定义初始化向量(IV)，使用UTF8编码解析"0102030405060708"字符串
          , e = CryptoJS.enc.Utf8.parse(a) // 定义要加密的数据，使用UTF8编码解析变量a的值,a是data
          , f = CryptoJS.AES.encrypt(e, c, { // 使用AES加密算法进行加密，采用CBC模式// 参数说明：// 1. 要加密的数据(e)// 2. 加密密钥(c)// 3. 配置选项，包含初始化向量(IV)和加密模式(mode)
            iv: d, // 设置初始化向量
            mode: CryptoJS.mode.CBC // 使用CBC(密码块链接)模式
        });
        return f.toString()     // 返回加密后的结果转换为字符串
    }
    function c(a, b, c) {
        var d, e;   // 声明两个变量 d 和 e
        return setMaxDigits(131),   // 调用 setMaxDigits 函数设置最大数字位数为131
        d = new RSAKeyPair(b,"",c),     // 创建一个新的RSA密钥对，参数为b（公钥指数）、空字符串（私钥指数，这里为空）、c（模数）
        e = encryptedString(d, a)   // 使用创建的RSA密钥对对字符串a进行加密，并将结果赋值给变量e
    }
    function d(d, e, f, g) { d:数据data(JSON.stringify(i5n)),e:bss0x(["流泪", "强"])→ 010001
     ,f:bss0x(Af0x.md)→ 00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
     , g:bss0x(["爱心", "女孩", "惊恐", "大笑"])→ 0CoJUm6Qyw8W8jud
        var h = {} #空对象
          , i = a(16);  # 生成16位随机字符串
        return 
        h.encText = b(d, g),     # d是数据 g是密钥
        h.encText = b(h.encText, i),    # 两次加密,先加密data → encText     回推encText是data ，i是key
        h.encSecKey = c(i, e, f),       # RSA加密随机字符串 → encSecKey
        # e和f是定死的，i是随机数，想要破解，就把i定死为固定值，c就会变成固定值
        h
    }
"""
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
# 参数在function d 打一个断点就可以找到

data ={
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_3324117652",
    'threadId': "R_SO_4_3324117652"
}
# 找data的过程：先定位至encSecKey，在定位回声明的一个空列表中，列表值就是data，
# 先在声明空列表处打一个断点，再在加密处window.asrsea打一个断点，不断刷新断点内容，直到出现评论get链接 https://music.163.com/weapi/comment/resource/comments/get
# data值会出现在已有内容的列表里


i = "SD1IKPmTgqRCP8gJ"  #网易是随机的，简化过程，直接定死

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

def get_encSecKey():    
    """
    模拟生成encSecKey,即模拟function c,以及function d 的调用h.encSecKey = c(i, e, f),
    直接将i定死为固定值，encSeckey就会变成固定值，这两个值需要一起断点查找
    """
    return "8b5074fc68192b140b88c91861142bd16a708ee2b042b6945bcf1387a6fb4d999c58b93587c9303a12f87ca3b7fe01dff0ec6d4e846d501ca26f84bdf28d4ddf62ff381783cb81eb9c6f08f83b503c5d6569745f09f83ac1127f1f8da9eb93290c3ceed01aa40e9543f3548360d29587c868fa01d500b521cd03e3ddc5ebe517"

def get_params(data): # 现在的data是默认字符串，提交给网易云音乐服务器的data是字典，需要转化
    """
    模拟生成params,即function d中的这二次加密
    h.encText = b(d, g),     
    h.encText = b(h.encText, i)
    """
    first = enc_paramas(data, g)
    second = enc_paramas(first, i)
    return second

def to_16(data):
    """转化成16的倍数，为下方加密算法服务"""
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data
    
def enc_paramas(data, key):
    """模拟生成params,即模拟function b"""
    iv = "0102030405060708" 
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC )
    bs = aes.encrypt(data.encode("utf-8"))  # 加密的长度必须是16的倍数，不足补0
    return str(b64encode(bs),"utf-8")

def get_comments():
    """把response.text中的评论提取出来"""
    pass

def save():
    """把提取出来的评论保存为文件"""
    pass

resp = requests.post(url, data={
    'params': get_params(json.dumps(data) ),
    'encSecKey': get_encSecKey()
} )
# print(resp.json())
print(resp.text)