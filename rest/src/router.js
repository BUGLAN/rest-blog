import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'

import Detail from './views/Detail'
import Editor from './views/Editor'
import Axis from './views/Axis'
import Manage from './views/Manage'
import BasicManage from './views/BasicManage'
import Login from './views/Login'

import NewTag from './components/NewTag'
import EditorCategory from './components/EditorCategory'
import EditorTag from './components/EditorTag'
import NavArticles from './components/NavArticles'
import NavContent from './components/NavContent'
import NewArticle from './components/NewArticle'
import NewCategory from './components/NewCategory'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home,
      children: [
        {
          path: '',
          component: NavArticles
        }
      ]
    },
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/article',
      component: Detail,
      children: [
        {
          path: ':date/:name',
          component: NavContent
        },
        {
          path: ':date/:name/editor',
          component: Editor
        }

      ]
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/axis',
      component: Axis
    },
    {
      path: '/manage',
      component: BasicManage,
      children: [
        {
          path: '',
          component: Manage
        },
        {
          path: 'category/:name/editor',
          component: EditorCategory
        },
        {
          path: 'tag/:name/editor',
          component: EditorTag
        },
        {
          path: 'test',
          component: { template: '<p>test</p>' }
        }
      ]
    },
    {
      path: '/new_article',
      component: NewArticle
    },
    {
      path: '/new_category',
      component: NewCategory
    },
    {
      path: '/new_tag',
      component: NewTag
    },
    {
      path: '/login',
      component: Login
    }
  ]
})
