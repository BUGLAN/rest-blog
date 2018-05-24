import unittest
import json
from blog import create_app
from config import TestConfig
from extand import db
from blog.models import Article, Category, Tag, User


class TestApi(unittest.TestCase):
    url = 'http://127.0.0.1:5000/api'

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        tag = Tag()
        tag.name = 'tagx'
        db.session.add(tag)
        category = Category()
        category.name = 'categoryx'
        db.session.add(category)
        db.session.commit()
        article = Article()
        article.title = 'articlex'
        article.slug = 'slugx'
        article.category = category
        article.content = 'contentx'
        article.tags = [tag]
        db.session.add(category)
        db.session.commit()
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()

    def get_token(self):
        r = self.client.post(
                self.url + '/login',
                data=json.dumps({
                    'username': 'admin',
                    'password': '123456'
                    }), content_type='application/json'
                )
        return json.loads(r.get_data(as_text=True))['token']


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

        tag = Tag()
        tag.name = 'tag'
        db.session.add(tag)
        category = Category()
        category.name = 'category'
        db.session.add(category)
        db.session.commit()
        article = Article()
        article.title = 'article'
        article.slug = 'slug'
        article.category = category
        article.content = 'content'
        article.tags = [tag]
        db.session.add(category)
        db.session.commit()
        r = self.client.get(self.url + '/article?slug=slug')
        self.assertEqual(r.status_code, 200)

    def test_article_post(self):
        r = self.client.post(self.url + '/article', headers={"Authorization": "Bearer {}".format(self.get_token())})
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
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
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
            content_type='application/json',  headers={"Authorization": "Bearer {}".format(self.get_token())})
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
            content_type='application/json',  headers={"Authorization": "Bearer {}".format(self.get_token())})
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
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
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
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
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
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue('修改文章成功' in r.get_data(as_text=True))
        self.assertTrue(Article.query.get(1).title == 'title')
        self.assertTrue(Article.query.get(1).slug == 'slug2')
        self.assertTrue(Article.query.get(1).content == 'context' * 20)
        self.assertTrue(Article.query.get(1).category is None)
        self.assertTrue(len(Article.query.get(1).tags.all()) == 1)

    def test_article_delete(self):
        r = self.client.delete(self.url + '/article?id=2')
        self.assertEqual(r.status_code, 401)
        r = self.client.post(
            self.url + '/article',
            data=json.dumps({
                'title': 'article-title',
                'slug': 'slug',
                'content': 'content ' * 20,
                'category_id': 1,
                'tag_ids': [1],
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        r = self.client.delete(self.url + '/article?id=2', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue('删除文章成功' in r.get_data(as_text=True))

    def test_category_get(self):
        r = self.client.get(self.url + '/category?name=a')
        self.assertEqual(r.status_code, 404)
        category = Category()
        category.name = 'a'
        db.session.add(category)
        db.session.commit()
        r = self.client.get(self.url + '/category?name=a')
        self.assertTrue('a' in r.get_data(as_text=True))

    def test_category_post(self):
        r = self.client.post(
            self.url + '/category',
            data=json.dumps({
                'name': 'a',
                'article_ids': []
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(Category.query.get(2).name == 'a')
        r = self.client.post(
            self.url + '/category',
            data=json.dumps({
                'name': 'b',
                'article_ids': []
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertTrue(Category.query.get(2).articles == [])

    def test_category_put(self):
        category = Category()
        category.name = 'a'
        db.session.add(category)
        db.session.commit()
        r = self.client.put(
            self.url + '/category',
            data=json.dumps({
                'id': 1,
                'name': 'b',
                'article_ids': []
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(Category.query.get(1).name == 'b')

    def test_category_delete(self):
        category = Category()
        category.name = 'a'
        db.session.add(category)
        db.session.commit()
        r = self.client.delete(
            self.url + '/category',
            data=json.dumps({
                'id': 1
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(Category.query.get(1) == None)

    def test_tag_get(self):
        r = self.client.get(self.url + '/tag?name=a')
        self.assertEqual(r.status_code, 404)
        tag = Tag()
        tag.name = 'a'
        db.session.add(tag)
        db.session.commit()
        r = self.client.get(self.url + '/tag?name=a')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('a' in r.get_data(as_text=True))

    def test_tag_post(self):
        r = self.client.post(
            self.url + '/tag',
            data=json.dumps({
                'name': 'a',
                'article_ids': []
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        r = self.client.post(
            self.url + '/tag',
            data=json.dumps({
                'name': 'a',
                'article_ids': []
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 400)

    def test_tag_put(self):
        tag = Tag()
        tag.name = 'a'
        db.session.add(tag)
        db.session.commit()
        r = self.client.put(
            self.url + '/tag',
            data=json.dumps({
                'id': 1,
                'name': 'b',
                'article_ids': []
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(Tag.query.get(1).name == 'b')

    def test_tag_delete(self):
        r = self.client.delete(
            self.url + '/tag',
            data=json.dumps({
                'id': 2
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 404)
        tag = Tag()
        tag.name = 'a'
        db.session.add(tag)
        db.session.commit()
        r = self.client.delete(
            self.url + '/tag',
            data=json.dumps({
                'id': 1
            }),
            content_type='application/json', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(Tag.query.get(1) == None)

    def test_articles(self):
        article = Article()
        article.title = 'a'
        article.slug = 'skg'
        article.content = 'content xxx'
        db.session.add(article)
        db.session.commit()
        r = self.client.get(self.url + '/articles?page=1', )
        self.assertEqual(r.status_code, 200)
        r = self.client.get(self.url + '/articles?page=-1', )
        self.assertEqual(r.status_code, 404)

    def test_categories(self):
        category = Category()
        category.name = 'c'
        category.articles = [Article.query.get(1)]
        db.session.add(category)
        db.session.commit()
        r = self.client.get(self.url + '/categories', )
        self.assertEqual(r.status_code, 200)
        text = r.get_data(as_text=True)
        self.assertTrue('name' in text and 'articles' in text)

    def test_pages(self):
        r = self.client.get(self.url + '/pages')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('[1]' in r.get_data(as_text=True))

    def test_mange(self):
        r = self.client.get(self.url + '/mange', headers={"Authorization": "Bearer {}".format(self.get_token())})
        self.assertEqual(r.status_code, 200)
        text = json.loads(r.get_data(as_text=True))
        self.assertTrue(type(text) == dict)

    def test_login(self):
        r = self.client.post(
                self.url + '/login',
                data=json.dumps({
                    'username': 'admin',
                    'password': '123456'
                    }), content_type='application/json'
                )
        self.assertEqual(r.status_code, 200)
        self.assertTrue('token' in r.get_data(as_text=True))
