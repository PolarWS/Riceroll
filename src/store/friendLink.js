import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', {
    state: () => ({

    }),
    actions: {
        async urlPing(url) {
            const res = await axios.get(url)
            return res.data;
        },
    },
})