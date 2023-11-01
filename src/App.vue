<template>
  <!-- 导航栏 -->
  <navigationBar :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <homePage />
  </div>
  <!-- 侧边栏 -->
  <informationBar :informationBarData="informationBarData" />
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import homePage from '@/components/body/homePage.vue';
import config from './config.json';
export default {
  data() {
    return {
      navigationBarData: config.navigationBarData,
      informationBarData: config.informationBarData,
    }
  },
  components: {
    navigationBar,
    informationBar,
    homePage,
  },
}
</script>

<style scoped>
.centralFramework {
  width: 100%;
  height: 100%;
  border-left: 2px solid #F4F4F4;
  border-right: 2px solid #F4F4F4;
}
</style>

