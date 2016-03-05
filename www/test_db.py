from models import User
from transwrap import db
from utils import getTimestamp

db.create_engine(user='root', password='testin', database='FinanceAdmin_db', host='127.0.0.1', port=3306)

#u = User(name='xuanzhen', email='xuanzhen@testin.cn', password='123456', createtime=getTimestamp())

#u.insert()

u1 = User.find_first('where email=?', 'xuanzhen@testin.cn')
print 'find user\'s name:', u1

u1.status = '1'
u1.update()

#u1.delete()

