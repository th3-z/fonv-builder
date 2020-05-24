<template>
    <div>
        <ul>
            <li>Carry weight:</li>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: "OtherEffects",
    computed: {
        ...mapGetters(['player']) 
    }
}
</script>

<style scoped>

</style>