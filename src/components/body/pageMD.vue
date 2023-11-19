<template>
    <div>
        <div class="bodyItemTopImg" :style="`background-image: url(${markDownData.title.img})`">
            <h1>「{{ markDownData.title.content }}」</h1>
        </div>
        <markDown :markDownData="markDownData.md" />
    </div>
</template>
<script>
import markDown from '../markDown.vue';
export default {
    data() {
        return {
            markDownData: {
                "title": {
                    "content": "这是一个md",
                    "img": "http://127.0.0.1:5173/src/components/img/7.jpg"
                },
                "md": "# 摆烂暂时不写"
            },
        }
    },
    components: {
        markDown,
    },
    mounted() {

    }
}
</script>
<style>
.bodyItemTopImg {
    width: 100%;
    height: 15rem;
    background-size: 100%;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--color-theme-white);
    transition: background-size 0.5s;
}

.bodyItemTopImg:hover {
    background-size: 110%;
}

@media screen and (max-width: 600px) {
    .bodyItemTopImg {
        background-size: cover;
    }

    .bodyItemTopImg:hover {
        background-size: cover;
    }
}
</style>