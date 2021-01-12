<template>
  <div :class="{'hidden': !perkVisible(perk, this.player), 'row': true}">
    <div class="col-sm">
      <button 
        class="btn btn-outline-primary"
        @click="addPerk({perkId: perk.id, level: perk.level_requirement})"
      >+</button>
      {{ player.gender == "female" && perk.name_female? perk.name_female: perk.name  }}
    </div>
    <div class="col-sm benefit">
      {{ perk.benefit }}
    </div>
    <div class="col-sm">
      <ul>
        <li :key="requirement.idx" v-for="requirement in reqList(perk, player)" v-bind:class="{'penalty':requirement.ok == false}">
          {{ requirement.requirement }}
        </li>
      </ul>
      
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex';
  import perks from '../lib/perks.js';

  export default {
      name: 'Perk',
      props: ['perk'],
      computed: {
        ...mapGetters(['player']),
      },
      methods: {
        ...mapActions(['addPerk']),
        togglePerk(checked, perkId) {
          if (checked) {
            const level = document.getElementById("sb-" + perkId + "-level")
            const rank = document.getElementById("sb-" + perkId + "-rank")
            this.addPerk(perkId)
            this.setPerkLevel({perk_id: perkId, level: Number(level.value)})
            if (rank) {
              this.setPerkRank({perk_id: perkId, rank: Number(rank.value)})
            }
          } else {
            this.removePerk(perkId);
          }
        },
        perkVisible: (perk, player) => perks.isVisible(perk, player),
        reqList: (perk, player) => perks.reqList(perk, player)
      }
  }
</script>

<style scoped>
  .perk-card {
    width: 34em;
    min-height: 12em;
  }

  .hidden {
    display: none;
  }

  .penalty {
    color: red;
  }

  .benefit {
    color: green;
  }

  label {
    vertical-align: middle;
    position: relative;
    bottom: .16em;
  }
  
</style>
