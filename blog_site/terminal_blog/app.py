from blog_site.terminal_blog.database.database import Database
from blog_site.terminal_blog.model.menu import Menu

__author__ = 'Prajesh Ananthan'

Database.initialize()
menu = Menu()
menu.run_menu()
