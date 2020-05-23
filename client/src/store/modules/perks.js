const actions = {
    addPerk ({ commit, rootState }, perkId) {
        switch (perkId) {
            case 'some_perk':
                break;
            default:
                commit('addPerk', rootState.player.player)
        }
    },
};

const mutations = {
    addPerk(state, player) {
        console.log(player);
    },
};

export default {
    mutations,
    actions
}