<!-- 信息栏 -->
<template>
    <div class="informationBar">
        <!-- 侧边栏组件 -->
        <announcementBoard />
        <labelBar />
        <replyBar />
        <!-- 脚标 -->
        <div v-for="(item, index) in footmarkData" class="footmark">
            <a :href="item.url">{{ item.title }}</a>
        </div>
    </div>
</template>
<script>
import announcementBoard from './sideModule/announcementBoard.vue';
import labelBar from './sideModule/labelBar.vue';
import replyBar from './sideModule/replyBar.vue';
export default {
    data() {
        return {
            // 脚标数据
            footmarkData: [
                { title: "由 Riceroll 框架驱动", url: "#" },
                { title: "这是渡鸦的小窝哟!", url: "#" },
                { title: "萌备案号23333333", url: "#" },
                { title: "©2020 - 2023 By PolarWS", url: "#" }
            ]
        }
    },
    components: {
        announcementBoard,
        labelBar,
        replyBar,
    },
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