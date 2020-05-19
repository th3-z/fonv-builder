const actions = {
    addTrait ({ commit, rootState }, traitId) {
        switch (traitId) {
            case 'four_eyes':
                commit('addFourEyes', rootState.player.player);
                break;
        }
    },
};

const mutations = {
    addFourEyes(state, player) {
        console.log(player);
        player.base_specials.perception -= 1;
    },
};

export default {
    mutations,
    actions
}