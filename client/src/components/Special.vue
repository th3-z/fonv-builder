<template>
    <div class="special">
        <label for="sb-special">{{special.name}}</label>
        <b-form-spinbutton
            id="sb-special"
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
        name: 'Special',
        props: ['special'],
        data() {
            return {
                value: 5
            }
        }
    }
</script>

<style scoped>

</style>
