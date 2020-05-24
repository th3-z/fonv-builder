import axios from 'axios';

const state = {
    player: {
        traits: [],
        perks: []
    }
};

const getters = {
    player: (state) => state.player,

    getBenefits(state, getters, rootState) {
        let benefits = [];
        const traits = rootState.traits.traits;
        const perks = rootState.perks.perks;

        state.player.traits.forEach(function (traitId) {
            let trait = traits.find(function (trait) {
                return trait.id === traitId;    
            });
            
            if (trait) {
                benefits = benefits.concat(trait.effects_benefit);
            }
        });

        state.player.perks.forEach(function (perkId) {
            let perk = perks.find(function (perk) {
                return perk.id === perkId;    
            });
            
            if (perk) {
                benefits = benefits.concat(perk.effects);
            }
        });

        return benefits;
    },

    getPenalties(state, getters, rootState) {
        let penalties = [];
        const traits = rootState.traits.traits;

        state.player.traits.forEach(function (traitId) {
            let trait = traits.find(function (trait) {
                return trait.id === traitId;    
            });
            
            if (trait) {
                penalties = penalties.concat(trait.effects_penalty);
            }
        });

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
