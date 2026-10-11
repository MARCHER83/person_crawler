import requests, re, json, time, csv, os
import execjs

class Spider():
    def __init__(self):
        self.start_url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': 'https://s.taobao.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'Cookie': 'thw=xx; cna=RZ3GIU0Hj3ABASQIhF31lfeC; tracknick=111%5Cu5343%5Cu6CAB; aui=3331365111; wk_cookie2=12906d9b4469e19f29b2f94b35b7f01a; wk_unb=UNN%2Bxy6c7TRGnQ%3D%3D; _hvn_lgc_=0; havana_lgc2_0=eyJoaWQiOjMzMzEzNjUxMTEsInNnIjoiODg3NjA4MWY3MmY3NzNlZDg1YjQ4YzRlMDUxNzFhMzEiLCJzaXRlIjowLCJ0b2tlbiI6IjExRXB5VjZVRTZmQ1pOQmZEUF9ObllBIn0; cookie2=16298acc5cd98b6ab614ba9a1310cb90; t=ed97aa936c04a8a5c57af796e49a889e; xlly_s=1; sca=c7c3e674; _samesite_flag_=true; sn=; lgc=111%5Cu5343%5Cu6CAB; cancelledSubSites=empty; _tb_token_=f1e6850353b1d; unb=3331365111; uc1=existShop=false&pas=0&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie21=VT5L2FSpczFp&cookie14=UoYWO653SmL1uA%3D%3D; uc3=nk2=UoCIse5lKA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD1NmjkKMgIMhVKwQ%3D&id2=UNN%2Bxy6c7TRGnQ%3D%3D; csg=d731a301; cookie17=UNN%2Bxy6c7TRGnQ%3D%3D; dnk=1479%5Cu5343%5Cu6CAB; skt=2397437a3fca7cae; existShop=MTc4Njc1NjgzMA%3D%3D; uc4=id4=0%40UgQ2gbU0THW0X0sqAL2tcH65A5f7&nk4=0%40UOg0wxWsS%2FWCEESWHsvESJCw; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%B2%AB11; _nk_=111%5Cu5343%5Cu6CAB; cookie1=U%2BNiVP6pAnuByyxBYlQqQKZh4Yuex4%2BVzpz6BsfLvN0%3D; sgcookie=E100W5PBc4e50bCKMfSwOo0iQgCuGhICjW4bqCPZlapO6o%2Bu4c0tvLltj5%2FKTffbvT%2FtGSOdflqZyBpfzrBHUa8y2nET01qOsVB9o4TzUBbQrj9tIUYeY3NAGyQQUSw%2Bn88n; ultraCookieBase=1k6S45BQHShE1%2F0ySlsVSOzl2kvngp1tG35hIaOptu2PqFoIV9ZT4U0Ih9%2BEYquEoB3GPtxD%2BRXuoFpz0HZUmdfxYFUWZiD1v3I0fjl9C6wPFjlCh8BZmaDD6jA7pfRFH%2FXEGFS0x%2Fk9L1TpCUMHxBT4IXF6jCZWqpYpLzSJg6570Au7G%2FaHO6JgaHZSjHRjkBDl%2BiaSqS9E%2BNGqJekXc%2BdqXJZDxa8SE6nKV6NkQG%2BB13BzELvy1P4qfQmFC1L7nttruOUiOu6JaqCWBuMTZLtGI%2BT7dwbDyrqC4BghxX0aeBDol; havana_lgc_exp=1817892931044; sdkSilent=1786817731044; havana_sdkSilent=1786817731044; mtop_partitioned_detect=1; _m_h5_tk=de17faac0d861405a67aa3e21fc139de_1786814171256; _m_h5_tk_enc=8e59ea0074a8dd4f337ead3d9a04a01e; isg=BDo6X1hCBDUdzotm2-QQXaLDi2Bc677FIZXhoEQz5k2YN9pxLHsO1QBBg8PrpzZd',
        }
        self.all_items = []  # 存储所有商品
    
    def parse_get_sign(self, t, data):
        token = re.findall(r'_m_h5_tk=(.*?)_', self.headers['Cookie'])[0]
        get_sign = token + "&" + t + "&" + '12574478' + "&" + data
        
        with open('try26_MD5.js', 'r', encoding='utf-8') as f:
            js = f.read()
            ctx = execjs.compile(js)
            sign_md5 = ctx.call('eE', get_sign)
        
        return sign_md5

    def build_data(self, page=1):
        params_obj = {
            "device": "HMA-AL00", "isBeta": "false", "grayHair": "false",
            "from": "nt_history", "brand": "HUAWEI", "info": "wifi",
            "index": "4", "rainbow": "", "schemaType": "auction",
            "elderHome": "false", "isEnterSrpSearch": "true",
            "newSearch": "false", "network": "wifi", "subtype": "",
            "hasPreposeFilter": "false", "prepositionVersion": "v2",
            "client_os": "Android", "gpsEnabled": "false",
            "searchDoorFrom": "srp", "debug_rerankNewOpenCard": "false",
            "homePageVersion": "v7", "searchElderHomeOpen": "false",
            "search_action": "initiative", "sugg": "_4_1",
            "sversion": "13.6", "style": "list",
            "ttid": "600000@taobao_pc_10.7.0", "needTabs": "true",
            "areaCode": "CN", "vm": "nw", "countryNum": "156",
            "m": "pc", "page": page, "n": 48, "q": "书包",
            "qSource": "url", "pageSource": "", "channelSrp": "",
            "tab": "all", "pageSize": 48, "totalPage": 100,
            "totalResults": 4800, "sourceS": "0", "sort": "_coefp",
            "bcoffset": "", "ntoffset": "", "filterTag": "",
            "service": "", "prop": "", "loc": "",
            "start_price": None, "end_price": None,
            "startPrice": None, "endPrice": None,
            "itemIds": None, "p4pIds": None, "p4pS": None,
            "categoryp": "", "ha3Kvpairs": None,
            "myCNA": "RZ3GIU0Hj3ABASQIhF31lfeC",
            "screenResolution": "1920x1080",
            "viewResolution": "1903x1533",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "couponUnikey": "", "subTabId": "", "np": "",
            "clientType": "h5", "isNewDomainAb": "false",
            "forceOldDomain": "false"
        }
        
        data_obj = {
            "appId": "34385",
            "params": json.dumps(params_obj, ensure_ascii=False, separators=(',', ':'))
        }
        return json.dumps(data_obj, ensure_ascii=False, separators=(',', ':'))

    def parse_start_url(self, page=1):
        """发送请求"""
        t = str(int(time.time() * 1000))
        data = self.build_data(page)
        
        # 随机 callback 名，和浏览器行为一致
        callback = f'mtopjsonp{page + 5}'
        
        params = {
            'jsv': '2.7.4', 'appKey': '12574478', 't': t,
            'sign': self.parse_get_sign(t, data),
            'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
            'v': '2.0', 'timeout': '10000',
            'type': 'jsonp', 'dataType': 'jsonp',
            'callback': callback,
            'data': data,
        }
        
        response = requests.get(url=self.start_url, headers=self.headers, params=params, timeout=15)
        return response.text


    def parse_response_data(self, response_text):
        """
        解析 JSONP 响应，提取商品列表
        """
        try:
            # 去掉 JSONP 包装：支持任意回调名 mtopjsonp1, mtopjsonp6, mtopjsonp100...
            match = re.search(r'mtopjsonp\d+\((.*)\)$', response_text, re.S)
            if match:
                json_str = match.group(1)
            else:
                json_str = response_text
            
            result = json.loads(json_str)
            
            # 检查报错
            if 'ret' in result:
                for r in result['ret']:
                    if 'FAIL' in str(r) or 'ERROR' in str(r):
                        print(f"接口报错: {r}")
                        return []
            
            # ========== 关键调试：打印 data 下的所有 key ==========
            data = result.get('data', {})
            print(f"\n【data 下的所有 key】: {list(data.keys())}")
            
            # 递归查找包含商品数组的字段
            def find_items(obj, path=""):
                """递归查找可能是商品列表的数组"""
                if isinstance(obj, list) and len(obj) > 0:
                    # 检查第一个元素是否有商品特征字段
                    first = obj[0]
                    if isinstance(first, dict):
                        has_item_features = any(k in first for k in ['title', 'itemId', 'item_id', 'nid', 'picUrl', 'pic', 'price', 'salePrice'])
                        if has_item_features:
                            print(f"\n【找到商品列表】路径: {path}, 数量: {len(obj)}")
                            print(f"【第一条数据样例】: {json.dumps(first, ensure_ascii=False)[:500]}")
                            return obj
                    return None
                
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        found = find_items(v, f"{path}.{k}")
                        if found:
                            return found
                return None
            
            items = find_items(data, "data")
            
            if not items:
                print("【警告】没找到商品数组，打印前 2000 字符看看结构:")
                print(json.dumps(data, ensure_ascii=False, indent=2)[:2000])
                return []
            
            # 提取商品字段（根据实际 key 名调整）
            clean_items = []
            for item in items:
                clean_item = {
                    'title': item.get('title') or item.get('itemTitle') or item.get('name') or '',
                    'price': item.get('price') or item.get('salePrice') or item.get('view_price') or '',
                    'originalPrice': item.get('originalPrice') or item.get('reservePrice') or '',
                    'itemId': item.get('itemId') or item.get('item_id') or item.get('nid') or '',
                    'picUrl': item.get('picUrl') or item.get('pic') or item.get('img') or '',
                    'shopName': item.get('shopName') or item.get('nick') or item.get('shop') or '',
                    'sales': item.get('sales') or item.get('sale') or item.get('sellCount') or '',
                    'location': item.get('location') or item.get('area') or '',
                }
                clean_items.append(clean_item)
            
            return clean_items
            
        except json.JSONDecodeError as e:
            print(f"JSON 解析失败: {e}")
            print(f"原始返回长度: {len(response_text)}")
            print(f"原始返回前 500 字: {response_text[:500]}")
            print(f"原始返回后 100 字: {response_text[-100:]}")
            return []
        except Exception as e:
            print(f"解析异常: {e}")
            return []

    def parse_save_data(self, items, filename='taobao_bag'):
        """
        保存数据到 CSV 和 JSON
        """
        if not items:
            print("没有数据需要保存")
            return
        
        # 去重：按 itemId 去重
        seen = set()
        unique_items = []
        for item in items:
            item_id = item.get('itemId', '')
            if item_id and item_id not in seen:
                seen.add(item_id)
                unique_items.append(item)
        
        # 1. 保存为 CSV
        csv_file = f'{filename}.csv'
        file_exists = os.path.exists(csv_file)
        
        with open(csv_file, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'title', 'price', 'originalPrice', 'itemId', 
                'picUrl', 'shopName', 'sales', 'location', 'page'
            ])
            if not file_exists:
                writer.writeheader()
            writer.writerows(unique_items)
        
        # 2. 保存为 JSON（追加模式，每次写完整文件）
        json_file = f'{filename}.json'
        existing = []
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    existing = json.load(f)
            except:
                pass
        
        existing.extend(unique_items)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 本次新增 {len(unique_items)} 条，累计 {len(existing)} 条")
        print(f"📁 CSV: {csv_file}")
        print(f"📁 JSON: {json_file}")

    def run(self, pages=3):
        """
        主运行函数：爬取多页
        """
        print(f"开始爬取淘宝「书包」，共 {pages} 页...\n")
        
        for page in range(1, pages + 1):
            print(f"正在爬取第 {page} 页...")
            try:
                response_text = self.parse_start_url(page)
                items = self.parse_response_data(response_text)
                
                if items:
                    self.all_items.extend(items)
                    self.parse_save_data(items)
                else:
                    print(f"第 {page} 页无数据，可能 Cookie 过期或接口限制")
                
                # 随机延时，防止被封
                time.sleep(1.5 + (page % 3))
                
            except Exception as e:
                print(f"第 {page} 页出错: {e}")
                continue
        
        print(f"\n🎉 爬取完成！共获取 {len(self.all_items)} 条商品数据")


if __name__ == '__main__':
    spider = Spider()
    spider.run(pages=3)  # 先爬3页试试