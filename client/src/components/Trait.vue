<template>
    <div class="trait">
      <b-form-checkbox
      >
        {{ trait.name }}
      </b-form-checkbox>
      <b-button variant="outline-primary">Add</b-button>
    </div>
</template>

<script>
    export default {
        name: 'Trait',
        props: ['trait']
    }
</script>

<style scoped>

</style>
