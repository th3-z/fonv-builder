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
import axios from 'axios';

import computedSpecial from '../lib/special.js'

export default {
    name: "Specials",
    components: {
        Special
    },
    computed: {
        ...mapGetters(['player']),
        remainingSpecial() {
            return computedSpecial.remainingPoints(this.player)
        }
    },
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/specials")
            .then(res => this.specials = res.data.specials)
            .catch(err => console.log(err));
    },
    data() {
        return {
            specials: []
        }
    },
}
</script>

<style scoped>
    .error {
        color: red;
    }
</style>