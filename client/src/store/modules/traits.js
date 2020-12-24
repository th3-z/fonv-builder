import axios from 'axios';

const state = {
    traits: {}
};

const getters = {
    traits: (state) => state.traits
};

const actions = {
    async loadTraits({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/traits");
        commit('setTraits', response.data.traits);
    },

    addTrait({ commit, rootState }, traitId) {
        commit('addTraitGeneric', {
            player: rootState.player.player,
            trait_id: traitId
        });
    },

    removeTrait({commit, rootState}, traitId) {
        commit('removeTraitGeneric', {
            player: rootState.player.player,
            trait_id: traitId
        });
    }
};

const mutations = {
    setTraits: (state, traits) => (state.traits = traits),

    addTraitGeneric(state, payload) {
        payload.player.traits.push(payload.trait_id);
    },

    removeTraitGeneric(state, payload) {
        payload.player.traits.splice(
            payload.player.traits.indexOf(payload.trait_id),
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