<template>
  <!-- 导航栏 -->
  <navigationBar v-if="widthLevel >= 2"  :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <!-- 导航栏mob -->
    <navigationBarMob v-if="widthLevel < 2" @navigationBarMobSwitch="navigationBarMobSwitch"
      :navigationBarData="navigationBarData" :style="{ right: navigationBarMobRight + 'rem' }" />
    <topMenuBar v-if="widthLevel < 2" @navigationBarMobSwitch="navigationBarMobSwitch"
      :navigationBarData="navigationBarData.titleData" :blogName="blogName" />
    <messagePopups ref="messagePopups" />
    <RouterView v-slot="{ Component }">
      <transition-group name="fade" @enter="scrollToTop">
        <div :key="$route.path">
          <component :is="Component" />
        </div>
      </transition-group>
    </RouterView>
    <backToTheTop />
  </div>
  <!-- 侧边栏 -->
  <div v-if="widthLevel > 3">
    <informationBar :informationBarData="informationBarData" :markdownTocData="markdownTocData"
      :markdownTocIndex="markdownTocIndex" />
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import navigationBarMob from '@/components/navigationBarMob.vue';
import informationBar from '@/components/informationBar.vue';
import messagePopups from '@/components/messagePopups.vue';
import topMenuBar from '@/components/topMenuBar.vue';
import backToTheTop from './components/backToTheTop.vue';
import { dataRelay } from '@/store/dataRelay.js';
import config from '@/config.json';
export default {
  data() {
    return {
      navigationBarData: config.navigationBarData,
      informationBarData: config.informationBarData,
      blogName: config.blogName,
      navigationBarMobRight: 50,
      widthLevel: Number,
      markdownTocIndex: -1,
      markdownTocData: {
        display: false,
        data: {},
      },
    }
  },
  components: {
    navigationBar,
    navigationBarMob,
    informationBar,
    messagePopups,
    topMenuBar,
    backToTheTop,
  },
  methods: {
    messagePopups(event) {
      this.$refs.messagePopups.showPopup(event);
    },
    markdownToc(Toc) {
      this.markdownTocData = Toc;
    },
    markdownTocIndexs(index) {
      this.markdownTocIndex = index;
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
      } else if (window.innerWidth > 750) {
        this.widthLevel = 3;
      } else if (window.innerWidth > 600) {
        this.widthLevel = 2;
      } else {
        this.widthLevel = 1;
      }
      dataRelay().widthLevel = this.widthLevel;
    },
    scrollToTop() {
      window.scrollTo(0, 0);
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
  border-left: 2px solid var(--color-theme-frame1);
  border-right: 2px solid var(--color-theme-frame1);
}

@media screen and (max-width: 1280px) {
  .centralFramework {
    border-right: 2px solid var(--color-theme-frame1);
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

