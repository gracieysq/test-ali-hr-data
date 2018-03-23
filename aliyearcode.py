def years(i,n):
    """
    此程序统计阿里社招对工作经验的要求
    i,n均为positionid
    i为研究起始id，n为终点
    >>> years(40200,40300)
    有效数据： 100  一年以上:  0.02  二年以上:  0.02  三年以上:  0.56  五年以上:  0.37  其他:  0.03
    """
    aa = []
    import pandas as pd
    while i<n:
        try: 
            url = 'https://job.alibaba.com/zhaopin/position_detail.htm?positionId={}'.format(i)
            tbls = pd.read_html(url)
            comps = tbls[0]
            a = comps.iloc[0][5]
            aa.append(a)
            i = i + 1
        except:
            return None
    er = []
    wu = []
    san = []
    yi = []
    qt = []
    for k in aa:
        if k =="二年以上":
            er.append(k)
        elif k =="五年以上":
            wu.append(k)
        elif k =="三年以上":
            san.append(k)
        elif k =="一年以上":
            yi.append(k)
        else:
            qt.append(k)
    print("有效数据：",len(aa),
          " 一年以上: ",len(yi)/len(aa),
          " 二年以上: ",len(er)/len(aa),
          " 三年以上: ",len(san)/len(aa),
          " 五年以上: ",len(wu)/len(aa),
          " 其他: ",len(qt)/len(aa))

years(40200,40300)
years(10000,10100)
