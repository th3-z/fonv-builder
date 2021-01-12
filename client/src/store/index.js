import Vue from 'vue'
import Vuex from 'vuex'

import player from './modules/player'
import traits from './modules/traits'
import perks from './modules/perks'
import books from './modules/books'
import implants from './modules/implants'
import skills from './modules/skills'
import specials from './modules/specials'

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
    books,
    implants,
    skills,
    specials
  }
})
