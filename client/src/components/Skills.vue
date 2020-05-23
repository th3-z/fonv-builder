<template>
    <div>
        <div v-bind:key="skill.id" v-for="skill in skills">
            <skill v-bind:skill="skill"/>
        </div>
    </div>
</template>

<script>
import Skill from './Skill.vue'
import axios from 'axios';
// import computedStats from './lib/skills.js'; // move down into skill

export default {
    name: "Skills",
    components: {
        Skill
    },
    data() {
        return {
            skills: []
        }
    },
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/skills")
            .then(res => this.skills = res.data.skills)
            .catch(err => console.log(err));
    }
}
</script>

<style scoped>

</style>