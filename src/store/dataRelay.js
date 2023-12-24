import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';

export const dataRelay = defineStore('dataRelay', {
    state: () => ({
        markdownPage: '',
        widthLevel: 0,
    }),
    actions: {
    },
});