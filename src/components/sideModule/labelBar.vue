<template>
    <sideTemplate>
        <template #title>
            标签页面
        </template>
        <template #content>
            <div class="labelBar" v-for="item in labelBarData" @click="tagSrearch(item.tag)">
                <div>
                    <h3>#{{ item.tag }}</h3>
                    <span>文章量{{ item.total }}/</span>
                    <span>浏览量{{ item.hots }}</span>
                </div>
                <div class="hot">
                    <div :class="labelHeat(item.hotness)"></div>
                </div>
            </div>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '@/components/sideModule/sideTemplate.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            labelBarData: []
        }
    },
    components: {
        sideTemplate,
    },
    methods: {
        labelHeat(hotness) {
            if (hotness < this.labelBar.heatNode.firstGear) {
                return "hotG";
            } else if (hotness < this.labelBar.heatNode.secondGear) {
                return "hotY";
            } else if (hotness < this.labelBar.heatNode.thirdGear) {
                return "hotO";
            } else {
                return "hotR";
            }
        },tagSrearch(tag) {
            this.$router.push({ path: '/filePage', query: { class: "tag", content: tag } });
        }
    }, mounted() {
        axiosStore().apiRequest(axiosStore().api.url + axiosStore().api.labelBar).then(data => {
            this.labelBarData = data.data;
        });
    },
    props: ["labelBar"]
}
</script>
<style scoped>
h3 {
    margin: 0.1rem;
    color: var(--color-theme-black);
}

.labelBar {
    display: grid;
    cursor: pointer;
    grid-template-columns: 3.5fr 1fr;
    border-radius: 0.25rem;
    transition: background-color 0.1s, transform 0.1s;
}

.labelBar:hover {
    background-color: var(--color-theme-grayscale2);
}

.labelBar:active {
    background-color: var(--color-theme-grayscale3);
    transform: scale(0.98);
}

.labelBar h1 {
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.announcementBoardTitleContent {
    margin: 0;
}

.hotG {
    background-color: var(--color-theme-G);
}

.hotY {
    background-color: var(--color-theme-Y);
}

.hotO {
    background-color: var(--color-theme-O);
}

.hotR {
    background-color: var(--color-theme-R);
}

.hotG,
.hotY,
.hotO,
.hotR {
    width: 0.6rem;
    height: 0.6rem;
    border-radius: 50%;
}

.hot {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>