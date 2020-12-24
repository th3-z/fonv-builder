<template>
    <div class="special form-group row">
        <label for="sb-special" class="col-sm-2 col-form-label">{{special.name}}</label>
        <b-form-spinbutton
            id="sb-special"
            size="sm"
            :value="computedSpecial(special)"
            @change="changeSpecial($event, special)"
            min="1"
            max="10"
            inline
        ></b-form-spinbutton>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import computedSpecial from '../lib/special.js'

    export default {
        name: 'Special',
        props: ['special'],
        computed: mapGetters(['player']),
        methods: {
            computedSpecial(special) {
                return computedSpecial.special(this.player, special)
            },
            changeSpecial(event, special) {
                const delta = event - computedSpecial.special(this.player, special)
                this.player.base_specials[special.id] += delta
            }
        }
    }
</script>

<style scoped>
    .special {
        align-items: center;
    }
</style>
