<template>
  <b-card class="mb-1 mt-1 ml-1 mr-1 implant-card">
    <template v-slot:header>
      <b-form-checkbox
        inline
        :id="implant.id"
        class="mr-1"
        @input="toggleImplant($event, implant.id)"
      ></b-form-checkbox>
      
      <label :for="implant.id">
        <strong>{{ implant.name }}</strong>
      </label>
    </template>

    <p class="benefit">{{ implant.benefit }}</p>

    <template v-slot:footer>
      <label :for="'sb-' + implant.id + '-level'" class="col-sm-2 col-form-label">Level</label>
      <b-form-spinbutton
          :id="'sb-' + implant.id + '-level'"
          size="sm"
          min="1"
          max="50"
          placeholder="1"
          @input="setImplantLevel({implantId: implant.id, level: $event})"
          inline
      ></b-form-spinbutton>
    </template>
  </b-card>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex';

    export default { 
        name: 'Implant',
        props: ['implant'],
        computed: {
            ...mapGetters(['player']),
        },
        methods: {
            ...mapActions(['addImplant', 'removeImplant', 'setImplantLevel']),
            toggleImplant(checked, implantId) {
                if (checked) {
                    this.addImplant({
                        implantId: implantId,
                        level: document.getElementById('sb-' + implantId + '-level').value
                    });
                } else {
                    this.removeImplant(implantId);
                }
            }
        }
    }
</script>

<style scoped>
    .implant-card {
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
