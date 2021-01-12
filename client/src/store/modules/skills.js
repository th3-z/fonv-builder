import axios from 'axios';

const state = {
    skills: []
};

const getters = {
    skills: (state) => state.skills,
    getSkill: (state) => (skill_id) => state.skills.find(skill => skill.id == skill_id)
};

const actions = {
    async loadSkills({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/skills");
        commit('setSkills', response.data.skills);
    },
};

const mutations = {
    setSkills: (state, skills) => (state.skills = skills)
};

export default {
    mutations,
    actions,
    state,
    getters
}