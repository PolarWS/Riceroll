<!-- 公告组件 -->
<template>
    <sideTemplate>
        <template #title>
            {{ date }}
        </template>
        <template #content>
            <span>{{ announcementBoard.title }}</span>
            <br><br>
            <span>#文章统计：{{ articleCount }}</span>
            <br>
            <span>#回复统计：{{ commentCount }}</span>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '@/components/sideModule/sideTemplate.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            date: "",
            articleCount: "",
            commentCount: "",
        }
    },
    beforeMount() {
        this.date = new Date().getFullYear() + "/" + (new Date().getMonth() + 1) + "/" + new Date().getDate();
        axiosStore().apiRequest(axiosStore().api.url+axiosStore().api.announcementBoard).then(data => {
            this.articleCount = data.data.article;
            this.commentCount = data.data.comment;
        });
    },
    components: {
        sideTemplate,
    }, props: ["announcementBoard"]
}
</script>