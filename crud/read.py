from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from threading import Thread
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash,check_password_hash
import sys
from flask import jsonify
sys.path.insert(0, '../models/')


from models import Base,User,Filedetails
import datetime


engine = create_engine('sqlite:///crud/beeruva.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

def listofilesuploaded(currentuser):
    """
    Function to return list of files uploaded by a user. 
    """
    session=DBSession()
    files=session.query(Filedetails).filter_by(userid=currentuser.userid)
    listoffiles=[]
    for i in files:
        filedata={}
        filedata['fileid']=i.fileid        
        filedata['filename']=i.filename        
        filedata['filetype']=i.fileextension
        listoffiles.append(filedata)
    return jsonify(listoffiles)

def check_access(fileid,currentuser):
    """
    Function to check users access to the requested file.
    """
    session=DBSession()
    returnfiledata={}
    try:
        filedata=session.query(Filedetails).filter_by(userid=currentuser.userid).filter_by(fileid=fileid).one()
        returnfiledata['fileid']=filedata.fileid
        returnfiledata['filename']=filedata.filename
        returnfiledata['access_state']=1
        return returnfiledata
    except NoResultFound:
        returnfiledata['access_state']=0
        return returnfiledata 