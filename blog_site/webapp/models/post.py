import datetime
import uuid

from blog_site.common.database import Database

__author__ = 'Prajesh Ananthan'


class Post(object):
    COLLECTION_NAME = 'posts'

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection=Post.COLLECTION_NAME, data=self.get_json())

    def get_json(self):
        return {
            'id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo_in_post_object(cls, id):
        post_data = Database.find_one(collection=Post.COLLECTION_NAME, query={'id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection=Post.COLLECTION_NAME, query={'blog_id': id})]
