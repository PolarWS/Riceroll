<!-- 公告组件 -->
<template>
    <sideTemplate>
        <template #content>
            <div v-html="markDownToc" class="markDownToc"></div>
        </template>
    </sideTemplate>
</template>
<script>
import sideTemplate from '../sideTemplate.vue';
export default {
    components: {
        sideTemplate,
    }, props: {
        markDownToc: String,
    }
}
</script>
<style scoped>
.markDownToc {
    width: 14rem;
    padding: 0rem;
    background-color: var(--color-theme-grayscale1);
}

@media screen and (max-width: 1280px) {
    .markDownToc {
        width: 13rem;
    }
}
</style>