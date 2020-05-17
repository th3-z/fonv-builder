<template>
    <div>
        <div v-bind:key="trait.id" v-for="trait in traits">
            <trait v-bind:trait="trait"/>
            {{trait}}
        </div>
    </div>
</template>

<script>
import Trait from './Trait.vue'
import axios from 'axios';

export default {
    name: "Traits",
    components: {
        Trait
    },
    data() {
        return {
            traits: []
        }
    },
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/traits")
            .then(res => this.traits = res.data.traits)
            .catch(err => console.log(err));
    }
}
</script>

<style scoped>

</style>