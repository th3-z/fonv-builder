<template>
    <div class="special">
        <label for="sb-special">{{special.name_short}}</label>
        <b-form-spinbutton
            id="sb-special"
            size="sm"
            class="mb-2"
            v-model="player.base_specials[special.id]"
            min="1"
            max="10"
            inline
        ></b-form-spinbutton>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';

    export default {
        name: 'Special',
        props: ['special'],
        computed: mapGetters(['player'])
    }
</script>

<style scoped>

</style>
