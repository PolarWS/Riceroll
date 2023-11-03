<template>
    <div class="informationBar">
        <div class="topImg">
            <img :src="informationBarData.topimg.src" :alt="informationBarData.topimg.alt">
        </div>
        <div class="avatarImg">
            <img :src="informationBarData.avatar.src" :alt="informationBarData.avatar.alt">
            <div class="blogInformation">
                <h1>{{ informationBarData.blogInformation.name }}</h1>
                <span>#{{ informationBarData.blogInformation.introduction }}</span>
            </div>
        </div>
        <div class="webLink">
            <div class="webLinkItem" v-for="(item, index) in  informationBarData.linkData " :key="index"
                :style="{ backgroundColor: '#' + item.color }" v-html="item.svg">
            </div>
        </div>
    </div>
</template>
<script> 
import githubLink from "./linkIcon/githubLink.vue";
import bilibiliLink from "./linkIcon/bilibiliLink.vue";
import cloudMusicLink from "./linkIcon/cloudMusicLink.vue";
export default {
    data() {
        return {

        }
    },
    components: {
        githubLink,
        bilibiliLink,
        cloudMusicLink,
    }, props: {
        informationBarData: Object
    }
}
</script>
<style scoped>
.informationBar {
    height: auto;
    border-bottom: 2px solid #F4F4F4;
}

.topImg {
    width: 100%;
    height: 20rem;
}

.avatarImg {
    margin-top: -5rem;
    display: flex;
}

.webLink {
    display: flex;
    margin: 1.5rem 0 1.5rem 3rem;
}

.webLinkItem {
    width: 2rem;
    height: 2rem;
    margin: 0 2rem 0 0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.avatarImg img {
    width: 10rem;
    height: 10rem;
    margin-left: 2rem;
    border-radius: 50%;
    border: 0.35rem solid #fff;
}

.blogInformation h1 {
    margin: 5rem 0 0 1rem;
}

.blogInformation span {
    margin: 0 0 0 1rem;
    color: #8A8E90;
    font-size: 1.2rem;
}

img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>