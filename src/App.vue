<template>
  <!-- 导航栏 -->
  <navigationBar v-if="widthLevel >= 3" @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <!-- 导航栏mob -->
    <navigationBarMob v-if="widthLevel < 3" @handleClick="handleClick" @navigationBarMobSwitch="navigationBarMobSwitch"
      :navigationBarData="navigationBarData" :style="{ right: navigationBarMobRight + 'rem' }" />
    <topMenuBar v-if="widthLevel < 3" @navigationBarMobSwitch="navigationBarMobSwitch" />
    <messagePopups ref="messagePopups" />
    <RouterView v-slot="{ Component }">
      <transition-group name="fade">
        <div :key="$route.path">
          <component :is="Component" />
        </div>
      </transition-group>
    </RouterView>
    <!-- <router-view></router-view> -->
  </div>
  <!-- 侧边栏 -->
  <div v-if="widthLevel > 3">
    <informationBar :informationBarData="informationBarData" />
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import navigationBarMob from '@/components/navigationBarMob.vue';
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
      navigationBarMobRight: 50,
      widthLevel: Number,
    }
  },
  components: {
    navigationBar,
    navigationBarMob,
    informationBar,
    messagePopups,
    topMenuBar,
  }, methods: {
    handleClick(event) {
      this.$router.push('/' + event.id);
    },
    myMethod(event) {
      this.$refs.messagePopups.showPopup(event);
    },
    navigationBarMobSwitch(event) {
      if (event) {
        this.navigationBarMobRight = 0;
      } else {
        this.navigationBarMobRight = 50;
      }
    },
    checkScreenSize() {
      if (window.innerWidth > 1280) {
        this.widthLevel = 5;
      } else if (window.innerWidth > 1024) {
        this.widthLevel = 4;
      } else if (window.innerWidth > 600) {
        this.widthLevel = 3;
      } else {
        this.widthLevel = 2;
      }
      dataRelay().widthLevel = this.widthLevel;
    },
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

.fade-enter-from {
  opacity: 0;
}

.fade-enter-to {
  opacity: 1;
}

.fade-leave-active {
  transition: opacity 0.15s;
}

.fade-enter-active {
  transition: opacity .15s;
  transition-delay: 0.2s;
}

.fade-leave-from {
  opacity: 1;
}

.fade-leave-to {
  opacity: 0;
}
</style>

