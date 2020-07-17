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
                    perk_id: perkId
                });
                break;
        }
    },

    setPerkLevel({commit, rootState}, perkId, level) {
        commit('setPerkLevel', {
            player: rootState.player.player,
            perk_id: perkId,
            level: level
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

    setPerkRank(state, payload) {
        payload.player.perks.find(
            perk => perk.id === payload.perk_id
        ).rank = payload.rank
    },

    addPerkGeneric(state, payload) {
        payload.player.perks.push({
            id: payload.perk_id,
            level: 0,
            rank: 1
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