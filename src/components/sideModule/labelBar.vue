<!-- 标签组件 -->
<template>
    <sideTemplate>
        <template #title>
            标签页面
        </template>
        <template #content>
            <div class="labelBar" v-for="item in labelBarData">
                <div>
                    <h3>#{{ item.labelName }}</h3>
                    <span>文章量{{ item.numberOfPages }}/</span>
                    <span>浏览量{{ item.numberOfViews }}</span>
                </div>
                <div class="hot">
                    <!-- 调用labelheat进行热度统计同时改变这个·的颜色 -->
                    <div :class="labelHeat(item.numberOfPages, item.numberOfViews)"></div>
                </div>
            </div>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '../sideTemplate.vue';
export default {
    data() {
        return {
            labelBarData: [{
                labelName: "日常",
                numberOfPages: 999,
                numberOfViews: 10,
            }, {
                labelName: "数码",
                numberOfPages: 70,
                numberOfViews: 80,
            }, {
                labelName: "计算机",
                numberOfPages: 30,
                numberOfViews: 40,
            }, {
                labelName: "摄影",
                numberOfPages: 10,
                numberOfViews: 19,
            }]
        }
    },
    components: {
        sideTemplate,
    },
    methods: {
        // 判断热度并且返回class颜色
        labelHeat(numberOfPages, numberOfViews) {
            const heatIndex = numberOfPages * numberOfViews;
            if (heatIndex < this.labelBar.heatNode.firstGear) {
                return "hotG";
            } else if (heatIndex < this.labelBar.heatNode.secondGear) {
                return "hotY";
            } else if (heatIndex < this.labelBar.heatNode.thirdGear) {
                return "hotO";
            } else {
                return "hotR";
            }
        }
    }, props: ["labelBar"]
}
</script>
<style scoped>
h3 {
    margin: 0.1rem;
}

.labelBar {
    display: grid;
    cursor: pointer;
    grid-template-columns: 3.5fr 1fr;

    border-radius: 0.25rem;
    transition: background-color 0.1s,transform 0.1s;
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

.hot{
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>