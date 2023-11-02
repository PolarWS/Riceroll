<template>
    <div class="informationBar">
        <div class="topImg">
            <img :src="topimg.src" :alt="topimg.alt">
        </div>
        <div class="avatarImg">
            <img :src="avatar.src" :alt="avatar.alt">
            <div class="blogInformation">
                <h1>{{ blogInformation.name }}</h1>
                <span>#{{ blogInformation.introduction }}</span>
            </div>
        </div>
        <div class="webLink">
            <div class="webLinkItem" v-for="(item, index) in  linkData " :key="index"
                :style="{ backgroundColor: '#' + item.color }">
                <component :is="item.alt"></component>
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
            topimg: {
                src: "/src/components/img/zhuye.png",
                alt: "topimg",
            },
            avatar: {
                src: "/src/components/img/avatar.jpg",
                alt: "avatar",
            },
            blogInformation: {
                name: "鸦鸦不是鸭鸭",
                introduction: "恭喜你发现了一只鸦",
            },
            linkData: [{
                src: "/src/components/img/github.svg",
                alt: "githubLink",
                color: "000000",
            },
            {
                src: "/src/components/img/github.svg",
                alt: "bilibiliLink",
                color: "fb7299",
            },
            {
                src: "/src/components/img/github.svg",
                alt: "cloudMusicLink",
                color: "ec4141",
            }]
        }
    },
    components: {
        githubLink,
        bilibiliLink,
        cloudMusicLink,
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