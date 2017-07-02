import datetime
import uuid

from flask import session

from blog_site.common.database import Database
from blog_site.webapp.models.blog import Blog

class User(object):
    COLLECTION_NAME = 'users'

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one(User.COLLECTION_NAME, {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one(User.COLLECTION_NAME, {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            # TODO: notify user account exists!
            return False

    def new_blog(self, title, description):
        blog = Blog(
            author=self.email,
            title=title,
            description=description,
            author_id=self._id
        )
        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):
        # title, content, created_date=datetime.datetime.utcnow()
        blog = Blog.from_mongo_in_blog_object(blog_id)
        blog.new_post(title=title, content=content, created_date=date)

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blog.find_author_by_id(self._id)

    def get_json(self):
        # TODO: Encrypt password
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert(User.COLLECTION_NAME, self.get_json())
