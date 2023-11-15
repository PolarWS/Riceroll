<template>
  <!-- 导航栏 -->
  <navigationBar @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <messagePopups />
    <router-view></router-view>
  </div>
  <!-- 侧边栏 -->
  <div>
    <informationBar v-if="!isMobile" :informationBarData="informationBarData" />
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import messagePopups from '@/components/messagePopups.vue';
import config from '@/config.json';
export default {
  data() {
    return {
      navigationBarData: config.navigationBarData,
      informationBarData: config.informationBarData,
      isMobile: true,
    }
  },
  components: {
    navigationBar,
    informationBar,
    messagePopups,
  }, methods: {
    handleClick(event) {
      this.$router.push('/' + event.id);
    },
    checkScreenSize() {
      this.isMobile = window.innerWidth <= 1024;
    },
  },
  provide: {
    api: config.api,
  },
  mounted() {
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreenSize);
  },
}
</script>

<style scoped>
.centralFramework {
  width: 100%;
  height: 100%;
  border-left: 2px solid var(--color-theme-grayscale1);
  border-right: 2px solid var(--color-theme-grayscale1);
}
</style>

