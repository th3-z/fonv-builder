<template>
    <div class="perks-container">
        <div v-bind:key="perk.id" v-for="perk in perks">
            <perk v-bind:perk="perk"/>
        </div>
        <p
            v-bind:class="{'error':remainingPerks < 0}"
        >Remaining perks: {{remainingPerks}}</p>
    </div>
</template>

<script>
import Perk from './Perk.vue';
import { mapGetters } from 'vuex';

export default {
    name: "Perks",
    components: {
        Perk
    },
    computed: {
        ...mapGetters(['perks', 'player']),
        remainingPerks() {
            return Math.floor(this.player.level / 2) - this.player.perks.length;
        }
    }
}
</script>

<style scoped>
    .perks-container {
        display: flex;
        flex-wrap: wrap;
    }
</style>