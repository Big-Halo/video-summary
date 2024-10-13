def baidu_search(key_word):

    import requests
    # from lxml import etree
    import urllib
    headers={
        'User-Agent':'',
    }

    #url="https://baike.baidu.com/item/"
    url = "https://www.google.com/search?q="
    #key_word = (input())
    # 转化编码：parse为解析功能，quote为编码功能，errors是为了替换加上 ’ % '功能
    key_word=urllib.parse.quote(key_word,encoding='utf-8',errors='replace')
    word_url=url+key_word
    resp=requests.get(word_url,headers=headers)
    print(word_url)

    # from lxml import etree
    # e=etree.HTML(resp.text)
    #infos=e.xpath("//div[@class='para_y91E8 summary_TLESm MARK_MODULE‘]/text()")
    #test=e.xpath("//div[@class='para_y91E8 summary_TLESm MARK_MODULE']")
    # infos = e.xpath("//div[@class='para_y91E8 summary_TLESm MARK_MODULE']/span/text()")[0]
    # print(test)
    # print(infos)
    # ,infos
    return word_url