from models import User, Contract
from transwrap import db
from utils import getTimestamp
import config
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

db.create_engine(**config.configs.db)

#test User
#u = User(name='xuanzhen', email='xuanzhen@testin.cn', password='123456', createtime=getTimestamp())

#u.insert()

#u1 = User.find_first('where email=?', 'xuanzhen@testin.cn')
#print 'find user\'s name:', u1

#u1.status = '1'
#u1.updatetime = getTimestamp()
#u1.descr = 'Administrator'
#u1.update()

#u1.delete()


#test Contract
c = Contract(contract_id='MX-20160305', price=100.00, num=10, starttime=getTimestamp(), endtime=getTimestamp(), signtime=getTimestamp(), type=1, status=1, descr='test', createtime=getTimestamp())

c.insert()

cs = Contract.find_all()

print cs
