print("序列化：把变量从内存中变成可存储或传输的过程")
print("python专门提供pickle模块")
import  pickle
d = dict(name="bob", age = 20, score = 88)
pickle.dumps(d)
with open("xiao.txt","wb") as f:
    f.write(pickle.dumps(d))
print(pickle.dumps(d))
# with open("xiao.txt","wb") as f:
#     pickle.dump(d,f)
print("读取！")
with open("xiao.txt","rb") as e:
    ff = pickle.load(e)
print(ff)
print("JSON:")

import  json
print(json.dumps(d),"返回一个str")
with open("xiao.txt","w") as fj:
    fj.write(json.dumps(d))
