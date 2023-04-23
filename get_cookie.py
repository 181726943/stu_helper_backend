import time
import datetime

import json
import requests
from selenium import webdriver

#
#
#
# url = 'http://jw.swu.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=222019603193109'
# session = requests.Session()
# cookie = session.get(url).cookies.get_dict()
# print(type(cookie))
# print(cookie)


url1 = 'http://jw.swu.edu.cn/jwglxt/cjcx/cjcx_cxXsgrcj.html?sg8l3mmA' \
       '=1sDbbGlqExsx5VaqTRR0t7ofYBju5jb87ai1YDhzQaHd9AlbMnr6VWKVfmVY4BWAX6S5eGaNxZlZ7bKaU1WCfrYMd67pe_CwBQr43I' \
       '.Qgdl7pIailO.5yFz3d0TZo7WKFzHK1lIH.2PFXgUt6q6RcMmem2wxRDTD '
# url2 = 'http://jw.swu.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su=222019603193109'

cookie_str = "JSESSIONID=5CD5B9CF04A727305803D6345B7A894B; " \
             "61zqTsrO93nzS=5WOKQZEXlsDQPvnKrrAB0XxohP5giBJqvmTyJ7oyfvjk9YdFvhYaOKkHTEWEkKSJ84tIKRpm3AjgcpTjmu_WOaq; " \
             "1=56359.25038.15679.0000; 61zqTsrO93nzT=za67cWXrzRjXhKi9QnNChqNBz2GQz5cs8cmGD4z_mNa07pH1gN2SwcGLGSJNNor" \
             "OiHw7JF6LAcyB1sfb6d_YMfnafF7.aFlTXwq2g8gohnptAIIj9wbqRS5X73sZHifhhsvbybVObDlsJ_tx4Y0Flpt1hfQEsR5AiyyFgQ" \
             "tLvWUOY.u2WXc0x7hzErQmbJs3Pn7WgbcA8gwQH7bIdqHbCY3egkuvizzFQaxyPkTQ8duJ_JUEPAIBe4C3hMcynL4t9zCpMmDylu9wr" \
             "sp5FyxNzkpR0hPtNXVA0a_zVQZT9QVzBRZxQfT2VyPd3FnU0BqhGx4pKtY729xs_mndgJ_DeD2EvSEskAKEFiRPaC0da3CljC9le601" \
             "ClZ.n8LGKWkXbgqFmoXdP9GO978IZ.gKVA "

headers = {
    "Host": "jw.swu.edu.cn",
    "Connection": "keep-alive",
    "Content-Length": "147",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "http: // jw.swu.edu.cn",
    "Referer": "http://jw.swu.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su"
               "=222019603193109",
    # "Referer": "http://jw.swu.edu.cn/jwglxt/kwgl/kscx_cxXsksxxIndex.html?gnmkdm=N358105&layout=default&su"
    #            "=222019603193109",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": cookie_str,
    "Upgrade-Insecure-Requests": "1"

}

post_data = {
    "xnm": 2020,
    "xqm": 3,
    "_search": "false",
    "nd": str(int(time.time() * 1000)),
    "queryModel.showCount": 15,
    "queryModel.currentPage": 1,
    "queryModel.sortName": "",
    "queryModel.sortOrder": "asc",
    "time": 5,
}

session = requests.Session()
session.headers.update(headers)
res = session.post(url1, data=post_data)
result = res.json()
# print(res.raise_for_status())
print(type(res))
print(res)
print(type(result))
print(result)
# browser.close()
