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
            msgData: [
                { id: "dsfsdf", msg: "Anonymous：码农路过，留农路过，", url: "#" },
                { id: "dfsdff", msg: "千羽：鼠标点击特效好像：鼠标点击特效", url: "#" },
                { id: "xcvdfg", msg: "neko：欢迎交换友链,请留言过，", url: "#" },
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
    width: 14rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    color: var(--color-theme-grayscale5);
}

@media screen and (max-width: 1280px) {
    .replyList {
        width: 13rem;
    }
}
</style>