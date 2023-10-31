<script>
import navigationBar from './components/navigationBar.vue';
import informationBar from './components/informationBar.vue';
import bodyArticle from './components/body/bodyArticle.vue';
export default {
  components: {
    navigationBar,
    informationBar,
    bodyArticle,
  },
}
</script>

<template>
  <!-- 导航栏 -->
  <navigationBar />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <bodyArticle />
  </div>
  <!-- 侧边栏 -->
  <informationBar />
</template>
<style scoped>
.centralFramework {
  width: 100%;
  height: 100%;
  border-left: 2px solid #F4F4F4;
  border-right: 2px solid #F4F4F4;
}
</style>

