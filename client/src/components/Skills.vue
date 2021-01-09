<template>
    <div>
        <div v-bind:key="skill.id" v-for="skill in skills">
            <skill v-bind:skill="skill"/>
        </div>
        <p
            v-bind:class="{'error':remainingSkillPoints < 0}"
        >Remaining points: {{remainingSkillPoints}}</p>
        <p
            v-bind:class="{'error':remainingTags < 0}"
        >Remaining tags: {{remainingTags}}</p>
        <p v-if="hasComprehension()">
            <em>Assumes skill books are consumed after taking comprehension.</em>
        </p>
    </div>
</template>

<script>
import Skill from './Skill.vue'
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
    name: "Skills",
    components: {
        Skill
    },
    computed: {
        ...mapGetters(['player']),
        remainingSkillPoints() {
            const baseSkillPoints = this.player.skill_points;

            // find int implant

            // find intense trainings for int

            let earnedSkillPoints = 
                (this.player.level -  1)  // No points are earned for level 1
                * (10 + this.player.base_specials.intelligence*0.5);

            let skillsTotal = 0;
            for(let skill in this.player.base_skills) {
                skillsTotal += this.player.base_skills[skill].value;
            }

            

            return Math.floor((baseSkillPoints+earnedSkillPoints) - skillsTotal);
        },
        remainingTags() {
            const hasTag = this.player.perks.includes("tag");
            let remainingTags = 3 + (hasTag? 1: 0);

            for(let skill in this.player.base_skills) {
                if (this.player.base_skills[skill].tagged) {
                    remainingTags -= 1;
                }
            }

            return remainingTags;
        }
    },
    data() {
        return {
            skills: []
        }
    },
    methods: {
        hasComprehension() {
            if (this.player.perks.find(perk => perk.id == "comprehension")) {
                return true
            }
            return false
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
    .error {
        color: red;
    }
</style>