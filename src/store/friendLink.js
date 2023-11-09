import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', {
    state: () => ({
        
    }),
    actions: {
        async urlPing(url) {
            return await axios.get(url);
        },
    },
})