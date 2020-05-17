<template>
    <div>
        <div v-bind:key="special.id" v-for="special in specials">
            <Special v-bind:special="special"/>
            {{special}}
        </div>
    </div>
</template>

<script>
import Special from './Special.vue'
import axios from 'axios';

export default {
    name: "Specials",
    components: {
        Special
    },
    data() {
        return {
            specials: []
        }
    },
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/specials")
            .then(res => this.specials = res.data.specials)
            .catch(err => console.log(err));
    }
}
</script>

<style scoped>

</style>