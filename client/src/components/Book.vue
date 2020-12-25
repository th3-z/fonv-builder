<template>
    <div class="book form-group row">
        <label for="sb-book" class="col-sm-2 col-form-label">{{book.name}}</label>
        <b-form-spinbutton
            id="sb-book"
            size="sm"
            :value="countBooks(book)"
            @change="change($event, book)"
            min="0"
            :max="book.quantity"
            inline
        ></b-form-spinbutton>
    </div>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex';

    export default {
        name: 'Book',
        props: ['book'],
        computed: {
            ...mapGetters(['player']),
        },
        methods: {
            ...mapActions(['addBook', 'removeBook']),
            countBooks(book) {
                let count = this.player.books.reduce(function(count, current) {
                    if (current == book.id) {
                        count++
                    }
                    return count
                }, 0)
                return count
            },
            change(event, book) {
                const delta = event - this.countBooks(book)
                for (let i = 0; i < Math.abs(delta); i++) {
                    if (delta>0)
                        this.addBook(book.id)
                    else
                        this.removeBook(book.id)
                }
            }
        }
    }
</script>

<style scoped>
    .book {
        align-items: center;
    }
</style>
