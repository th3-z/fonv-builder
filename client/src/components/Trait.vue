<template>
    <div class="trait">
      <b-form-checkbox
      >
        {{ trait.name }}
      </b-form-checkbox>
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
