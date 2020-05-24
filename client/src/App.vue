<template>
  <div id="app">
    <Header/>
    
    <div class="m-2">
      <BasicInfo/>
      <b-tabs content-class="mt-3">
        <b-tab title="SPECIAL" active><Specials/></b-tab>
        <b-tab title="Skills"><Skills/></b-tab>
        <b-tab title="Traits"><Traits/></b-tab>
        <b-tab title="Perks"><Perks/></b-tab>
        <b-tab title="Stats"><Stats/></b-tab>
        <b-tab title="Other effects"><OtherEffects/></b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';

  import Header from './components/layout/Header.vue'
  import Specials from './components/Specials.vue'
  import Traits from './components/Traits.vue'
  import Skills from './components/Skills.vue'
  import Perks from './components/Perks.vue'
  import OtherEffects from './components/OtherEffects.vue'
  import Stats from './components/Stats.vue'
  import BasicInfo from './components/BasicInfo.vue'

  export default {
    name: 'App',
    components: {
      Header,
      Specials,
      Traits,
      Skills,
      Perks,
      OtherEffects,
      Stats,
      BasicInfo
    },
    methods: {
        ...mapActions(['newPlayer', 'loadTraits', 'loadPerks'])
    },
    created() {
        this.newPlayer();
        this.loadTraits();
        this.loadPerks();
    },
  }
</script>

<style>
/* Resets */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
