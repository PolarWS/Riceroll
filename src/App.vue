<template>
  <!-- 导航栏 -->
  <navigationBar @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
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
  }, methods: {
    handleClick(event) {
      this.$router.push('/' + event.id);
    },
  }, provide: {
    api: config.api,
  }
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

