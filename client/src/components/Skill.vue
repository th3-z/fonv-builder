<template>
    <div class="skill">
        <label for="sb-skill">{{skill.name}}</label>
        <b-form-spinbutton
            id="sb-skill"
            size="sm"
            class="mb-2"
            v-model="value"
            min="1"
            max="10"
            inline
        ></b-form-spinbutton>
    </div>
</template>

<script>
    export default {
        name: 'Skill',
        props: ['skill'],
        data() {
            return {
                value: 5
            }
        }
    }
</script>

<style scoped>

</style>
