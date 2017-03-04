import uuid

from blog_site.terminal_blog.database.database import Database

__author__ = 'Prajesh Ananthan'


class Post(object):
    COLLECTION_NAME = 'posts'
    BLOG_COLLECTION = 'blog'

    def __init__(self, blog_id, title, content, author, date, id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection=Post.COLLECTION_NAME, data=self.get_json())

    def get_json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.date
        }

    @classmethod
    def from_mongo_db_into_post_object(cls, id):
        post_data = Database.find_one(collection=Post.COLLECTION_NAME, query={'id': id})
        return cls(
            blog_id=post_data['blog_id'],
            title=post_data['title'],
            content=post_data['content'],
            author=post_data['author'],
            date=post_data['date']
        )

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection=Post.BLOG_COLLECTION, query={'id': id})]
