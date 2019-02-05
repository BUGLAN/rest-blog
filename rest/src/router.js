import Vue from 'vue'
import Router from 'vue-router'

// import Home from './views/Home.vue'
// import About from './views/About.vue'
// import Detail from './views/Detail'
// import Editor from './views/Editor'
// import Axis from './views/Axis'
// import Manage from './views/Manage'
// import BasicManage from './views/BasicManage'
// import Login from './views/Login'

// import NewTag from './components/NewTag'
// import EditorCategory from './components/EditorCategory'
// import EditorTag from './components/EditorTag'
// import NavArticles from './components/NavArticles'
// import NavContent from './components/NavContent'
// import NewArticle from './components/NewArticle'
// import NewCategory from './components/NewCategory'

function loadView (view) {
  return () => import(/* webpackChunkName: "view-[request]" */ `@/views/${view}.vue`)
}

function loadComponent (component) {
  return () => import(/* webpackChunkName: "component-[request]" */ `@/components/${component}.vue`)
}

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: loadView('Home'),
      children: [
        {
          path: '',
          component: loadComponent('NavArticles')
        }
      ]
    },
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/article',
      component: loadView('Detail'),
      children: [
        {
          path: ':date/:name',
          component: loadComponent('NavContent')
        },
        {
          path: ':date/:name/editor',
          component: loadView('Editor')
        }

      ]
    },
    {
      path: '/about',
      component: loadView('About')
    },
    {
      path: '/axis',
      component: loadView('Axis')
    },
    {
      path: '/manage',
      component: loadView('BasicManage'),
      children: [
        {
          path: '',
          component: loadView('Manage')
        },
        {
          path: 'category/:name/editor',
          component: loadComponent('EditorCategory')
        },
        {
          path: 'tag/:name/editor',
          component: loadComponent('EditorTag')
        },
        {
          path: 'test',
          component: { template: '<p>test</p>' }
        }
      ]
    },
    {
      path: '/new_article',
      component: loadComponent('NewArticle')
    },
    {
      path: '/new_category',
      component: loadComponent('NewCategory')
    },
    {
      path: '/new_tag',
      component: loadComponent('NewTag')
    },
    {
      path: '/login',
      component: loadView('Login')
    }
  ]
})
