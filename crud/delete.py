from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from threading import Thread
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash,check_password_hash
import read
import sys
sys.path.insert(0, '../models/')
import os

from models import Base,User,Filedetails
import datetime


engine = create_engine('sqlite:///crud/beeruva.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def deletefile(fileid,currentuser):
    """
    Function to delete a file by file id. 
    """
    session=DBSession()
    try:
        filedetails = session.query(Filedetails).filter_by(fileid=fileid).filter_by(userid=currentuser.userid).one()
        files = [filedetails]

        if filedetails.filetype == 'd':
            files.extend(read.u_getdescendents(fileid))
        
        if len(files) > 0:
            for i in files:
                filedetails=session.query(Filedetails).filter_by(fileid=i.fileid).filter_by(userid=currentuser.userid).one()
                session.delete(filedetails)
            for i in files:
                if i.filetype == 'f':
                    os.remove('static/fileuploadfolder/'+i.fileid)
            session.commit()
            return 'Successfully deleted'
        else:
            return 'Not found'
    except Exception as err:
        print err
        return 'Deletion Failed'
