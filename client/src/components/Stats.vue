<template>
    <div class="ml-4">
        <ul>
            <li>Action points: {{ actionPoints }}</li>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import computedStats from '../lib/stats.js';

export default {
    name: "OtherEffects",
    computed: {
        ...mapGetters(['player']) ,
        actionPoints() {
            return computedStats.actionPoints(this.player);
        }
    }
}
</script>

<style scoped>

</style>