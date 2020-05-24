<template>
  <b-card class="mb-1 mt-1 ml-1 mr-1 perk-card">
    <b-form-checkbox
      inline
      :id="perk.id"
      class="mr-1"
      @input="changePerk($event, perk.id)"
    ></b-form-checkbox>
    <label :for="perk.id">
      <strong>{{ perk.name }}</strong>
    </label>
    <p class="benefit">{{ perk.benefit }}</p>
  </b-card>
</template>

<script>
  import { mapActions } from 'vuex';

  export default {
      name: 'Perk',
      props: ['perk'],
      methods: {
        ...mapActions(['addPerk', 'removePerk']),
        changePerk(checked, perkId) {
          if (checked)
            this.addPerk(perkId);
          else
            this.removePerk(perkId);
        }
      }
  }
</script>

<style scoped>
  .perk-card {
    width: 38em;
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
