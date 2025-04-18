<template>
    <messagePopup v-for="popup in popups" :key="popup" @animationend="removePopup(popup)" :messageData="messageData" />
</template>
<script>
import { axiosStore } from '@/store/axiosStore.js';
import messagePopup from '@/components/messagePopup.vue';
export default {
    data() {
        return {
            popups: [],
            popupsUniqueIdentifier: 0,
            messageData: Object,
        }
    }, components: {
        messagePopup,
    }, computed: {
        messagePopupData() {
            return axiosStore().messagePopupData;
        }
    }, watch: {
        messagePopupData: {
            handler() {
                let delay = 0;
                let maxDelay = 0;
                for (const item of this.messagePopupData) {
                    setTimeout(() => {
                        this.showPopup(item);
                    }, delay);
                    delay += 400;
                    if (delay > maxDelay) {
                        maxDelay = delay;
                    }
                }
                setTimeout(() => {
                    axiosStore().messagePopupData = [];
                }, maxDelay);
            },
            deep: true,
        }
    }, methods: {
        showPopup(event) {
            this.messageData = event;
            this.popups.push(this.popupsUniqueIdentifier++);
        },
        removePopup(popup) {
            this.popups = this.popups.filter(p => p !== popup);
        },
    },
}
</script>