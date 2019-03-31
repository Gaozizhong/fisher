"""
    @File  : test.py
    @Author: GaoZizhong
    @Date  : 2019/3/28 19:07
    @Desc  : 
"""
from flask import jsonify

from . import web

__author__ = "GaoZizhong"


@web.route("/classic/latest")
def latest():
    r = {
        "content": "人生不能像做菜，把所有的料准备好才下锅",
        "fav_nums": 28,
        "id": 1,
        "image": "http://bl.7yue.pro/images/movie.8.png",
        "index": 7,
        "like_status": 1,
        "pubdate": "2018-06-22",
        "title": "李安<<饮食男女>>",
        "type": 100
    }
    return jsonify(r)


@web.route("/classic/<int:index>/previous", methods=['GET'])
def previous(index):
    r = {
         "content": "你陪我步入蝉夏 越过城市喧嚣",
        "fav_nums": 0,
        "image": "http://bl.7yue.pro/images/music.1.png",
        "id": 3,
        "index": 6,
        "like_status": 0,
        "pubdate": "2018-06-22",
        "title": "纸短情长",
        "type": 200,
        "url": "http://music.163.com/song/media/outer/url?id=516076896.mp3"
    }
    return jsonify(r)


@web.route("/classic/<int:index>/next", methods=['GET'])
def next2(index):
    r = {
        "content": "这个夏天又是一个毕业季",
        "fav_nums": 0,
        "id": 2,
        "image": "http://bl.7yue.pro/images/sentence.2.png",
        "index": 7,
        "like_status": 0,
        "pubdate": "2018-06-22",
        "title": "未名",
        "type": 300
    }
    return jsonify(r)


@web.route("/like", methods=['POST'])
def like():
    r = {
        "content": "人生不能像做菜，把所有的料准备好才下锅",
        "fav_nums": 28,
        "id": 1,
        "image": "http://bl.7yue.pro/images/movie.8.png",
        "index": 7,
        "like_status": 1,
        "pubdate": "2018-06-22",
        "title": "李安<<饮食男女>>",
        "type": 100
    }
    return jsonify(r)


@web.route("/like/cancel", methods=['POST'])
def dislike():
    r = {
        "content": "人生不能像做菜，把所有的料准备好才下锅",
        "fav_nums": 28,
        "id": 1,
        "image": "http://bl.7yue.pro/images/movie.8.png",
        "index": 7,
        "like_status": 1,
        "pubdate": "2018-06-22",
        "title": "李安<<饮食男女>>",
        "type": 100
    }
    return jsonify(r)


@web.route("/classic/<int:type>/<int:id>/favor", methods=['GET'])
def like_status(type, id):
    r = {
        "fav_nums": 1,
        "id": 1,
        "like_status": 1
    }
    return jsonify(r)


@web.route("/book/hot_list", methods=['GET'])
def hot_list():
    r = [
        {
            "author": "陈儒",
            "fav_nums": 0,
            "id": 1,
            "image": "https://img3.doubanio.com/lpic/s3435132.jpg",
            "like_status": 0,
            "title": "Python源码剖析"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 2,
            "image": "https://img3.doubanio.com/lpic/s29631790.jpg",
            "like_status": 0,
            "title": "Dive Into Python"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 3,
            "image": "https://img3.doubanio.com/lpic/s4059293.jpg",
            "like_status": 0,
            "title": "Dive Into Python 3"
        },
        {
            "author": "陈儒",
            "fav_nums": 0,
            "id": 4,
            "image": "https://img3.doubanio.com/lpic/s3435132.jpg",
            "like_status": 0,
            "title": "Python源码剖析"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 5,
            "image": "https://img3.doubanio.com/lpic/s29631790.jpg",
            "like_status": 0,
            "title": "Dive Into Python"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 6,
            "image": "https://img3.doubanio.com/lpic/s4059293.jpg",
            "like_status": 0,
            "title": "Dive Into Python 3"
        },
        {
            "author": "陈儒",
            "fav_nums": 0,
            "id": 7,
            "image": "https://img3.doubanio.com/lpic/s3435132.jpg",
            "like_status": 0,
            "title": "Python源码剖析"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 8,
            "image": "https://img3.doubanio.com/lpic/s29631790.jpg",
            "like_status": 0,
            "title": "Dive Into Python"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 9,
            "image": "https://img3.doubanio.com/lpic/s4059293.jpg",
            "like_status": 0,
            "title": "Dive Into Python 3"
        },
        {
            "author": "陈儒",
            "fav_nums": 0,
            "id": 10,
            "image": "https://img3.doubanio.com/lpic/s3435132.jpg",
            "like_status": 0,
            "title": "Python源码剖析"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 11,
            "image": "https://img3.doubanio.com/lpic/s29631790.jpg",
            "like_status": 0,
            "title": "Dive Into Python"
        },
        {
            "author": "MarkPilgrim",
            "fav_nums": 0,
            "id": 12,
            "image": "https://img3.doubanio.com/lpic/s4059293.jpg",
            "like_status": 0,
            "title": "Dive Into Python 3"
        },
    ]
    return jsonify(r)


@web.route("/book/favor/count", methods=['GET'])
def favor_count():
    r = {
        "count": 10,
    }
    return jsonify(r)


@web.route("/book/<int:book_id>/detail", methods=['GET'])
def get_book_detail(book_id):
    r = {
        "author": [
            "Wolfgang Mauerer"
        ],
        "binding": "平装",
        "category": "算法",
        "id": 6980,
        "image": "https://img1.doubanio.com/lpic/s4368169.jpg",
        "images": {
            "large": "https://img1.doubanio.com/lpic/s4368169.jpg"
        },
        "isbn": "9787115227430",
        "pages": "1038",
        "price": "149.00元",
        "pubdate": "201005",
        "publisher": "人民邮电出版社",
        "subtitle": "全球开源社区集体智慧结晶，领略Linux内核的绝美风光",
        "summary": "众所周知，Linux操作系统的源代码复杂、文档少，对程序员的要求高，要想看懂这些代码并不是一件容易事...\n众所周知，Linux"
                   "操作系统的源代码复杂、文档少，对程序员的要求高，要想看懂这些代码并不是一件容易事...\n众所周知，Linux"
                   "操作系统的源代码复杂、文档少，对程序员的要求高，要想看懂这些代码并不是一件容易事...\n众所周知，Linux"
                   "操作系统的源代码复杂、文档少，对程序员的要求高，要想看懂这些代码并不是一件容易事...",
        "title": "深入Linux内核架构",
        "translator": [
            "郭旭"
        ]
    }
    return jsonify(r)


@web.route("/book/<int:book_id>/favor", methods=['GET'])
def book_favor(book_id):
    r = {
        "fav_nums": 8,
        "id": 1,
        "like_status": 1
    }
    return jsonify(r)


@web.route("/book/<int:book_id>/short_comment", methods=['GET'])
def book_comment(book_id):
    r = {
        "comment":
            [

            ],
        "book_id": 1
    }
    return jsonify(r)


@web.route("/book/add/short_comment", methods=['POST'])
def add_short_comment():
    r = {
        "error_code": 0,
        "msg": "ok",
        "request": "POST  /book/add_short_comment"
    }
    return jsonify(r)

