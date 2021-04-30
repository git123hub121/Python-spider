#接下来用mysql来保存
#这个书也太会偷懒了吧，竟然要我自己建库和建表
import pandas as pd
df = pd.read_excel('D:\Python\爬取网易云课堂\网易云课堂.xlsx')
df.head(5)
df.index.name = 'id'
df.head(2)
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/flask",echo=False)
df.to_sql(name = 'wyykt',con = engine,if_exists="replace")
print(engine.execute("show create table wyykt").first()[1])
print(engine.execute("select count(1) from wyykt").first())
engine.execute("select * from wyykt limit 3").fetchall()