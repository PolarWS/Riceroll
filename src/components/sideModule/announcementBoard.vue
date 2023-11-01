<!-- 公告组件 -->
<template>
    <sideTemplate>
        <template #title>
            {{ date }}
        </template>
        <template #content>
            <span>{{ announcementBoard.title }}</span>
            <br><br>
            <span>#字数统计：{{ numberOfWords }}</span>
            <br>
            <span>#评论统计：{{ numberOfComments }}</span>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '../sideTemplate.vue';
export default {
    data() {
        return {
            date: "",
            title: "感谢访问本站，若喜欢请收藏交个朋友谢谢呐(｀・ω・´)",
            numberOfWords: "999",
            numberOfComments: "999",
        }
    },
    beforeMount() {
        // 渲染前阶段获取日期
        this.date = new Date().getFullYear() + "/" + (new Date().getMonth() + 1) + "/" + new Date().getDate();
    },
    components: {
        sideTemplate,
    }, props: ["announcementBoard"]
}
</script>