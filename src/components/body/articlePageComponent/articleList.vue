<template>
    <div class="articleListCard">
        <div class="test">
            <div class="test2">

            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            url: "../../img/1.jpg",
            articleListData: [{
                title: "标题1",
                date: "2020-01-01",
                label: ["日常"],
                img: "文章链接",
                url: "../../img/1.jpg",
            },
            {
                title: "标题2",
                date: "2020-01-01",
                label: ["代码", "计算机"],
                img: "文章链接",
                url: "../../img/2.jpg",
            },
            {
                title: "标题3",
                date: "2020-01-01",
                label: ["相机", "数码"],
                img: "文章链接",
                url: "../../img/3.jpg",
            },
            {
                title: "标题4",
                date: "2020-01-01",
                label: ["日常"],
                img: "文章链接",
                url: "../../img/4.jpg",
            }]
        }
    },
}
</script>
<style>
.articleListCard {
    height: 13rem;
    display: grid;
    grid-template-columns: 1fr;
    padding: 2rem 3rem 0 3rem;
}

.test {
    height: 13rem;
    border-radius: 0.75rem;
}

.test2 {
    margin-top: 8rem;
    height: 5rem;
    border-radius: 0 0 0.75rem 0.75rem;
    background-color: rgba(0, 0, 0, 0.200);
}
</style>