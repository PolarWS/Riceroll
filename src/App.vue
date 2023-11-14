<template>
  <!-- 导航栏 -->
  <navigationBar @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <messagePopup />
    <router-view></router-view>
  </div>
  <!-- 侧边栏 -->
  <div>
    <informationBar :informationBarData="informationBarData" />
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import messagePopup from './components/messagePopup.vue';
import config from '@/config.json';
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
    messagePopup,
  }, methods: {
    handleClick(event) {
      this.$router.push('/' + event.id);
    },
  }, provide: {
    api: config.api,
  }, created() {
  }
}
</script>

<style scoped>
.centralFramework {
  width: 100%;
  height: 100%;
  border-left: 2px solid var(--color-theme-grayscale1);
  border-right: 2px solid var(--color-theme-grayscale1);
  /* position: relative; */
  
}
</style>

