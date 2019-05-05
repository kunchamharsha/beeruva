from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Boolean, VARCHAR, Integer, String, DateTime, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import TEXT

engine = create_engine('sqlite:///beeruva.db', encoding="utf-8")

Base = declarative_base() 
DBSession = sessionmaker(bind=engine)

session = DBSession()
class User(Base):
    __tablename__ = 'user'
    userid = Column(VARCHAR(36), primary_key=True)
    email = Column(VARCHAR(256),unique=True)    
    password = Column(VARCHAR(256))
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.userid

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Filedetails(Base):
    __tablename__='filedetails'
    fileid=Column(VARCHAR(36),primary_key=True)
    userid=Column(VARCHAR(36),ForeignKey('user.userid'))
    filename=Column(VARCHAR(128))
    parentid=Column(VARCHAR(36),ForeignKey('user.userid'), nullable = False)
    fileextension=Column(VARCHAR(128))
    filetype=Column(VARCHAR(5))
    fileuploadedon=Column(DateTime)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
