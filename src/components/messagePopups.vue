<template>
    <messagePopup v-for="(popup, index) in popups" :key="popup" @animationend="removePopup(popup)"
        :messageData="messageData" />
</template>
<script>
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
    },
    methods: {
        showPopup(event) {
            this.messageData = event;
            this.popups.push(this.popupsUniqueIdentifier++);
        },
        removePopup(popup) {
            this.popups = this.popups.filter(p => p !== popup);
        },
    }, popup: ['messagePopups']
}
</script>