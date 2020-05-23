import axios from 'axios';

const state = {
    player: {}
};

const getters = {
    player: (state) => state.player,

    getPenalties(state, getters, rootState) {
        let penalties = ["Test"];
        const traits = rootState.traits.traits;

        for (let traitId in state.player.traits) {
            let trait = traits.find(trait => trait.id = traitId);
            penalties = penalties.concat(trait.effects_penalty);
        }

        return penalties;
    }
};

const actions = {
    async newPlayer({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/new_player");
        commit('setPlayer', response.data.new_player);
    },
};

const mutations = {
    setPlayer: (state, player) => (state.player = player),
};

export default {
    state,
    getters,
    actions,
    mutations
};
