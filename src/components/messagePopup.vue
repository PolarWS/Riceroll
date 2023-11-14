<template>
    <div class="messagePopup">
        这是一个消息弹窗
    </div>
</template>

<style>
.messagePopup {
    position: fixed;
    width: fit-content;
    top: -10rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
    max-width: 15rem;
    padding: 1rem 1.5rem;
    border-radius: 0.5rem;
    color: var(--color-theme-white);
    background-color: var(--color-theme-selected);
    animation: fadeInOut 3s ease-in-out;
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