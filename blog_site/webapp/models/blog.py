import datetime
import uuid

from blog_site.common.database import Database
from blog_site.webapp.models.post import Post


class Blog(object):
    COLLECTION_NAME = 'blog'

    def __init__(self, author, title, description, author_id, _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, created_date=datetime.datetime.utcnow()):
        self.created_date = str(created_date)
        post = Post(
            blog_id=self._id,
            title=title,
            content=content,
            author=self.author,
            created_date=self.created_date
        )
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self._id)

    def get_date(self, _date):
        date_format = "%d%m%Y"
        today_date = datetime.datetime.utcnow()
        input_date = datetime.datetime.strptime(_date, date_format)
        return today_date if _date is None else input_date

    def save_to_mongo(self):
        Database.insert(collection=Blog.COLLECTION_NAME, data=self.get_json())

    def get_json(self):
        return {
            'id': self._id,
            'title': self.title,
            'description': self.description,
            'author': self.author,
            'author_id': self.author_id
        }

    @classmethod
    def from_mongo_in_blog_object(cls, _id):
        blog_data = Database.find_one(collection=Blog.COLLECTION_NAME, query={'_id': _id})
        return cls(**blog_data)

    @classmethod
    def find_author_by_id(cls, author_id):
        # will return content from Database not blog objects
        blogs = Database.find(Blog.COLLECTION_NAME, query={'author_id': author_id})
        return [cls(**blog) for blog in blogs]
