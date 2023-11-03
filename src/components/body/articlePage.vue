<!-- 最新回复组件 -->
<template>
    <informationBar :informationBarData="itemData.informationBarData" />
    <articleList />
</template>
<script>
import informationBar from './articlePageComponent/informationBar.vue';
import articleList from './articlePageComponent/articleList.vue';
export default {
    components: {
        informationBar,
        articleList,
    }, props: {
        itemData: Object
    }
}
</script>
<style scoped></style>