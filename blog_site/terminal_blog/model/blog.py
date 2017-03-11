import datetime
import uuid

from blog_site.common.database import Database
from blog_site.terminal_blog.model.post import Post


class Blog(object):
    COLLECTION_NAME = 'blog'
    DATE_FORMAT = "%d%m%Y"

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter title: ")
        content = input("Enter content: ")
        date = input("Enter date, or leave blank for today (in format DDMMYYYY): ")
        date = str(self.get_date(date))
        post = Post(
            blog_id=self.id, title=title,
            content=content, author=self.author,
            date=date
        )
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def get_date(self, date):
        if date == None or date == '':
            date = self.get_today_date()
        else:
            date = self.get_formated_date(date)
        return date

    def get_today_date(self):
        return datetime.datetime.utcnow()

    def get_formated_date(self, date):
        return datetime.datetime.strptime(date, Blog.DATE_FORMAT)

    def save_to_mongo(self):
        Database.insert(collection=Blog.COLLECTION_NAME, data=self.get_json())

    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'author': self.author
        }

    @classmethod
    def from_mongo_in_blog_object(cls, id):
        blog_data = Database.find_one(collection=Blog.COLLECTION_NAME, query={'id': id})
        return cls(
            author=blog_data['author'],
            title=blog_data['title'],
            description=blog_data['description'],
            id=blog_data['id']
        )
