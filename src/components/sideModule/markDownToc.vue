<!-- 公告组件 -->
<template>
    <sideTemplate>
        <template #content>
            <markDown :markDownData="markDownData" />
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '../sideTemplate.vue';
import markDown from '../markDown.vue';
export default {
    data() {
        return {
            markDownData: "",
        }
    },
    components: {
        sideTemplate,
        markDown,
    },
}
</script>
<style scoped>
.markdown-body {
    width: 14rem;
    padding: 0rem;
    background-color: var(--color-theme-grayscale1);
}

@media screen and (max-width: 1280px) {
    .markdown-body {
        width: 13rem;
    }
}
</style>