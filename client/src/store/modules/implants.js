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

    addImplant({ commit, rootState }, payload) {
        commit('addImplantGeneric', {
            player: rootState.player.player,
            implant_id: payload.implantId,
            level: payload.level
        });
    },

    setImplantLevel({ commit, rootState }, payload) {
        commit('setImplantLevel', {
            player: rootState.player.player,
            implant_id: payload.implantId,
            level: payload.level
        })
    },

    removeImplant({commit, rootState}, implantId) {
        commit('removeImplantGeneric', {
            player: rootState.player.player,
            implant_id: implantId
        });
    }
};

const mutations = {
    setImplants: (state, implants) => (state.implants = implants),

    addImplantGeneric(state, payload) {
        payload.player.implants.push({
            id: payload.implant_id,
            level: payload.level
        });
    },

    setImplantLevel(state, payload) {
        payload.player.implants.find(
            implant => implant.id === payload.implant_id
        ).level = payload.level
    },

    removeImplantGeneric(state, payload) {
        payload.player.implants.splice(
            payload.player.implants.findIndex(implant => implant.id === payload.implant_id),
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