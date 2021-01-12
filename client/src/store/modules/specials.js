import axios from 'axios';

const state = {
    specials: []
};

const getters = {
    specials: (state) => state.specials,
    getSpecial: (state) => (special_id) => state.specials.find(special => special.id == special_id)
};

const actions = {
    async loadSpecials({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/specials");
        commit('setSpecials', response.data.specials);
    },
};

const mutations = {
    setSpecials: (state, specials) => (state.specials = specials)
};

export default {
    mutations,
    actions,
    state,
    getters
}