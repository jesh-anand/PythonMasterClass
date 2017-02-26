import datetime
import uuid

from blog_site.terminal_blog.database.database import Database
from blog_site.terminal_blog.model.post import Post


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        self.title = input("Enter title: ")
        content = input("Enter content: ")
        date = input("Enter date, or leave blank for today (in format DDMMYY): ")
        post = Post(
            blog_id=id, title=self.title, content=content, author=self.author,
            date=datetime.datetime.strptime(date, "%d%m%Y")
        )

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blog', data=self.get_json())

    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'author': self.author
        }

    @classmethod
    def get_content_from_mongo_in_blog_object(cls, id):
        blog_data = Database.find_one(collection='blog', query={'id': id})
        return cls(
            author=blog_data['author'],
            title=blog_data['title'],
            description=blog_data['description'],
            id=blog_data['id']
        )
