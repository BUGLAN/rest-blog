import unittest
import json
from blog import create_app
from config import TestConfig
from extand import db
from blog.models import Article


class TestApi(unittest.TestCase):
    url = 'http://127.0.0.1:5000/api'

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_article_get(self):
        r = self.client.get(self.url + '/article')
        self.assertEqual(r.status_code, 400)
        article = Article()
        article.title = 'title-test'
        article.slug = 'test'
        article.content = 'content ' * 20
        db.session.add(article)
        db.session.commit()
        r = self.client.get(self.url + '/article?slug=test')
        text = r.get_data(as_text=True)
        self.assertEqual(r.status_code, 200)
        self.assertTrue('title-test' in text and 'test' in text
                        and 'content' in text)

    def test_article_post(self):
        r = self.client.post(self.url + '/article')
        self.assertEqual(r.status_code, 400)
        r = self.client.post(
            self.url + '/article',
            data=json.dumps({
                'title': 'article-title',
                'slug': 'slug',
                'content': 'content ' * 20,
                'category_id': 1,
                'tag_ids': [1],
            }),
            content_type='application/json')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('新建文章成功' in r.get_data(as_text=True))
        r = self.client.post(
            self.url + '/article',
            data=json.dumps({
                'title': 'article-title',
                'slug': 'slug',
                'content': 'content ' * 20,
                'category_id': 1,
                'tag_ids': [1],
            }),
            content_type='application/json')
        self.assertEqual(r.status_code, 400)
        self.assertTrue('字段冲突' in r.get_data(as_text=True))
        r = self.client.post(
            self.url + '/article',
            data=json.dumps({
                'title': 'article-titlex',
                'slug': 'slug',
                'content': 'content ' * 20,
                'category_id': 1,
                'tag_ids': [1],
            }),
            content_type='application/json')
        self.assertEqual(r.status_code, 400)
        self.assertTrue('字段冲突' in r.get_data(as_text=True))

    def test_article_put(self):
        r = self.client.post(
            self.url + '/article',
            data=json.dumps({
                'title': 'article-title',
                'slug': 'slug',
                'content': 'content ' * 20,
                'category_id': 1,
                'tag_ids': [1],
            }),
            content_type='application/json')
        r = self.client.put(
            self.url + '/article',
            data=json.dumps({
                'id': 1,
                'title': 'title',
                'slug': 'slug2',
                'content': 'context' * 20,
                'category_id': 2,
                'tag_ids': [1]
            }),
            content_type='application/json')
        self.assertEqual(r.status_code, 200)
        article = Article()
        article.title = 'x'
        article.slug = 'y'
        article.conten = 'z' * 20
        db.session.add(article)
        db.session.commit()
        r = self.client.put(
            self.url + '/article',
            data=json.dumps({
                'id': 1,
                'title': 'title',
                'slug': 'slug2',
                'content': 'context' * 20,
                'category_id': 2,
                'tag_ids': [1]
            }),
            content_type='application/json')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('修改文章成功' in r.get_data(as_text=True))
        self.assertTrue(Article.query.get(1).title == 'title')
        self.assertTrue(Article.query.get(1).slug == 'slug2')
        self.assertTrue(Article.query.get(1).content == 'context' * 20)
        self.assertTrue(Article.query.get(1).category is None)
        self.assertTrue(Article.query.get(1).tags.all() == [])

    def test_article_delete(self):
        r = self.client.delete(self.url + '/article?id=1')
        self.assertEqual(r.status_code, 404)
        r = self.client.post(
            self.url + '/article',
            data=json.dumps({
                'title': 'article-title',
                'slug': 'slug',
                'content': 'content ' * 20,
                'category_id': 1,
                'tag_ids': [1],
            }),
            content_type='application/json')
        self.assertEqual(r.status_code, 200)
        r = self.client.delete(self.url + '/article?id=1')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('删除文章成功' in r.get_data(as_text=True))
