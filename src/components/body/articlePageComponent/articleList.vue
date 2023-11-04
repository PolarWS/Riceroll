<!-- 第一版，感觉没那么好看后面改 -->
<template>
    <div class="articleListCard" v-for="index in articleListData">
        <div class="articleListCardImg" :style="{ backgroundImage: 'url(' + index.url + ')' }">
            <div class="articleListCardTitle">
                <div id="title">{{ index.title }}</div>
                <span class="date">{{ index.date }}</span>
                <span class="date" v-for="label in index.label">#{{ label }}</span>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            articleListData: [{
                title: "标题标题标题标题2",
                date: "2020-01-01",
                label: ["日常"],
                img: "文章链接",
                url: "src/components/img/3.jpg",
            },
            {
                title: "标题标题标题",
                date: "2020-01-01",
                label: ["代码", "计算机"],
                img: "文章链接",
                url: "src/components/img/4.png",
            },
            {
                title: "标题标题2标题23",
                date: "2020-01-01",
                label: ["相机", "数码"],
                img: "文章链接",
                url: "src/components/img/1.jpg",
            },
            {
                title: "标题4",
                date: "2020-01-01",
                label: ["日常"],
                img: "文章链接",
                url: "src/components/img/2.png",
            }]
        }
    },
}
</script>
<style scoped>
#title {
    font-size: 1.75rem;
    margin-bottom: 0.3rem;
}

.date {
    margin-right: 0.75rem;
}

.articleListCard {
    height: 13rem;
    display: grid;
    grid-template-columns: 1fr;
    padding: 1.5rem 5% 0 5%;

}

.articleListCardImg {
    box-shadow: 0 0 0.5rem #eeeeee;
    height: 13rem;
    border-radius: 0.75rem;
    background-size: cover;

    transition-property: transform, box-shadow;
    transition-duration: .25s, 1s;
}

.articleListCardImg:hover {
    transform: translateY(-0.2rem);
    box-shadow: 0 0 0.75rem 0.5rem #e5e5e5;
}

.articleListCardTitle {
    margin-top: 7rem;
    height: 5rem;
    color: white;
    padding: 1rem 0 0 1.5rem;
    border-radius: 0 0 0.75rem 0.75rem;
    background-color: rgba(0, 0, 0, 0.200);
}
</style>