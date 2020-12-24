<template>
    <div class="skill form-group row">
        <label for="sb-skill" class="col-sm-2 col-form-label">{{skill.name}}</label>
        <b-form-spinbutton
            id="sb-skill"
            size="sm"
            :value="computedSkill(skill)"
            @change="changeSkill($event, skill)"
            min="15"
            max="100"
            inline
        ></b-form-spinbutton>
        <b-form-checkbox
            v-b-tooltip.hover.right="'Tag skill'"
            inline
            class="ml-2"
            v-model="player.base_skills[skill.id].tagged"
            @input="tagSkill($event, skill.id)"
        ></b-form-checkbox>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import computedSkill from '../lib/skills.js';

    export default {
        name: 'Skill',
        props: ['skill'],
        computed: {
            ...mapGetters(['player']),
        },
        methods: {
            tagSkill(checked, skillId) {
                if (checked) {
                    this.player.base_skills[skillId].value += 15
                    this.player.skill_points += 15
                } else {
                    this.player.base_skills[skillId].value -= 15
                    this.player.skill_points -= 15
                }
            },
            computedSkill(skill) {
                return computedSkill.skill(this.player, skill)
            },
            changeSkill(event, skill) {
                const delta = event - computedSkill.skill(this.player, skill)
                this.player.base_skills[skill.id].value += delta
            }
        }
    }
</script>

<style scoped>
    .skill {
        align-items: center;
    }
</style>
