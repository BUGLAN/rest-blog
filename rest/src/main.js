import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

axios.defaults.baseURL = process.env.VUE_APP_API_HOST

new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
