<template>
    <div>
        <div v-bind:key="trait.id" v-for="trait in traits">
            <trait v-bind:trait="trait"/>
            {{trait}}
        </div>
    </div>
</template>

<script>
import Trait from './Trait.vue';
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
    name: "Traits",
    components: {
        Trait
    },
    methods: {
        // ...mapActions(['addTrait'])
    },
    computed: mapGetters(['player']),
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/traits")
            .then(res => this.traits = res.data.traits)
            .catch(err => console.log(err));
    },
    data() {
        return {
            traits: []
        }
    },
}
</script>

<style scoped>

</style>