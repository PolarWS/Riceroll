<template>
    <div>
        <div class="bodyItemTopImg" :style="`background-image: url(${itemData.title.img})`">
            <h1>「{{ itemData.title.content }}」</h1>
        </div>
        <markDown :markDownData="itemData.md" />
    </div>
</template>
<script>
import markDown from '../markDown.vue';
export default {
    props: {
        itemData: Object,
    },
    components: {
        markDown,
    },
}
</script>
<style scoped>
.bodyItemTopImg {
    width: 100%;
    height: 15rem;
    background-size: 100%;
    background-position: center;
    background-repeat: no-repeat;
    /* 居中 */
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--color-theme-white);
    transition: background-size 0.5s;
}

.bodyItemTopImg:hover {
    background-size: 110%;
}

/* 轮询600px取消background-size */
@media screen and (max-width: 600px) {
    .bodyItemTopImg {
        background-size: cover;
    }

    .bodyItemTopImg:hover {
        background-size: cover;
    }
}
</style>