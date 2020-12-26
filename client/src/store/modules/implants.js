import axios from 'axios';

const state = {
    implants: {}
};

const getters = {
    implants: (state) => state.implants
};

const actions = {
    async loadImplants({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/implants");
        commit('setImplants', response.data.implants);
    },

    addImplant({ commit, rootState }, implantId) {
        commit('addImplantGeneric', {
            player: rootState.player.player,
            implant_id: implantId
        });
    },

    removeImplant({commit, rootState}, implantId) {
        commit('removeImplantGeneric', {
            player: rootState.player.player,
            implant_id: implantId
        });
    }
};

const mutations = {
    setImplants: (state, implants) => (state.impalnts = implants),

    addImplantGeneric(state, payload) {
        payload.player.implants.push(payload.implant_id);
    },

    removeImplantGeneric(state, payload) {
        payload.player.implants.splice(
            payload.player.implants.indexOf(payload.implant_id),
            1
        );
    },
};

export default {
    state,
    getters,
    mutations,
    actions
}