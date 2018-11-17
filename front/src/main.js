import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = true

export const serverBus = new Vue();

var app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
