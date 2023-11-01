<!-- 信息栏 -->
<template>
    <div class="informationBar">
        <!-- 侧边栏组件 -->
        <announcementBoard v-if="informationBarData.default.announcementBoard.display"
            :announcementBoard="informationBarData.default.announcementBoard" />
        <labelBar v-if="informationBarData.default.labelBar.display" :labelBar="informationBarData.default.labelBar" />
        <replyBar v-if="informationBarData.default.replyBar.display" />
        <!-- 自定义组件 -->
        <sideTemplate v-if="informationBarData.custom.display" v-for="item in informationBarData.custom.content">
            <template #title>
                {{ item.title }}
            </template>
            <template #content>
                <div v-html="item.html"></div>
            </template>
        </sideTemplate>
        <!-- 脚标 -->
        <div v-for="item in informationBarData.footmark" class="footmark">
            <a :href="item.url">{{ item.title }}</a>
        </div>
    </div>
</template>
<script>
import announcementBoard from './sideModule/announcementBoard.vue';
import labelBar from './sideModule/labelBar.vue';
import replyBar from './sideModule/replyBar.vue';
import sideTemplate from './sideTemplate.vue';
export default {
    components: {
        announcementBoard,
        labelBar,
        replyBar,
        sideTemplate,
    }, props: ["informationBarData"]
}
</script>
<style scoped>
.footmark a {
    text-decoration: none;
    cursor: pointer;
    margin: 1rem 1.5rem;
    padding: 0 1.5rem;
    color: #D1D2D2;
}

.footmark a:hover {
    color: #8A8E90;
}

.footmark a:active {
    color: #74E4FB;
}
</style>