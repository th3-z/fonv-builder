import Vue from 'vue'
import PortalVue from 'portal-vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import App from './App.vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import store from './store'

Vue.config.productionTip = false

Vue.use(PortalVue)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)


new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
