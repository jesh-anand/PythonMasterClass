import datetime
import uuid

from blog_site.terminal_blog.database.database import Database

__author__ = 'Prajesh Ananthan'


class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_post_in_mongo_db(self):
        collection_name = 'posts'
        Database.insert(collection=collection_name, data=self.get_json())

    def get_json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'created_date': self.created_date,
            'content': self.content,
            'author': self.author
        }

    @classmethod
    def from_mongo_db_into_post_object(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(
            blog_id=post_data['blog_id'],
            title=post_data['title'],
            content=post_data['content'],
            author=post_data['author'],
            date=post_data['date']
        )

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='blog', query={'id': id})]
