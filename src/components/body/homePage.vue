<!-- 最新回复组件 -->
<template>
    <informationBar />
    <articleList />
</template>
<script>
import informationBar from './homePageComponent/informationBar.vue';
import articleList from './homePageComponent/articleList.vue';
export default {
    components: {
        informationBar,
        articleList,
    },
}
</script>
<style scoped></style>