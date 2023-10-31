<!-- 最新回复组件 -->
<template>
    <informationBar />
    <articleList />
</template>
<script>
import informationBar from './bodyArticleComponent/informationBar.vue';
import articleList from './bodyArticleComponent/articleList.vue';
export default {
    components: {
        informationBar,
        articleList,
    },
}
</script>
<style scoped></style>