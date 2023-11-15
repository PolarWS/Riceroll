<template>
    <messagePopup v-for="(popup, index) in popups" :key="popup" @animationend="removePopup(popup)"
        :messageData="messageData" />
    <!-- <button @click="showPopup">Show Popup</button> -->
</template>
<script>
import messagePopup from '@/components/messagePopup.vue';
export default {
    data() {
        return {
            popups: [],
            popupsUniqueIdentifier: 0,
            messageData: {
                message: 'Your message',
                Color: 'messageY',
            }
        }
    }, components: {
        messagePopup,
    },
    methods: {
        handleClick(event) {
            this.$router.push('/' + event.id);
        },
        showPopup() {
            this.popups.push(this.popupsUniqueIdentifier++);
        },
        removePopup(popup) {
            this.popups = this.popups.filter(p => p !== popup);
        },
    },
}
</script>
<style></style>