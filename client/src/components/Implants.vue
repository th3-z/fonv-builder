<template>
    <div>
        <div v-bind:key="implant.id" v-for="implant in implants">
            <implant v-bind:implant="implant"/>
        </div>
        <p>Endurance implant does not affect implant capacity</p>
        <p>Remaining implants: {{remainingImplants()}}</p>
    </div>
</template>

<script>
import Implant from './Implant.vue'
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
    name: "Implants",
    components: {
        Implant
    },
    computed: {
        ...mapGetters(['player'])
    },
    data() {
        return {
            implants: []
        }
    },
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/implants")
            .then(res => this.implants = res.data.implants)
            .catch(err => console.log(err));
    },
    methods: {
        remainingImplants() {
            return this.player.base_specials.endurance - this.player.implants.length
        }
    }
}
</script>

<style scoped>
    .error {
        color: red;
    }
</style>