# person_crawler
# Python 爬虫项目集

个人爬虫工程化实践项目合集，覆盖 **JS 逆向、加密还原、Scrapy 分布式、异步高并发、动态渲染、流媒体下载、电商接口签名还原** 等核心爬虫技术场景。

&gt; ⚠️ 免责声明：本项目仅供学习与技术交流使用，所有代码仅针对公开数据，请勿用于任何商业或违法用途。

---

## 🗂️ 项目索引

| 目录 | 技术点 | 说明 |
|---|---|---|
| [`taobao-mtop/`](./taobao-mtop) | 签名还原 · Cookie 会话 | **淘宝商品搜索接口逆向**：抓包定位 mtop JSONP 接口，还原 `_m_h5_tk` token 提取 + MD5 签名（sign）生成算法，实现登录态下商品数据多页采集，含 itemId 去重、CSV/JSON 双格式存储、随机延时反限流 |
| [`crypto-reverse/`](./crypto-reverse) | JS 逆向 · AES/RSA | 网易云音乐评论：断点定位 `window.asrsea`，纯 Python 还原前端 AES-CBC 双重加密 + RSA，模拟生成 `params`/`encSecKey` |
| [`crypto-reverse/`](./crypto-reverse) | 流媒体 · AES 解密 | m3u8/ts 视频下载全流程：解析 m3u8、AES-CBC 解密 ts 分片、异步解密、合并输出 MP4 |
| [`douban/`](./douban) | Scrapy · scrapy-redis Selenium| 豆瓣 Top250：xpath 翻页采集 + scrapy-redis 分布式 Spider 详情页二级解析（meta 传参）,Selenium 处理 JS 动态加载页面 |
| [`tencent/`](./tencent) | Scrapy · API 分页 | 腾讯招聘 JSON API 全量分页采集，Item/Pipeline 数据结构化 |
| [`wangyi/`](./wangyi) | Scrapy · POST API | 网易招聘 POST 接口翻页采集，数据清洗与字段提取 |
| [`baodi_splash/`](./splash) | 动态渲染 | Splash 渲染服务 vs 静态请求效果对比验证 |

## 🛠️ 技术栈

- **逆向**：Chrome DevTools 断点调试、AES-CBC / RSA / MD5 签名还原、mtop JSONP 接口分析、请求参数加密模拟
- **框架**：Scrapy、scrapy-redis（分布式）、Selenium、Splash
- **异步**：asyncio、aiohttp、aiofiles（高并发下载/解密）
- **流媒体**：m3u8 解析、ts 分片 AES 解密、FFmpeg / copy 合并
- **存储**：MySQL、Redis、JSON/CSV
- **工具**：Fiddler / Reqable 抓包、adb、Git

