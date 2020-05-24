<template>
    <div>
        <b-form inline>
            <b-form-group label="Name" label-for="name" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-input
                    id="name"
                    v-model="player.name"
                    placeholder="Player name"
                ></b-form-input>
            </b-form-group>

            <b-form-group label="Gender" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-radio-group
                    v-model="player.gender"
                    :options="genders"
                    name="radio-inline"
                ></b-form-radio-group>
            </b-form-group>

            <b-form-group label="Level" label-for="level" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-spinbutton
                    id="level"
                    size="sm"
                    class=""
                    v-model="player.level"
                    min="1"
                    max="50"
                    inline
                ></b-form-spinbutton>
            </b-form-group>

            <b-button variant="outline-primary" @click="exportPlayer()" class="mb-2 mr-sm-2 mb-sm-0">Export</b-button>

            <b-form-file
                v-model="importFile"
                placeholder="Choose a file or drop it here..."
                accept=".json"
                class="mb-2 mr-sm-2 mb-sm-0"
            ></b-form-file>
            <b-button variant="outline-primary" @click="importPlayer()" class="mb-2 mr-sm-2 mb-sm-0">Import</b-button>
        </b-form>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: "BasicInfo",
    computed: {
        ...mapGetters(['player']),
    },
    methods: {
        ...mapActions(['setPlayer']),
        exportPlayer() {
            let data = "data:"
                +"text/json;charset=utf-8,"
                + encodeURIComponent(JSON.stringify(this.player));
            let exportAnchor = document.createElement("a");
            exportAnchor.setAttribute("download", "player.json");
            exportAnchor.setAttribute("href", data);
            document.body.appendChild(exportAnchor);
            exportAnchor.click();
            exportAnchor.remove();
        },
        importPlayer() {
            const reader = new FileReader();
            reader.onload = (event) => {
                this.setPlayer(JSON.parse(event.target.result));
            };
            reader.readAsText(this.importFile);  
        },
    },
    data() {
        return {
            genders: [
                { text: "Male", value: "male" },
                { text: "Female", value: "female" }
            ],
            importFile: null
        };
    }
}
</script>

<style scoped>

</style>