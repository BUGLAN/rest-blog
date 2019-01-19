import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import setMetaTitle from './setMetaTitle'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import hljs from 'highlight.js'
import 'highlight.js/styles/github.css'

Vue.directive('highlight', function (el) {
  let blocks = el.querySelectorAll('pre code')
  blocks.forEach((block) => {
    hljs.highlightBlock(block)
  })
})

Vue.use(mavonEditor)

Vue.config.productionTip = false
Vue.prototype.$axios = axios

axios.defaults.baseURL = process.env.VUE_APP_API_HOST

Vue.directive('title', {
  inserted: function (el, binding) {
    setMetaTitle(binding.value)
  }
})

Vue.prototype.setCookie = (Cname, value, expiredays) => {
  var exdate = new Date()
  exdate.setDate(exdate.getDate() + expiredays)
  document.cookie = Cname + '=' + escape(value) + ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString())
}

function getCookie (name) {
  var arr
  var reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)')
  if (arr === document.cookie.match(reg)) {
    return (arr[2])
  } else { return null }
}

Vue.prototype.getCookie = getCookie
// axios 拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      if (error.response.status === 401) {
        // store.commit(types.LOGOUT);
        router.replace({
          path: '/login',
          query: {
            redirect: router.currentRoute.fullPath
          }
        })
      }
    }
    return Promise.reject(error.response.data) // 返回接口返回的错误信息
  }
)

new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
