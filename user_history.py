
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
import os
from sqlalchemy.ext.declarative import declarative_base
import datetime
from db import Session,Base
#define user history table 
class UserHistory(Base):
    __tablename__ = 'user_history'
    id = Column(Integer, primary_key=True)
    user_id =Column(String)
    search_query = Column(String)
    searched_at=Column(DateTime(),default=datetime.datetime.utcnow)

    # retrieval of search history of user in the particular channel in descending order timewise
    @classmethod
    def get_search_history(cls,search_query,user_id):
        session = Session()
        db_query="%"+search_query+"%"
        print(db_query)
        result_obj= session.query(cls).filter(*[cls.search_query.ilike(db_query),cls.user_id==str(user_id)]).order_by(cls.searched_at.desc()).all()
        result=[]
        for row in result_obj:
            result.append(row.search_query)
        session.close()
        return result
    
    #storing of search query in db
    @classmethod
    def add(cls,search_query,user_id):
        session = Session()
        srch_query= session.query(cls).filter(*[cls.search_query==search_query,cls.user_id==str(user_id)]).all()
        print(srch_query)
        if len(srch_query)!=0:
            srch_query[0].searched_at=datetime.datetime.utcnow()
            session.commit()
            session.close()
        else:
            srch_query=cls(user_id=str(user_id),search_query=search_query)
            session.add(srch_query)
            session.commit()
            session.close()
        
        



        
