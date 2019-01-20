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
Vue.prototype.setCookie = function (name, value, day) {
  if (day !== 0) { // 当设置的时间等于0时，不设置expires属性，cookie在浏览器关闭后删除
    var curDate = new Date()
    var curTamp = curDate.getTime()
    var curWeeHours = new Date(curDate.toLocaleDateString()).getTime() - 1
    var passedTamp = curTamp - curWeeHours
    var leftTamp = 24 * 60 * 60 * 1000 - passedTamp
    var leftTime = new Date()
    leftTime.setTime(leftTamp + curTamp)
    document.cookie = name + '=' + escape(value) + ';expires=' + leftTime.toGMTString()
  } else {
    document.cookie = name + '=' + escape(value)
  }
}

Vue.prototype.getCookie = function (cname) {
  var name = cname + '='
  var ca = document.cookie.split(';')
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i]
    while (c.charAt(0) === ' ') c = c.substring(1)
    if (c.indexOf(name) !== -1) return c.substring(name.length, c.length)
  }
  return ''
}

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
