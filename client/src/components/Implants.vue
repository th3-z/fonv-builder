<template>
    <div>
        <div v-bind:key="implant.id" v-for="implant in implants">
            <implant v-bind:implant="implant"/>
        </div>
        <p>Endurance implant does not affect implant capacity</p>
        <p>Remaining implants: ?</p>
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
    }
}
</script>

<style scoped>
    .error {
        color: red;
    }
</style>