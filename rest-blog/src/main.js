// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'
import App from './App'
import axios from 'axios'
import hljs  from 'highlight.js'
import 'highlight.js/styles/github.css'

import Home from '@/components/Home'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

Vue.directive('highlight',function (el) {
  let blocks = el.querySelectorAll('pre code');
  blocks.forEach((block)=>{
    hljs.highlightBlock(block)
  })
})


new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>',

})
