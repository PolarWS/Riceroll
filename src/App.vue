<template>
  <!-- 导航栏 -->
  <navigationBar @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <topMenuBar v-if="isMobile600" />
    <messagePopups />
    <router-view></router-view>
  </div>
  <!-- 侧边栏 -->
  <div>
    <informationBar v-if="isMobile1024" :informationBarData="informationBarData" />
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import messagePopups from '@/components/messagePopups.vue';
import topMenuBar from '@/components/topMenuBar.vue';
import config from '@/config.json';
export default {
  data() {
    return {
      navigationBarData: config.navigationBarData,
      informationBarData: config.informationBarData,
      isMobile1024: true,
      isMobile600: false,
    }
  },
  components: {
    navigationBar,
    informationBar,
    messagePopups,
    topMenuBar,
  }, methods: {
    handleClick(event) {
      this.$router.push('/' + event.id);
    },
    checkScreenSize() {
      this.isMobile1024 = window.innerWidth > 1024;
      this.isMobile600 = window.innerWidth <= 600;
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
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  border-left: 2px solid var(--color-theme-grayscale1);
  border-right: 2px solid var(--color-theme-grayscale1);
}

@media screen and (max-width: 1280px) {
  .centralFramework {
    border-right: 2px solid var(--color-theme-grayscale1);
  }
}
</style>

