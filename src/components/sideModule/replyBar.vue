<!-- 最新回复组件 -->
<template>
    <sideTemplate>
        <template #title>
            最新回复
        </template>
        <template #content>
            <div v-for="(item, index) in msgData" :key="index" class="replyList">
                <a :href="item.url + '#' + item.uuid">{{ item.name + '：' + item.comment }}</a>
            </div>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '@/components/sideModule/sideTemplate.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            msgData: []
        }
    }, mounted() {
        axiosStore().apiRequest(axiosStore().api.url + axiosStore().api.replyBar).then(data => {
            this.msgData = data.data;
        });

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