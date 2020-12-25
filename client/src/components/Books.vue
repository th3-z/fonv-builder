<template>
    <div>
        <div v-bind:key="book.id" v-for="book in books">
            <book v-bind:book="book"/>
        </div>
        <p>Maximum includes all DLC books, and skill book recipes found in Old World Blues but excludes random loot books from Honest Hearts.</p>
    </div>
</template>

<script>
import Book from './Book.vue'
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
    name: "Books",
    components: {
        Book
    },
    computed: {
        ...mapGetters(['player'])
    },
    data() {
        return {
            books: []
        }
    },
    created() {
        axios.get(process.env.VUE_APP_ROOT_API + "/books")
            .then(res => this.books = res.data.books)
            .catch(err => console.log(err));
    }
}
</script>

<style scoped>
    .error {
        color: red;
    }
</style>