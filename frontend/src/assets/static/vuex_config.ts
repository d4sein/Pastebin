import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist'

Vue.use(Vuex)

const vuexLocalStorage = new VuexPersist({
  key: 'vuex',
  storage: window.localStorage
})

const state: any = new Vuex.Store({
  state: {
    token: null
  },
  mutations: {
    addToken (state: any, token: any): void {
      if (typeof token === 'string') {
        state.token = token
      }
    }
  },
  getters: {
    token (state: any): any {
      return state.token
    }
  },
  plugins: [vuexLocalStorage.plugin]
})

export default state
