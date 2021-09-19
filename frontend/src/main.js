import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Vuex from 'vuex'

Vue.config.productionTip = false

Vue.use(Vuex)

const coreModule = {
    state: () => ({
        loggedIn: false,
        currentUser: null,
        language: 'en',
    }),
  }

const birthdayModule = {
    state: () => ({
        birthdayList: []
    })
}
  
  const store = new Vuex.Store({
    modules: {
      core: coreModule,
      birthday: birthdayModule
    }
  })

new Vue({
  router,
  store: store,
  render: function (h) { return h(App) }
}).$mount('#app')
