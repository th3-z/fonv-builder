import axios from 'axios';

const state = {
    perks: {}
};

const getters = {
    perks: (state) => state.perks
};

const actions = {
    async loadPerks({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/perks");
        commit('setPerks', response.data.perks);
    },

    addPerk({ commit, rootState }, perkId) {
        switch (perkId) {
            default:
                commit('addPerkGeneric', {
                    player: rootState.player.player,
                    perk_id: perkId
                });
                break;
        }
    },

    removePerk({commit, rootState}, perkId) {
        switch (perkId) {
            default:
                commit('removePerkGeneric', {
                    player: rootState.player.player,
                    trait_id: perkId
                });
                break;
        }
    }
};

const mutations = {
    setPerks: (state, perks) => (state.perks = perks),

    addPerkGeneric(state, payload) {
        payload.player.perks.push(payload.perk_id);
    },

    removePerkGeneric(state, payload) {
        payload.player.perks.splice(
            payload.player.perks.indexOf(payload.perk_id),
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