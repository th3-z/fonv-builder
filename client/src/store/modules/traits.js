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

    addTrait ({ commit, rootState }, traitId) {
        switch (traitId) {
            case 'four_eyes':
                commit('addFourEyes', rootState.player.player);
                break;
            case 'good_natured':
                commit('addGoodNatured', rootState.player.player);
                break;
            default:
                // built_to_destroy
                // fast_shot
                // heavy_handed
                // kamikaze
                // loose_cannon
                // trigger_discipline
                // wild_wasteland
                commit('addTraitGeneric', {
                    player: rootState.player.player,
                    trait_id: traitId
                })
                break;
        }
    },
};

const mutations = {
    setTraits: (state, traits) => (state.traits = traits),

    addTraitGeneric({ rootState}, payload) {
        console.log(payload);
        rootState.player.player.traits.push(payload.trait_id);
    },

    addFourEyes(state, player) {
        player.base_specials.perception -= 1;
        player.special_points -= 1
        player.traits.push("four_eyes");
    },

    addSmallFrame(state, player) {
        player.base_specials.agility += 1;
        player.special_points += 1
        player.traits.push("small_frame");
    },

    addGoodNatured(state, player) {
        player.base_skills.speech += 5;
        player.base_skills.medicine += 5;
        player.base_skills.science += 5;
        player.base_skills.barter += 5;
        player.base_skills.repair += 5;

        player.base_skills.energy_weapons -= 5;
        player.base_skills.explosives -= 5;
        player.base_skills.guns -= 5;
        player.base_skills.melee_weapons -= 5;
        player.base_skills.unarmed -= 5;

        player.traits.push("good_natured");
    },
};

export default {
    state,
    getters,
    mutations,
    actions
}