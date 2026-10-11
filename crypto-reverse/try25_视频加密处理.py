import requests,os
from Crypto.Cipher import AES
import asyncio,aiofiles,aiohttp #异步库

def get_key(url):
    """得到密钥"""
    resp = requests.get(url)
    resp.encode('utf-8')
    ker_content = resp.text
    print(ker_content)
    return ker_content
async def dec_ts(key_content,file_name):
    """解密"""
    aes = AES.new(key= key_content, IV=b'0000000000000000',mode=AES.MODE_CBC)
    async with aiofiles.open(f'./dir/{file_name}','rb') as f1, \
        aiofiles.open(f'./dir/temp_{file_name}','wb') as f2:#写文件
            
        bs = await f1.read()    #从源文件读取内容
        await f2.write(aes.decrypt(bs))
        print(f'{file_name}解密完成')
        
async def aio_dec_task(key_content,file_name_list):
    """异步解密任务"""
    tasks = []
    for file_name in file_name_list:
        task = asyncio.create_task(dec_ts(key_content,file_name))
        tasks.append(task)
    await asyncio.gather(*tasks)
    
def merge_ts(file_name_list):
    """合并 先转成地址 copy/b  """
    list = []
    for file_name in file_name_list:
        list.append(f'./dir/temp_{file_name}')
    s = ' '.join(list)    
    os.system(f'copy/b {s} > movie.mp4')
        
def main():
    #
    #
    asyncio.run(aio_dec_task)
        
    