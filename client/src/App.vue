<template>
  <div id="app">
    <Header/>
    
    <div class="m-2 content">
      <BasicInfo class="mb-2"/>
      <b-tabs content-class="mt-2">
        <b-tab title="Skills &amp; SPECIAL" active>
          <b-row>
            <b-col><Skills/></b-col>
            <b-col><Specials/></b-col>
          </b-row>
        </b-tab>
        <b-tab title="Traits"><Traits/></b-tab>
        <b-tab title="Perks"><Perks/></b-tab>
        <b-tab title="Books"><Books/></b-tab>
        <b-tab title="Stats"><Stats/></b-tab>
        <b-tab title="Other effects"><OtherEffects/></b-tab>
      </b-tabs>
    </div>

    <Footer/>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';

  import Header from './components/layout/Header.vue'
  import Footer from './components/layout/Footer.vue'
  import Specials from './components/Specials.vue'
  import Traits from './components/Traits.vue'
  import Skills from './components/Skills.vue'
  import Perks from './components/Perks.vue'
  import Books from './components/Books.vue'
  import OtherEffects from './components/OtherEffects.vue'
  import Stats from './components/Stats.vue'
  import BasicInfo from './components/BasicInfo.vue'

  export default {
    name: 'App',
    components: {
      Header,
      Footer,
      Specials,
      Traits,
      Skills,
      Perks,
      Books,
      OtherEffects,
      Stats,
      BasicInfo
    },
    methods: {
        ...mapActions(['newPlayer', 'loadTraits', 'loadPerks', 'loadBooks'])
    },
    created() {
        this.newPlayer();
        this.loadTraits();
        this.loadPerks();
        this.loadBooks();
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

body, html {
  height: 100%;
}

#app {
  display: flex;
  height: 100vh;
  flex-direction: column;
  font-family: Arial, Helvetica, sans-serif;
  width: 90%;
  margin: 0 auto;
  background: #fff;
}

.content {
  flex: 1 0 auto;
}
</style>
