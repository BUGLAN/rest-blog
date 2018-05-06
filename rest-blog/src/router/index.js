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
      path: '/article', // 2018-5-6/我的一次flask的路程
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
    }
  ]
})
