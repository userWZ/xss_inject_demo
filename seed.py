import sqlite3
import datetime
import random
import string
import nltk
from nltk.corpus import words
from datetime import datetime, timedelta
nltk.download('words')

def generate_title():
    # 生成標題
    title_length = random.randint(1, 5)  # 隨機選擇標題長度
    title_words = random.choices(words.words(), k=title_length)
    title = ' '.join(title_words)
    return title

def generate_article():
    # 生成文章
    article_length = random.randint(100, 500)  # 隨機選擇文章長度
    article_words = random.choices(words.words(), k=article_length)
    article = ' '.join(article_words)
    return article

def generate_random_article():
    # 生成隨機文章及其標題
    title = generate_title()
    article = generate_article()

    # 添加隨機時間
    start_date = datetime.now() - timedelta(days=365)  # 從一年前開始計算
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    formatted_date = random_date.strftime("%Y-%m-%d")

    return title, article, formatted_date
# BLOG POST CONFIG
title, content, date_posted  = generate_random_article()
category = "Blog Post"
# content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
#           "dolore magna aliqua. Mauris nunc congue nisi vitae. Orci phasellus egestas tellus rutrum tellus " \
#           "pellentesque eu tincidunt. Diam donec adipiscing tristique risus nec feugiat. In massa tempor nec feugiat " \
#           "nisl. Ut morbi tincidunt augue interdum velit euismod in pellentesque massa. Commodo viverra maecenas " \
#           "accumsan lacus vel. Scelerisque fermentum dui faucibus in ornare quam. Arcu cursus vitae congue mauris. " \
#           "Libero volutpat sed cras ornare arcu dui vivamus arcu felis. Mi proin sed libero enim sed faucibus turpis " \
#           "in eu. Dictum at tempor commodo ullamcorper a. Diam quis enim lobortis scelerisque fermentum dui faucibus " \
#           "in ornare. Scelerisque eleifend donec pretium vulputate. Tincidunt praesent semper feugiat nibh. Sed sed " \
#           "risus pretium quam vulputate. Sed viverra tellus in hac habitasse platea dictumst. Sagittis vitae et leo " \
#           "duis. Vestibulum lorem sed risus ultricies. At imperdiet dui accumsan sit amet nulla. Gravida dictum fusce " \
#           "ut placerat. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Dictum sit amet justo donec " \
#           "enim. Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac. Sit amet luctus venenatis " \
#           "lectus magna fringilla urna. Netus et malesuada fames ac turpis egestas sed. Quis commodo odio aenean sed " \
#           "adipiscing diam donec adipiscing. Tortor vitae purus faucibus ornare suspendisse sed. Netus et malesuada " \
#           "fames ac turpis. Eget nunc lobortis mattis aliquam faucibus purus in massa tempor. Feugiat sed lectus " \
#           "vestibulum mattis ullamcorper velit sed ullamcorper morbi. "
# date_posted = "2023-05-02"
author = ""

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

create_post_query = "INSERT INTO home_post (id, title, category, content, date_posted) VALUES (NULL, ?, ?, ?, ?)"
create_post_params = (title, category, content, date_posted)
cursor.execute(create_post_query, create_post_params)
conn.commit()

print("[*] Successfully seeded the database! [*]")
