from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from threading import Thread
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash,check_password_hash
import sys
sys.path.insert(0, '../models/')


from models import Base,User,Filedetails
import datetime


engine = create_engine('sqlite:///crud/opendrive.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def addfile(fileid,actualfilename,currentuser):
    """
    Function to store file data in db.
    """
    session=DBSession()
    filedetails=Filedetails(fileid=fileid,filename=actualfilename,fileuploadedon=datetime.datetime.now(),fileextension=actualfilename.split('.')[-1].lower(),userid=currentuser.userid)
    session.add(filedetails)
    session.commit()
    session.close()
    return 'Successfully Uploaded'