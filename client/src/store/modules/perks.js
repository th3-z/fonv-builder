import axios from 'axios';

const state = {
    perks: {}
};

const getters = {
    perks: (state) => state.perks,
    getPerk: (state) => (perk_id) => state.perks.find(perk => perk.id == perk_id)
};

const actions = {
    async loadPerks({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/perks");
        commit('setPerks', response.data.perks);
    },

    addPerk({ commit, rootState }, payload) {
        commit('addPerkGeneric', {
            player: rootState.player.player,
            perk_id: payload.perkId,
            level: payload.level
        });
    },

    removePerk({commit, rootState}, perkId) {
        commit('removePerkGeneric', {
            player: rootState.player.player,
            perk_id: perkId
        });
    },

    setPerkLevel({commit, rootState}, payload) {
        commit('setPerkLevel', {
            player: rootState.player.player,
            perk_id: payload.perk_id,
            level: payload.level
        });
    }
};

const mutations = {
    setPerks: (state, perks) => (state.perks = perks),

    setPerkLevel(state, payload) {
        payload.player.perks.find(
            perk => perk.id === payload.perk_id
        ).level = payload.level
    },

    addPerkGeneric(state, payload) {
        payload.player.perks.push({
            id: payload.perk_id,
            level: payload.level
        });
    },

    removePerkGeneric(state, payload) {
        payload.player.perks.splice(
            payload.player.perks.findIndex(perk => perk.id === payload.perk_id),
            1
        );
    },
};

export default {
    mutations,
    actions,
    state,
    getters
}