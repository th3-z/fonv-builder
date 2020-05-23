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
                });
                break;
        }
    },

    removeTrait({commit, rootState}, traitId) {
        switch (traitId) {
            case 'four_eyes':
                commit('removeFourEyes', rootState.player.player);
                break;
            case 'good_natured':
                commit('removeGoodNatured', rootState.player.player);
                break;
            default:
                // built_to_destroy
                // fast_shot
                // heavy_handed
                // kamikaze
                // loose_cannon
                // trigger_discipline
                // wild_wasteland
                commit('removeTraitGeneric', {
                    player: rootState.player.player,
                    trait_id: traitId
                });
                break;
        }
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

    addFourEyes(state, player) {
        player.base_specials.perception -= 1;
        player.special_points -= 1
        player.traits.push("four_eyes");
    },

    removeFourEyes(state, player) {
        player.base_specials.perception += 1;
        player.special_points += 1
        player.traits.splice(player.traits.indexOf("four_eyes"), 1);
    },

    addSmallFrame(state, player) {
        player.base_specials.agility += 1;
        player.special_points += 1
        player.traits.push("small_frame");
    },

    removeSmallFrame(state, player) {
        player.base_specials.agility -= 1;
        player.special_points -= 1
        player.traits.splice(player.traits.indexOf("small_frame "), 1);
    },

    addGoodNatured(state, player) {
        player.base_skills.speech.value += 5;
        player.base_skills.medicine.value += 5;
        player.base_skills.science.value += 5;
        player.base_skills.barter.value += 5;
        player.base_skills.repair.value += 5;

        player.base_skills.energy_weapons.value -= 5;
        player.base_skills.explosives.value -= 5;
        player.base_skills.guns.value -= 5;
        player.base_skills.melee_weapons.value -= 5;
        player.base_skills.unarmed.value -= 5;

        player.traits.push("good_natured");
    },

    removeGoodNatured(state, player) {
        player.base_skills.speech.value -= 5;
        player.base_skills.medicine.value -= 5;
        player.base_skills.science.value -= 5;
        player.base_skills.barter.value -= 5;
        player.base_skills.repair.value -= 5;

        player.base_skills.energy_weapons.value += 5;
        player.base_skills.explosives.value += 5;
        player.base_skills.guns.value += 5;
        player.base_skills.melee_weapons.value += 5;
        player.base_skills.unarmed.value += 5;

        player.traits.splice(player.traits.indexOf("small_frame "), 1);
    },
};

export default {
    state,
    getters,
    mutations,
    actions
}