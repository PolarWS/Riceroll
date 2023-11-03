<template>
  <!-- 导航栏 -->
  <navigationBar @handleClick="handleClick" :navigationBarData="navigationBarData" />
  <!-- 中心内容页 -->
  <div class="centralFramework">
    <component :is="showBody" :itemData="itemData" v-if="showBodyDisplay"></component>
    <bodyItem :itemData="itemData" v-if="!showBodyDisplay" />
  </div>
  <!-- 侧边栏 -->
  <informationBar :informationBarData="informationBarData" />
</template>

<script>
import navigationBar from '@/components/navigationBar.vue';
import informationBar from '@/components/informationBar.vue';
import articlePage from '@/components/body/articlePage.vue';
import filePage from '@/components/body/filePage.vue';
import aboutPage from '@/components/body/aboutPage.vue';
import friendLinkPage from '@/components/body/friendLinkPage.vue';
import musicPage from '@/components/body/musicPage.vue';
import searchPage from '@/components/body/searchPage.vue';
import bodyItem from './components/bodyItem.vue';
import config from '@/config.json';
export default {
  data() {
    return {
      showBody: String,
      showBodyDisplay: Boolean,
      itemData: Object,
      // 评论区开关，目前还没写
      comment: Boolean,
      navigationBarData: config.navigationBarData,
      informationBarData: config.informationBarData,
    }
  },
  components: {
    navigationBar,
    informationBar,
    articlePage,
    filePage,
    aboutPage,
    friendLinkPage,
    musicPage,
    searchPage,
    bodyItem,
  }, methods: {
    handleClick(event) {
      let defaultVue = ["articlePage", "searchPage", "musicPage", "filePage", "friendLinkPage", "aboutPage"]
      this.itemData = this.navigationBarData.titleData[event.data].data;
      this.comment = this.navigationBarData.titleData[event.data].comment;
      if (defaultVue.includes(event.id)) {
        this.showBodyDisplay = true;
        this.showBody = event.id;
      } else {
        this.showBodyDisplay = false;
      }
    }
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

