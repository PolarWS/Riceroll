<template>
  <!-- 导航栏 -->
  <navigationBar @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <topMenuBar v-if="widthLevel < 3" />
    <messagePopups />
    <router-view></router-view>
  </div>
  <!-- 侧边栏 -->
  <div>
    <informationBar v-if="widthLevel > 3" :informationBarData="informationBarData" />
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import messagePopups from '@/components/messagePopups.vue';
import topMenuBar from '@/components/topMenuBar.vue';
import { dataRelay } from '@/store/dataRelay.js';
import config from '@/config.json';
export default {
  data() {
    return {
      navigationBarData: config.navigationBarData,
      informationBarData: config.informationBarData,
      widthLevel: 0,
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
      dataRelay().winWidth();
      this.widthLevel = dataRelay().widthLevel;
    },
  },
  watch: {

  },
  created() {
    this.checkScreenSize();
  },
  mounted() {
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreenSize);
  },
  provide() {
    return {
      api: config.api
    }
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

