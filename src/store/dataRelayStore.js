import { defineStore } from 'pinia';
export const dataRelayStore = defineStore('dataRelayStore', {
    state: () => ({
        widthLevel: 0,
        configData: Object,
    }),
});