import { defineStore } from 'pinia'

export const dataRelay = defineStore('dataRelay', {
    state: () => ({
        widthLevel: 0,
    }),
    actions: {
        winWidth() {
            if (window.innerWidth > 1280) {
                this.widthLevel = 5;
            } else if (window.innerWidth > 1024) {
                this.widthLevel = 4;
            } else if (window.innerWidth > 600) {
                this.widthLevel = 3;
            } else {
                this.widthLevel = 2;
            }
        }
    },
})