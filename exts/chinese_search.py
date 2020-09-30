# -*- coding: utf-8 -*- 
import zh

def setup(app): 
    import sphinx.search as search
    search.languages["zh_CN"] = zh.SearchChinese