<template>
    <div class="ml-4">
        <ul v-bind:key="benefit" v-for="benefit in getBenefits">
            <li class="benefit">{{ benefit }}</li>
        </ul>
        <ul v-bind:key="penalty" v-for="penalty in getPenalties">
            <li class="penalty">{{ penalty }}</li>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: "OtherEffects",
    computed: {
        ...mapGetters(['getPenalties', 'getBenefits']) 
    }
}
</script>

<style scoped>

    .penalty {
        color: red;
    }

    .benefit {
        color: green;
    }

</style>