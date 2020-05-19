<template>
    <div class="skill">
        <label for="sb-skill">{{skill.name}}</label>
        <b-form-spinbutton
            id="sb-skill"
            size="sm"
            class="mb-2"
            v-model="player.base_skills[skill.id].value"
            min="15"
            max="100"
            inline
        ></b-form-spinbutton>
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

</style>
