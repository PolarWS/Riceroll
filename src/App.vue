<template>
  <messagePopups />
  <div class="Riceroll">
    <!-- 导航栏 -->
    <navigationBar v-if="widthLevel >= 2" :navigationBarData="navigationBarData" />
    <!-- 中心内容页 -->
    <div class="centralFramework">
      <!-- 导航栏mob -->
      <navigationBarMob v-if="widthLevel < 2" @navigationBarMobSwitch="navigationBarMobSwitch"
        :navigationBarData="navigationBarData" :style="{ right: navigationBarMobRight + 'rem' }" />
      <topMenuBar v-if="widthLevel < 2" @navigationBarMobSwitch="navigationBarMobSwitch"
        :navigationBarData="navigationBarData.titleData" :blogName="blogName" />
      <RouterView v-slot="{ Component }">
        <transition-group name="fade" @enter="scrollToTop" tag="div" class="transition-container">
            <div :key="$route.path" style="width: 100%">
                <component :is="Component" />
            </div>
        </transition-group>
      </RouterView>
      <backToTheTop />

    </div>
    <!-- 侧边栏 -->
    <div v-show="widthLevel > 3">
      <informationBar :informationBarData="informationBarData" :markdownTocData="markdownTocData"
        :markdownTocIndex="markdownTocIndex" />
    </div>
  </div>
  <div class="footerMobile" v-show="widthLevel < 4">
    <a :href="item.url" v-for="item in config.informationBarData.footmark">{{ item.title }}</a>
  </div>
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import navigationBarMob from '@/components/navigationBarMob.vue';
import informationBar from '@/components/informationBar.vue';
import messagePopups from '@/components/messagePopups.vue';
import topMenuBar from '@/components/topMenuBar.vue';
import backToTheTop from './components/backToTheTop.vue';
import { dataRelayStore } from '@/store/dataRelayStore.js';

export default {
  data() {
    return {
      config: Object,
      navigationBarData: Object,
      informationBarData: Object,
      blogName: Object,
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
      dataRelayStore().widthLevel = this.widthLevel;
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    },
  },
  created() {
    this.config = this.configData;
    dataRelayStore().configData = this.config;
    this.navigationBarData = this.config.navigationBarData;
    this.informationBarData = this.config.informationBarData;
    this.blogName = this.config.blogName;
  },
  mounted() {
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);

  },
  unmounted() {
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkScreenSize);
  }, props: ['configData'],
}
</script>

<style scoped>
.centralFramework {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  border-left: 2px solid var(--color-theme-frame1);
  border-right: 2px solid var(--color-theme-frame1);
  overflow: hidden;
  position: relative;
}

.footerMobile {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  padding: 1.75rem 0;
  background-color: var(--color-theme-blue-1);
}

.footerMobile a {
  display: flex;
  justify-content: center;
  margin: 0.25rem 1rem;
  text-decoration: none;
  cursor: pointer;
  color: var(--color-theme-white);
}

@media screen and (max-width: 1280px) {
  .centralFramework {
    border-right: 2px solid var(--color-theme-frame1);
  }
}

@media screen and (max-width: 600px) {
  .footerMobile {
    flex-direction: column;
  }

  .footerMobile a {
    margin: 0.15rem 0;
  }
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.fade-enter-to {
  opacity: 1;
  transform: translateY(0);
}

.fade-leave-active {
    position: absolute;
    width: 100%;
    top: 0;
    left: 0;
    transition: all 0.3s ease;
}

.transition-container {
    position: relative;
    min-height: 100vh; /* 添加最小高度 */
    display: block;
    overflow: hidden;
}

.fade-enter-active {
  transition: all 0.4s ease;
  transition-delay: 0.2s;
}

.fade-leave-from {
  opacity: 1;
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.transition-container {
    position: relative;
    overflow: hidden;
    width: 100%;
}

</style>
