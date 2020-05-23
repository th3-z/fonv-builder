<template>
    <div class="perks-container">
        <div v-bind:key="perk.id" v-for="perk in perks">
            <perk v-bind:perk="perk"/>
        </div>
    </div>
</template>

<script>
import Perk from './Perk.vue';
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
    name: "Perks",
    components: {
        Perk
    },
    computed: mapGetters(['player']),
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/perks")
            .then(res => this.perks = res.data.perks)
            .catch(err => console.log(err));
    },
    data() {
        return {
            perks: []
        }
    },
}
</script>

<style scoped>
    .perks-container {
        display: flex;
        flex-wrap: wrap;
    }
</style>