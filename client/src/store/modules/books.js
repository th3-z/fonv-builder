import axios from 'axios';

const state = {
    books: {}
};

const getters = {
    books: (state) => state.books
};

const actions = {
    async loadBooks({ commit }) {
        const response = await axios.get(process.env.VUE_APP_ROOT_API + "/books");
        commit('setBooks', response.data.books);
    },

    addBook({ commit, rootState }, bookId) {
        commit('addBookGeneric', {
            player: rootState.player.player,
            book_id: bookId
        });
    },

    removeBook({commit, rootState}, bookId) {
        commit('removeBookGeneric', {
            player: rootState.player.player,
            book_id: bookId
        });
    }
};

const mutations = {
    setBooks: (state, books) => (state.books = books),

    addBookGeneric(state, payload) {
        payload.player.books.push(payload.book_id);
    },

    removeBookGeneric(state, payload) {
        payload.player.books.splice(
            payload.player.books.indexOf(payload.book_id),
            1
        );
    },
};

export default {
    state,
    getters,
    mutations,
    actions
}