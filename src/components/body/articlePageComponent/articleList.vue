<!-- 第一版，感觉没那么好看后面改 -->
<template>
    <div class="articleListCard" v-for="index in articleListData">
        <div class="articleListCardImg" :style="{ backgroundImage: 'url(' + index.img + ')' }">
            <div class="articleListCardTitle">
                <div id="title">{{ index.title }}</div>
                <span class="date">{{ index.date }}</span>
                <span class="date" v-for="label in index.label">#{{ label }}</span>
                <div>
                    <span class="date" id="content">aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</span>
                </div>
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
                url: "文章链接",
                img: "src/components/img/3.jpg",
            },
            {
                title: "标题标题标题",
                date: "2020-01-01",
                label: ["代码", "计算机"],
                url: "文章链接",
                img: "src/components/img/4.png",
            },
            {
                title: "标题标题2标题23",
                date: "2020-01-01",
                label: ["相机", "数码"],
                url: "文章链接",
                img: "src/components/img/1.jpg",
            },
            {
                title: "标题4",
                date: "2020-01-01",
                label: ["日常"],
                url: "文章链接",
                img: "src/components/img/2.png",
            }]
        }
    },
}
</script>
<style scoped>
#title {
    font-size: 1.75rem;
    margin-bottom: 0.3rem;
    color: white;
}

.date {
    margin-right: 0.75rem;
    color: rgb(240, 240, 240);
}

.articleListCard {
    height: 16rem;
    display: grid;
    grid-template-columns: 1fr;
    padding: 1.5rem 5% 0 5%;

}

.articleListCardImg {
    box-shadow: 0 0 0.5rem #eeeeee;
    height: 16rem;
    border-radius: 0.75rem;
    background-size: cover;
    background-position: center center;

    transition: box-shadow 0.25s;
}

.articleListCardImg:hover {
    box-shadow: 0 0 0.75rem 0.5rem #e5e5e5;
    /* transform: scale(1.2); */
}

.articleListCardImg:hover .articleListCardTitle {
    margin-top: 8.75rem;
    height: 6.25rem;
}

.articleListCardTitle {
    margin-top: 10rem;
    height: 5rem;
    padding: 1rem 0 0 1.5rem;
    border-radius: 0 0 0.75rem 0.75rem;
    background-color: rgba(0, 0, 0, 0.300);
    overflow: hidden;
    right: 0;

    transition: margin-top 0.25s, height 0.25s;
}

.articleListCardImg:hover #content {
    line-height: 1rem;
}

#content {
    line-height: 2.5rem;
    transition: line-height 0.5s;
}
</style>