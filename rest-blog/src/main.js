// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'
import App from './App'
import axios from 'axios'
import hljs from 'highlight.js'
import 'highlight.js/styles/github.css'

import Home from '@/components/Home'

import {setMetaTitle} from "./util/setMetaTitle";

Vue.config.productionTip = false
Vue.prototype.$axios = axios

Vue.directive('title', {
  inserted: function (el, binding) {
    setMetaTitle(binding.value)
  }
})

//     something start

//设置cookie
Vue.prototype.setCookie = (c_name, value, expiredays) => {
  var exdate = new Date();
  exdate.setDate(exdate.getDate() + expiredays);
  document.cookie = c_name + "=" + escape(value) + ((expiredays == null) ? "" : ";expires=" + exdate.toGMTString());
}

//获取cookie
function getCookie(name) {
  var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
  if (arr = document.cookie.match(reg))
    return (arr[2]);
  else
    return null;
}


Vue.prototype.getCookie = getCookie;
//删除cookie
Vue.prototype.delCookie = (name) => {
  var exp = new Date();
  exp.setTime(exp.getTime() - 1);
  var cval = getCookie(name);
  if (cval != null)
    document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}
//     something end
Vue.directive('highlight', function (el) {
  let blocks = el.querySelectorAll('pre code');
  blocks.forEach((block) => {
    hljs.highlightBlock(block)
  })
})

// axios 拦截器
axios.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        if (error.response) {
            if (error.response.status == 401) {
                    // store.commit(types.LOGOUT);
                    router.replace({
                        path: '/login',
                        query: {redirect: router.currentRoute.fullPath}
                    })
            }
        }
        return Promise.reject(error.response.data)   // 返回接口返回的错误信息
    }
);




new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>',

})
