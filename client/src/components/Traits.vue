<template>
    <div class="traits-container">
        <div v-bind:key="trait.id" v-for="trait in traits">
            <trait v-bind:trait="trait"/>
        </div>
        <p
            v-bind:class="{'error':remainingTraits < 0}"
        >Remaining traits: {{remainingTraits}}</p>
    </div>
</template>

<script>
import Trait from './Trait.vue';
import { mapGetters } from 'vuex';

export default {
    name: "Traits",
    components: {
        Trait
    },
    computed: {
        ...mapGetters(['traits', 'player']),
        remainingTraits() {
            return 2 - this.player.traits.length;
        }
    },
}
</script>

<style scoped>
    .traits-container {
        display: flex;
        flex-wrap: wrap;
    }

    .error {
        color: red;
    }
</style>