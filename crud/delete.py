from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from threading import Thread
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash,check_password_hash
import sys
sys.path.insert(0, '../models/')
import os

from models import Base,User,Filedetails
import datetime


engine = create_engine('sqlite:///crud/opendrive.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def deletefile(fileid,currentuser):
    """
    Function to delete a file by file id. 
    """
    session=DBSession()
    try:
        filedetails=session.query(Filedetails).filter_by(fileid=fileid).filter_by(userid=currentuser.userid).one()
        session.delete(filedetails)  
        session.commit()
        os.remove('static/fileuploadfolder/'+fileid)
        return 'Successfully deleted the file!'
    except NoResultFound:
        return 'Failed deleting the file!'
    except OSError:
        return 'No File Found!'