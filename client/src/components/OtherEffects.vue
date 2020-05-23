<template>
    <div>
        <ul v-bind:key="benefit" v-for="benefit in benefits">
            <li>{{ benefit }}</li>
        </ul>
        <ul v-bind:key="penalty" v-for="penalty in getPenalties">
            <li>{{ penalty }}</li>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: "OtherEffects",
    computed: mapGetters(['getPenalties']),
    data() {
        return {
            benefits: []
        }
    }    
}
</script>

<style scoped>

</style>