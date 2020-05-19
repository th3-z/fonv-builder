import Vue from 'vue'
import Vuex from 'vuex'

import player from './modules/player'
import traits from './modules/traits'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    player,
    traits
  }
})
