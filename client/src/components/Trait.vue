<template>
    <div class="trait">
      <b-form-checkbox
      >
        {{ trait.name }}
      </b-form-checkbox>
      <b-button 
        variant="outline-primary"
        @click="addTrait(trait.id)"
      >Add</b-button>
    </div>
</template>

<script>
  import { mapActions } from 'vuex';

    export default {
        name: 'Trait',
        props: ['trait'],
        methods: {
          ...mapActions(['addTrait'])
        }
    }
</script>

<style scoped>

</style>
