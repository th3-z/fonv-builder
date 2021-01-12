<template>
    <div>
        <div v-bind:key="special.id" v-for="special in specials">
            <Special v-bind:special="special"/>
        </div>
        <p
            v-bind:class="{'error':remainingSpecial < 0}"
        >Remaining points: {{remainingSpecial}}</p>
    </div>
</template>

<script>
import Special from './Special.vue';
import { mapGetters } from 'vuex';

import computedSpecial from '../lib/special.js'

export default {
    name: "Specials",
    components: {
        Special
    },
    computed: {
        ...mapGetters(['player', 'specials']),
        remainingSpecial() {
            return computedSpecial.remainingPoints(this.player)
        }
    }
}
</script>

<style scoped>
    .error {
        color: red;
    }
</style>