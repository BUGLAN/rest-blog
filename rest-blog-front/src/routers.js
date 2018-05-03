import Home from './components/home.vue'

const routers = [
  {
    path: '/',
    component: Home,
    children: [
      {
        path: '/',
        component: Login
      }
    ]
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
    children: [
      {
        path: '/',
        name: 'login',
        component: Login
      },
      {
        path: 'first',
        name: 'first',
        component: First
      }
    ]
  }
]
export default routers
