<template>
  <b-card class="mb-1 mt-1 ml-1 mr-1 trait-card">
    <b-form-checkbox
      inline
      :id="trait.id"
      class="mr-1"
      @input="changeTrait($event, trait.id)"
    ></b-form-checkbox>
    <label :for="trait.id">
      <strong>{{ trait.name }}</strong>
    </label>
    <p class="benefit">{{ trait.desc_benefit }}</p>
    <p class="penalty mb-0">{{ trait.desc_penalty }}</p>
  </b-card>
</template>

<script>
  import { mapActions } from 'vuex';

  export default {
    name: 'Trait',
    props: ['trait'],
    methods: {
      ...mapActions(['addTrait', 'removeTrait']),
      changeTrait(checked, traitId) {
        if (checked)
          this.addTrait(traitId);
        else
          this.removeTrait(traitId);
      }
    }
  }
</script>

<style scoped>
  .trait-card {
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
