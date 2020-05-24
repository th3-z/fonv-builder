<template>
    <div>
        <b-form inline>
            <label  class="mr-sm-2" for="name">Name</label>
            <b-form-input
                id="name"
                class="mb-2 mr-sm-2 mb-sm-0"
                v-model="player.name"
                placeholder="Player name"
            ></b-form-input>
            
            <label  class="mr-sm-2" for="gender">Gender</label>
            <b-form-radio-group
                id="gender"
                class="mb-2 mr-sm-2 mb-sm-0"
                v-model="player.gender"
                :options="genders"
                name="radio-inline"
            ></b-form-radio-group>
            
            <label  class="mr-sm-2" for="level">Level</label>
            <b-form-spinbutton
                id="level"
                class="mb-2 mr-sm-2 mb-sm-0"
                v-model="player.level"
                min="1"
                max="50"
                inline
            ></b-form-spinbutton>

            <b-button
                id="export"
                variant="outline-primary"
                @click="exportPlayer()"
                class="mb-2 mr-sm-2 mb-sm-0"
            >Export</b-button>
            <div class="spacer"></div>
            
            <b-form-file
                id="import-file"
                placeholder="Choose a file or drop it here..."
                v-model="importFile"
                accept=".json"
                class="mb-2 mr-sm-2 mb-sm-0 file-import"
            ></b-form-file>

            <b-button
                id="import"
                variant="outline-primary"
                @click="importPlayer()"
                class="mb-2 mr-sm-2 mb-sm-0"
            >Import</b-button>
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

<style>
    .file-import {
        max-width: 20em;
    }

    .custom-file-label {
        justify-content: left !important;
    }
    
    .spacer {
        flex-grow: 1;
    }
</style>