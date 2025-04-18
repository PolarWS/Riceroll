<!-- 主页组件 -->
<template>
    <div class="informationBarToc">
        <div class="infBarTocTopImg" :style="`background-image: url(${itemData.topimg})`"></div>
        <div class="infBarTocAvatarImg">
            <img :src="itemData.avatar">
            <div class="infBarTocBlogInf">
                <h1>{{ itemData.blogInformation.name }}</h1>
                <span>#{{ itemData.blogInformation.introduction }}</span>
            </div>
        </div>
        <div class="infBarTocWebLink">
            <a class="infBarTocWebLinkItem" v-for="(item, index) in itemData.linkData" :key="index"
                :style="{ backgroundColor: '#' + item.color }" v-html="item.svg" :href="item.url">
            </a>
        </div>
    </div>
    <div v-show="renderBoolean" class="articleListCard" v-for="(item, index) in this.articleListData">
        <div class="articleListCardBox" @click="articleListCardBoxClick(item.id)">
            <div class="articleListCardImg"
                :style="{ backgroundImage: 'url(' + api.url + api.cover + '/' + item.cover + ')' }"></div>
            <div class="articleListCardSpan">
                <div class="articleListCardTitle">{{ item.title }}</div>
                <div class="articleListCardData">
                    <div class="articleListCardItem">
                        <svg width="15" height="15" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5 19H43V40C43 41.1046 42.1046 42 41 42H7C5.89543 42 5 41.1046 5 40V19Z"
                                fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" />
                            <path d="M5 9C5 7.89543 5.89543 7 7 7H41C42.1046 7 43 7.89543 43 9V19H5V9Z" stroke="#ffffff"
                                stroke-width="4" stroke-linejoin="round" />
                            <path d="M16 4V12" stroke="#ffffff" stroke-width="4" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M32 4V12" stroke="#ffffff" stroke-width="4" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M28 34H34" stroke="#ffffff" stroke-width="4" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M14 34H20" stroke="#ffffff" stroke-width="4" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M28 26H34" stroke="#ffffff" stroke-width="4" stroke-linecap="round"
                                stroke-linejoin="round" />
                            <path d="M14 26H20" stroke="#ffffff" stroke-width="4" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                        <span>{{ item.createdAt.slice(0, 10) }}</span>
                    </div>
                    <div class="articleListCardItem">
                        <svg t="1700205663159" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="2420" width="18" height="18">
                            <path d="M896 128a42.7 42.7 0 0 1 42.7 42.7v682.7a42.7 42.7 0 0 1-42.7 42.7H128a42.7 42.7 0 0 1-42.7-42.7V170.7A42.7 
                                42.7 0 0 1 128 128h768z m-42.7 85.3H170.7v597.3h682.7V213.3zM401 341.3l136.5 341.3h-91.9l-17.1-42.7H288.1L271 
                                682.6h-91.8l136.5-341.3H401z m409.7 0v341.3h-128a128 128 0 0 1 0-256h42.6v-85.3h85.3zM725.4 512h-42.7a42.7 42.7 
                                0 0 0-5 85l5 0.3h42.7V512z m-367-47.6l-36.2 90.3h72.2l-36.1-90.2z" p-id="2421"
                                fill="#ffffff"></path>
                        </svg>
                        <span>{{ item.wordCount }}</span>
                    </div>
                </div>
                <div class="articleListCardContent">
                    <span>{{ item.content }}</span>
                </div>
            </div>
        </div>
    </div>
    <pagination v-show="renderBoolean" :pageMax="this.pageMax" :page="this.page" @pageChange="pageChange" />
    <loadingDynamicEffect v-show="!renderBoolean" />
</template>
<script>
import loadingDynamicEffect from '@/components/loadingDynamicEffect.vue';
import pagination from '@/components/pagination.vue';
import { axiosStore } from '@/store/axiosStore.js';
export default {
    data() {
        return {
            page: 1,
            pageMax: 1,
            renderBoolean: false,
            articleListData: Object,
            // api: axiosStore().api.url + axiosStore().api.articlePage,
            api: axiosStore().api,
        }
    }, created() {
        axiosStore().apiRequest(this.api.url + this.api.articlePage, { "page": this.page })
            .then(data => {
                if (data.status == 200) {
                    this.articleListData = data.data;
                    this.renderBoolean = true;
                    this.pageMax = data.pages;
                }
            })
    }, components: {
        loadingDynamicEffect,
        pagination,
    }, methods: {
        articleListCardBoxClick(event) {
            this.articleListData = []
            this.$router.push('/articlePage/' + event);
        },
        pageChange(page) {
            this.renderBoolean = false;
            axiosStore().apiRequest(this.api.url + this.api.articlePage, { "page": page })
                .then(data => {
                    if (data.status == 200) {
                        this.articleListData = data.data;
                        this.renderBoolean = true;
                        this.page = page;
                    }
                })
            this.page = page;
        }
    }, props: {
        itemData: Object,
    },
}
</script>
<style scoped>
.infBarTocAvatarImg img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.informationBarToc {
    height: auto;
    border-bottom: 2px solid var(--color-theme-frame1);
}

.infBarTocTopImg {
    width: 100%;
    height: 20rem;
    background-size: cover;
    background-position: center;
}

.infBarTocWebLink {
    display: flex;
    margin: 1.8rem 0 1.8rem 3.2rem;
}

.infBarTocWebLinkItem {
    width: 2rem;
    height: 2rem;
    margin: 0 2.5rem 0 0;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;

    transition: transform 0.2s;
}

.infBarTocWebLinkItem:hover {
    transform: translateY(-0.16rem);
}

.infBarTocAvatarImg {
    margin-top: -5rem;
    display: flex;
}

.infBarTocAvatarImg img {
    width: 10rem;
    height: 10rem;
    margin-left: 2.5rem;
    border-radius: 50%;
    border: 0.35rem solid var(--color-theme-white);

    transform-origin: center;
    transform: rotate(0deg);
    transition: transform 0.5s ease-in-out;
}

.infBarTocAvatarImg img:hover {
    transform: rotate(360deg);
}

.infBarTocBlogInf h1 {
    font-size: 2.35rem;
    margin: 5rem 0 0 1rem;
}

.infBarTocBlogInf span {
    margin: 0 0 0 1rem;
    color: var(--color-theme-grayscale5);
    font-size: 1.25rem;
}

.articleListCardTitle {
    font-size: 1.65rem;
    margin-bottom: 0.3rem;
    color: var(--color-theme-white);
    font-weight: 550;
    width: 100%;
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.articleListCardData {
    display: flex;
    line-height: 1.5rem;
    transition: line-height 0.15s;
}

.articleListCardItem {
    margin-right: 0.75rem;
    color: var(--color-theme-grayscale1);
    font-weight: 550;
    display: flex;
    align-items: center;
}

.articleListCardItem span {
    margin-left: 0.35rem;
}

.articleListCardBox:hover .articleListCardData {
    line-height: 2rem;
}

.articleListCard {
    height: 18rem;
    display: grid;
    grid-template-columns: 1fr;
    padding: 1.5rem 5% 0 5%;
    max-width: 45rem;
    margin-left: auto;
    margin-right: auto;

    animation-name: fadeIn;
    animation-duration: 0.5s;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.articleListCardBox {
    cursor: pointer;
    height: 18rem;
    border-radius: 0.75rem;
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    transition: box-shadow 0.25s, transform 0.1s;
}

.articleListCardImg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    z-index: -1;
    transition: transform 0.4s, filter 0.4s;
}

.articleListCardBox:hover {
    box-shadow: 0 0 0.75rem 0.5rem var(--color-theme-grayscale2);
}

.articleListCardBox:active {
    transform: scale(0.98);
}

.articleListCardBox:hover .articleListCardSpan {
    background-color: var(--color-theme-black2);
    margin-top: 10.5rem;
    height: 7.5rem;
}

.articleListCardBox:hover .articleListCardImg {
    filter: blur(2px);
    transform: scale(1.1);
}

.articleListCardSpan {
    margin-top: 12rem;
    height: 6rem;
    padding: 1rem 1.5rem 0 1.5rem;
    border-radius: 0 0 0.75rem 0.75rem;
    background-color: var(--color-theme-black1);
    right: 0;

    transition: margin-top 0.2s, height 0.2s, background-color 0.2s;
}

.articleListCardBox:hover .articleListCardContent {
    line-height: 1rem;
}

.articleListCardContent {
    width: 100%;
    line-height: 4.5rem;
    transition: line-height 0.3s;
    color: var(--color-theme-grayscale1);
}

.articleListCardContent span {
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

@media screen and (max-width: 600px) {
    .infBarTocWebLink {
        display: flex;
        margin: 1.2rem 0 1.2rem 2.5rem;
    }

    .infBarTocTopImg {
        height: 15rem;
    }

    .infBarTocBlogInf h1 {
        font-size: 2rem;
    }

    .infBarTocBlogInf span {
        font-size: 1rem;
    }

    .infBarTocAvatarImg img {
        margin-top: 2rem;
        width: 7rem;
        height: 7rem;
        margin-left: 1.5rem;
    }

    .infBarTocWebLinkItem {
        width: 2rem;
        height: 2rem;
        margin: 0 2rem 0 0;
    }

    .articleListCardTitle {
        font-size: 1.5rem;
    }

    .articleListCard {
        height: 14rem;
    }

    .articleListCardSpan {
        margin-top: 8.5rem;
        height: 5.5rem;
    }

    .articleListCardBox {
        height: 14rem;
    }

    .articleListCardBox:hover .articleListCardSpan {
        margin-top: 6.5rem;
        height: 7.5rem;
    }
}
</style>