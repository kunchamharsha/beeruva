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


engine = create_engine('sqlite:///crud/beeruva.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


def renamefile(currentuser,data):
    """
    Function to update file name in db.
    """
    session=DBSession()
    try:
        filedetails=session.query(Filedetails).filter_by(fileid=data['fileid']).filter_by(userid=currentuser.userid).one()
        filedetails.filename=data['filerename']
        session.commit()
        session.close()
        return 'Successfully Uploaded'
    except NoResultFound:
        return 'You are not authorised to modify this file.'