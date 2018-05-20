import json
import unittest

from extand import db
from blog import create_app
from config import TestConfig
from blog.models import Article, Category, Tag, User


class TestApi(unittest.TestCase):
    	
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
	
    def test_articles(self):
        """
        test function get_articles
        """
        r = self.client.get('http://127.0.0.1:5000/api/articles')
        self.assertTrue('articles' in r.get_data(as_text=True))
        self.assertEqual(r.status_code, 200)
        self.assertTrue('[]' in r.get_data(as_text=True))
        article = Article()
        article.title = 'vim-test-article'
        article.slug = 'vim-article'
        article.content = 'test' * 50
        db.session.add(article)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/articles')
        text = r.get_data(as_text=True)
        self.assertTrue('articles' in text)
        self.assertTrue('vim-article' in text)
        self.assertTrue('testtest' in text)
    
    def test_articles_404(self):
        """
        test function get_articles 404
        """
        r = self.client.get('http://127.0.0.1:5000/api/articles?page=2')
        self.assertTrue('[]' in r.get_data(as_text=True))
        # should 404

    def test_article(self):
        """
        test function get_article
        """
        article = Article()
        article.title = 'slug'
        article.slug = 'test-slug'
        # need test slug
        article.content = 'test' * 200
        db.session.add(article)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/article?slug=test-slug')
        text = r.get_data(as_text=True)
        self.assertTrue('slug' in text)
        r = self.client.get('http://127.0.0.1:5000/api/article?slug=testslug')
        self.assertTrue(r.status_code == 400)
        self.assertTrue('{"status":400}' in  r.get_data(as_text=True))

    def test_article_put(self):
        """
        test function article_operation the put method
        """
        category = Category()
        category.name = 'c1'
        db.session.add(category)
        db.session.commit()

        article = Article()
        article.title = 'slug'
        article.slug = 'test-slug'
        article.content = 'test' * 200
        article.category = category
        db.session.add(article)
        db.session.commit()
        
        category = Category()
        category.name = 'c2'
        db.session.add(category)
        db.session.commit()

        tag = Tag()
        tag.name = 'tag1'
        tag.article = [article]
        db.session.add(tag)
        db.session.commit()

        r = self.client.put('http://127.0.0.1:5000/api/article_operation', data=json.dumps({
            "id": 1,
            "title": "slug1", 
            "slug": "test-slug-1", 
            "content": "xxx" * 20, 
            "category": 2, 
            "tags": [1]}), content_type='application/json')

        self.assertTrue('success' in r.get_data(as_text=True))
        self.assertTrue('c2' == article.category.name)
        self.assertTrue(tag in article.tags)
        self.assertTrue('xxx' in article.content)
        

    def test_articles_delete(self):
        """
        test function article_operation the delete method
        """
        article = Article()
        article.title = 'slug'
        article.slug = 'test-slug'
        article.content = 'test' * 200
        db.session.add(article)
        db.session.commit()

        r = self.client.delete('http://127.0.0.1:5000/api/article_operation?id=1')
        self.assertTrue([] == Article.query.all())

    def test_pages(self):
        for i in range(100):
            article = Article()
            article.title = 'test-range-' + str(i)
            article.slug = 'range-' + str(i)
            article.content = 'xxx' * i
            db.session.add(article)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/pages')
        self.assertTrue('10' in r.get_data(as_text=True))

    def test_categories(self):
        category = Category()
        category.name = 'a'
        category1 = Category()
        category1.name = 'b'
        category2 = Category()
        category2.name = 'c'
        db.session.add(category)
        db.session.add(category1)
        db.session.add(category2)
        db.session.commit()

        r = self.client.get('http://127.0.0.1:5000/api/categories')
        text = r.get_data(as_text=True)
        self.assertTrue('a' in text and 'b' in text and 'c' in text)
    
    def test_login(self):
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()
        r = self.client.post('http://127.0.0.1:5000/api/login',
                data=json.dumps({"username": "admin", "password": "123456"}),
                content_type="application/json")
        json_text = json.loads(r.get_data(as_text=True))
        self.assertTrue('token' in json_text)
        
    def get_token(self, username, password):
        r = self.client.post('http://127.0.0.1:5000/api/login',
                data=json.dumps({"username": "admin", "password": "123456"}),
                content_type="application/json")
        json_text = json.loads(r.get_data(as_text=True))
        token = json_text['token']
        return {
                "Authorization": "Bearer " + token,
                "Accept": "application/json",
                "Content-Type": "application/json"
                }

    def test_manage(self):
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/manage',
                headers=self.get_token('admin', '123456'))

        self.assertTrue(200 == r.status_code)
        self.assertTrue('[]' in r.get_data(as_text=True))
        category = Category()
        category.name = 'c'
        db.session.add(category)

        article = Article()
        article.title = 'a'
        article.content = 'article' * 20
        tag = Tag()
        tag.name = 't'
        db.session.add(tag)
        db.session.add(article)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/manage',
                headers=self.get_token('admin', '123456'))
        text = r.get_data(as_text=True)
        self.assertTrue('a' in text and 'c' in text and 't' in text)
        text_json = json.loads(text)
        self.assertTrue(type(text_json) == dict)
        
    def test_article_title(self):
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()

        article = Article()
        article.name = 'a'
        article.title = 'title'
        db.session.add(article)
        db.session.commit()

        r = self.client.get('http://127.0.0.1:5000/api/article_titles',
                headers=self.get_token('admin', '123456'))
        self.assertEqual(r.status_code, 200)
        text = r.get_data(as_text=True)
        self.assertTrue('a' in text and '1' in text and 'title' in text)
        
    def test_category_titles(self):
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()

        r = self.client.get('http://127.0.0.1:5000/api/category_titles',
                headers=self.get_token('admin', '123456'))
        self.assertTrue('[]' in r.get_data(as_text=True))

        category = Category()
        category.name = 'c'
        db.session.add(category)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/category_titles',
                headers=self.get_token('admin', '123456'))
        text = r.get_data(as_text=True)
        self.assertTrue('1' in text and 'c' in text)
        
    def test_tag_titles(self):
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()

        r = self.client.get('http://127.0.0.1:5000/api/tag_titles',
                headers=self.get_token('admin', '123456'))
        self.assertTrue('[]' in r.get_data(as_text=True))

        tag = Tag()
        tag.name = 't'
        db.session.add(tag)
        db.session.commit()
        r = self.client.get('http://127.0.0.1:5000/api/tag_titles',
                headers=self.get_token('admin', '123456'))
        text = r.get_data(as_text=True)
        self.assertTrue('1' in text and 't' in text)

    def test_new_category(self):
        r = self.client.post('http://127.0.1:5000/api/new_category')
        self.assertEqual(r.status_code, 401)
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()

        r = self.client.post('http://127.0.0.1:5000/api/new_category', data=json.dumps({
            "catgeory": "a"}),
            content_type='application/json',
            headers=self.get_token('admin', '123456'))
        self.assertEqual(r.status_code, 404)
        self.assertTrue('404' in r.get_data(as_text=True))

        article = Article()
        article.title = 'article'
        article.content = 'text' * 10
        db.session.add(article)
        db.session.commit()

        r = self.client.post('http://127.0.0.1:5000/api/new_category',
                data=json.dumps({
                    "category": "a",
                    "articles": [1]}),
                content_type='application/json',
                headers=self.get_token('admin', '123456'))
        self.assertTrue(200, r.status_code)
        category = Category.query.get(1)
        self.assertTrue(category.name == 'a')
        
    def test_new_tag(self):
        r = self.client.post('http://127.0.0.1:5000/api/new_tag')
        self.assertEqual(401, r.status_code)
        user = User()
        user.name = 'admin'
        user.password = '123456'
        db.session.add(user)
        db.session.commit()
        article = Article()
        article.title = 'article'
        article.content = 'article' * 10
        db.session.add(article)
        db.session.commit()
        r = self.client.post('http://127.0.0.1:5000/api/new_tag',
                data=json.dumps({"tag": "t"}),
                headers=self.get_token('admin', '123456'),
                content_type='application/json')
        self.assertTrue(404, r.status_code)
        r = self.client.post('http://127.0.0.1:5000/api/new_tag',
                data=json.dumps({"tag": "t", "articles": [1]}),
                headers=self.get_token('admin', '123456'),
                content_type='application/json')
        self.assertTrue(article.tags[0].name == 't') 

    def test_new_article(self):
        # i will change this api 
        pass
        
    def test_upload_image(self):
        # i will change this api
        pass

    def other_api(self):
        # this is api must be change
        pass



                    
        

        
        
        






















if __name__ == '__main__':
    unittest.main()
