<template>
  <b-card class="mb-1 mt-1 ml-1 mr-1 perk-card">
    <template v-slot:header>
      <b-form-checkbox
        inline
        :id="perk.id"
        class="mr-1"
        @input="togglePerk($event, perk.id)"
      ></b-form-checkbox>
      
      <label :for="perk.id">
        <strong>{{ perk.name }}</strong>
      </label>
    </template>

    <p class="benefit">{{ perk.benefit }}</p>

    <template v-slot:footer>
      <label :for="'sb-' + perk.id + '-level'" class="col-sm-2 col-form-label">Level</label>
      <b-form-spinbutton
          :id="'sb-' + perk.id + '-level'"
          size="sm"
          min="2"
          max="50"
          placeholder="2"
          step="2"
          inline
      ></b-form-spinbutton>

      <span v-if="perk.ranks > 1">
        <label :for="'sb-' + perk.id + '-rank'" class="col-sm-2 col-form-label">Rank</label>
        <b-form-spinbutton
            :id="'sb-' + perk.id + '-rank'"
            size="sm"
            min="1"
            :max="perk.ranks"
            placeholder="1"
            step="1"
            inline
        ></b-form-spinbutton>
      </span>
    </template>
  </b-card>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex';

  export default {
      name: 'Perk',
      props: ['perk'],
      computed: mapGetters(['player']),
      methods: {
        ...mapActions(['addPerk', 'removePerk', 'setPerkLevel', 'setPerkRank']),
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
        }
      }
  }
</script>

<style scoped>
  .perk-card {
    width: 34em;
    min-height: 12em;
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
