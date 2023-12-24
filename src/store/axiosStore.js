import { defineStore } from 'pinia'
import axios from 'axios'
import config from "../config.json"

export const useCounterStore = defineStore('counter', {
    state: () => ({
        markdownData: { id: "", content: {} },
        configData: config,
    }),
    actions: {
        async apiRequest(url, data) {
            let res;
            if (data) {
                res = await axios.post(url, data);
            } else {
                res = await axios.get(url);
            }
            return res.data;
        },
    },
})