<template>
    <div class="messagePopup" :class="messageData.Color">
        {{ messageData.message }}
    </div>
</template>
<script>
export default {
    props: ["messageData"]
}
</script>
<style>
.messagePopup {
    position: fixed;
    width: fit-content;
    top: -10rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
    max-width: 15rem;
    padding: 1rem 1.5rem;
    border-radius: 0.5rem;
    color: var(--color-theme-white);
    animation: fadeInOut 3s ease-in-out;
}

.messageG {
    background-color: var(--color-theme-msg-G);
}

.messageY {
    background-color: var(--color-theme-msg-Y);
}

.messageO {
    background-color: var(--color-theme-msg-O);
}

.messageR {
    background-color: var(--color-theme-msg-R);
}

@keyframes fadeInOut {
    0% {
        top: -10rem;
    }

    15% {
        top: 1rem;
    }

    85% {
        top: 1rem;
    }

    100% {
        top: -10rem;
    }
}
</style>