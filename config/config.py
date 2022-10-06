"""The unit contains named constants for different purposes like JSON
uploading, DAO testing"""
from os import path
from dao.posts_dao import PostsDao

# path constants building based on OS
POSTS_FILE = path.join('data', 'posts.json')
COMMENTS_FILE = path.join('data', 'comments.json')
LOG_FILE = path.join('logs', 'api.log')
BOOKMARKS_PATH = path.join('data', 'bookmarks.json')
IMG_PATH = 'img'

# format string for logger
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'

# a set of keys for testing
POSTS_KEYS = {'poster_name',
              'poster_avatar',
              'pic',
              'content',
              'views_count',
              'likes_count',
              'pk',
              'comments_count'
              }
COMMENTS_KEYS = {'post_id',
                 'commenter_name',
                 'comment',
                 'pk'
                 }

# creating a PostsDao instance to use in whole app
post_dao = PostsDao(POSTS_FILE, COMMENTS_FILE, BOOKMARKS_PATH)
