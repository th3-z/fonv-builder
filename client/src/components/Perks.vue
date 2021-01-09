<template>
    <div class="perks-container">
        <div class="container">
            <div class="row" v-bind:key="perk.id" v-for="perk in player.perks">
                <div class="col-sm">
                    <button 
                        class="btn btn-outline-primary"
                        @click="removePerk(perk.id)"
                    >-</button>
                    <p>{{ getPerk(perk.id).name }}</p>
                </div>
                <div class="col-sm">
                    <p>{{ getPerk(perk.id).benefit }}</p>
                </div>
                <div class="col-sm">
                    <p>{{ reqString(getPerk(perk.id)) }}</p>
                </div>
                <div class="col-sm">
                    <label :for="'sb-' + perk.id + '-level'" class="col-sm-2 col-form-label">Level</label>
                    <b-form-spinbutton
                        :id="'sb-' + perk.id + '-level'"
                        @change="setPerkLevel({perk_id: perk.id, level: $event})"
                        size="sm"
                        min="2"
                        max="50"
                        placeholder="2"
                        step="2"
                        inline
                    ></b-form-spinbutton>
                </div>
            </div>
        </div>

        <div class="container">
            <div v-bind:key="perk.id" v-for="perk in perks">
                <perk v-bind:perk="perk"/>
            </div>
        </div>
        <p
            v-bind:class="{'error':remainingPerks < 0}"
        >Remaining perks: {{remainingPerks}}</p>
    </div>
</template>

<script>
import Perk from './Perk.vue';
import { mapGetters, mapActions } from 'vuex';
import perks from '../lib/perks.js';

export default {
    name: "Perks",
    components: {
        Perk
    },
    computed: {
        ...mapGetters(['perks', 'player', 'getPerk']),
        remainingPerks() {
            return Math.floor(this.player.level / 2) - this.player.perks.length;
        }
    },
    methods: {
        ...mapActions(['removePerk', 'setPerkLevel']),
        reqString(perk) {
            return perks.reqString(perk)
        }
    }
}
</script>

<style scoped>
    .perks-container {
        display: flex;
        flex-wrap: wrap;
    }
</style>