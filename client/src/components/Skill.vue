<template>
    <div class="skill form-group row">
        <label for="sb-skill" class="col-sm-2 col-form-label">{{skill.name}}</label>
        <b-form-spinbutton
            id="sb-skill"
            size="sm"
            v-model="player.base_skills[skill.id].value"
            min="15"
            max="100"
            inline
        ></b-form-spinbutton>
        <b-form-checkbox
            inline
            class="ml-2"
            v-model="player.base_skills[skill.id].tagged"
        ></b-form-checkbox>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        name: 'Skill',
        props: ['skill'],
        computed: mapGetters(['player'])
    }
</script>

<style scoped>
    .skill {
        align-items: center;
    }
</style>
