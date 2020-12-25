import Vue from 'vue'
import Vuex from 'vuex'

import player from './modules/player'
import traits from './modules/traits'
import perks from './modules/perks'
import books from './modules/books'

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
    traits,
    perks,
    books
  }
})
