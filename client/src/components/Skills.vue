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

export default {
    name: "Skills",
    components: {
        Skill
    },
    computed: {
        ...mapGetters(['player', 'skills']),
        remainingSkillPoints() {
            const baseSkillPoints = this.player.skill_points;

            // find int implant
            const intImplant = this.player.implants.find(implant => implant.id == "intelligence_implant")

            // find intense trainings for int
            const intTrainings = this.player.perks.filter(
                perk => perk.id.substring(0,16) == "intense_training" && perk.special == "intelligence"
            )

            // find educated
            const educatedPerk = this.player.perks.find(perk => perk.id == "educated")

            let earnedSkillPoints = 0

            for (let level = 2; level <= this.player.level; level++) {
                let intAtLevel = this.player.base_specials.intelligence
                intAtLevel += intTrainings.filter(intTraining => intTraining.level < level).length
                intAtLevel += intImplant? (intImplant.level < level? 1: 0): 0
                intAtLevel = Math.min(
                    intAtLevel,
                    10
                )

                earnedSkillPoints += 10 + intAtLevel*0.5 + (educatedPerk? (educatedPerk.level < level? 1: 0): 0)
            }

            let skillsTotal = 0;
            for(let skill in this.player.base_skills) {
                skillsTotal += this.player.base_skills[skill].value;
            }

            

            return Math.floor((baseSkillPoints+earnedSkillPoints) - skillsTotal);
        },
        remainingTags() {
            const hasTag = this.player.perks.find(perk => perk.id == "tag");
            let remainingTags = 3 + (hasTag? 1: 0);

            for(let skill in this.player.base_skills) {
                if (this.player.base_skills[skill].tagged) {
                    remainingTags -= 1;
                }
            }

            return remainingTags;
        }
    },
    methods: {
        hasComprehension() {
            if (this.player.perks.find(perk => perk.id == "comprehension")) {
                return true
            }
            return false
        }
    }
}
</script>

<style scoped>
    .error {
        color: red;
    }
</style>