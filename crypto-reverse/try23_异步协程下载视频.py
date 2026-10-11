import requests ,re,os
from urllib.parse import urljoin
def get_index_m3u8(url,session,obj,headers):
    """ 拿到index.m3u8"""
    resp = session.get(url,headers=headers)
    m3u8_url = obj.findall(resp.text)[0]
    print(m3u8_url)
    resp.close()
    return m3u8_url

def get_ts(m3u8_url,session,headers):
    """ 拿到第一次的伪装ts"""
    resp2 = session.get(m3u8_url, headers=headers)
    
    base_url = urljoin(m3u8_url, './')
    print(base_url)
    m3u8_content = resp2.text.strip()

    for line in m3u8_content.splitlines():
        if line and not line.startswith('#'):
            ts_url = urljoin(base_url, line)  # 智能拼接
            print(ts_url)
    return ts_url
def get_ts_downloadurls(ts_url,session,headers):
    """ 拿到真正的ts地址"""
    base_url2 =  urljoin(ts_url, './') 
    resp3 = session.get(ts_url, headers=headers)
    # print(resp3.text)
    ts_downloadurls = []    #改成异步就是在此创建任务
    for line in resp3.text.splitlines():
            if line and not line.startswith('#'):
                ts_downloadurl = urljoin(base_url2, line)   
                ts_downloadurls.append(ts_downloadurl)
    print(ts_downloadurls[0:50])  
    session.close()
    return ts_downloadurls
def download_video(ts_downloadurls):
    pass
def main():
    session = requests.Session()
    obj = re.compile(r'.*?<script>.*?now="(?P<url>.*?)";', re.S)
    url = 'https://xcka.cc/play/106535-0-0.html'
    headers = {
    'Referer':url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
    index_m3u8_url = get_index_m3u8(url, session, obj, headers)
    false_tsurl = get_ts(index_m3u8_url,session,headers)
    ts_downloadurls = get_ts_downloadurls(false_tsurl, session,headers)
    
if __name__ == '__main__':
    main()