import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', {
    state: () => ({
        markdownData : {id:"", content:{}},
    }),
    actions: {
        async apiRequest(url) {
            const res = await axios.get(url)
            return res.data;
        },
    },
})