<!-- 最新回复组件 -->
<template>
    <sideTemplate>
        <template #title>
            最新回复
        </template>
        <template #content>
            <div v-for="(item, index) in msgData" :key="index" class="replyList">
                <a :href="item.url">{{ item.msg }}</a>
            </div>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '../sideTemplate.vue';
export default {
    data() {
        return {
            // 此处数据后端请务必做msg截取处理，为了减少带宽和防止页面变形
            msgData: [
                { id: "dsfsdf", msg: "Anonymous：码农路过，留...", url: "#" },
                { id: "dfsdff", msg: "千羽：鼠标点击特效好像有b...", url: "#" },
                { id: "xcvdfg", msg: "neko：欢迎交换友链,请留言...", url: "#" },
                { id: "hgfhfg", msg: "夏目：新的主题还行", url: "#" },
            ]
        }
    },
    components: {
        sideTemplate,
    },
}
</script>
<style scoped>
.replyList {
    margin: 0.3rem 0;
}
</style>