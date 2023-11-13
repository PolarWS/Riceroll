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
            <a class="webLinkItem" v-for="(item, index) in  informationBarData.linkData " :key="index"
                :style="{ backgroundColor: '#' + item.color }" v-html="item.svg" :href="item.url">
            </a>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        informationBarData: Object
    }
}
</script>
<style scoped>
img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.informationBar {
    height: auto;
    border-bottom: 2px solid var(--color-theme-grayscale1);
}

.topImg {
    width: 100%;
    height: 20rem;
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

    transition: transform 0.2s;
}

.webLinkItem:hover {
    transform: translateY(-0.16rem);
}

.avatarImg {
    margin-top: -5rem;
    display: flex;
}

.avatarImg img {
    width: 10rem;
    height: 10rem;
    margin-left: 2rem;
    border-radius: 50%;
    border: 0.35rem solid var(--color-theme-white);

    transform-origin: center;
    transform: rotate(0deg);
    transition: transform 0.5s ease-in-out;
}

.avatarImg img:hover {
    transform: rotate(360deg);
}

.blogInformation h1 {
    margin: 5rem 0 0 1rem;
}

.blogInformation span {
    margin: 0 0 0 1rem;
    color: var(--color-theme-grayscale5);
    font-size: 1.2rem;
}
</style>