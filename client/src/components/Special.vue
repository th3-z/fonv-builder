<template>
    <div class="special form-group row">
        <label for="sb-special" class="col-sm-2 col-form-label">{{special.name}}</label>
        <b-form-spinbutton
            id="sb-special"
            size="sm"
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
    .special {
        align-items: center;
    }
</style>
