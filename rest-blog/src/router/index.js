import Vue from 'vue'
import Router from 'vue-router'
import mavonEditor from 'mavon-editor'


import 'mavon-editor/dist/css/index.css'
import NavHeader from '@/components/index/NavHeader'
import NavArticles from '@/components/index/NavArticles'
import NavFooter from '@/components/index/NavFooter'
import Home from '@/components/Home'
import NavContent from '@/components/detail/NavContent'
import Detail from '@/components/Detail'
import About from '@/components/About'
import Editor from '@/components/Editor'
import Axis from '@/components/Axis'
import Manage from '@/components/Manage'
import NewArticle from '@/components/new/NewArticle'
import NewCategory from '@/components/new/NewCategory'
import NewTag from '@/components/new/NewTag'
import EditorCategory from '@/components/editor/EditorCategory'
import BasicManage from '@/components/BasicManage'
import EditorTag from '@/components/editor/EditorTag'
import Login from '@/components/Login'


Vue.use(Router)
Vue.use(mavonEditor)

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
      component: About,
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
          component: {template: '<p>test</p>'}
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
