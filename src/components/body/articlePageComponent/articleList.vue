<template>
    <div v-if="renderBoolean" class="articleListCard" v-for="(item, index) in this.articleListData">
        <div class="articleListCardBox" @click="articleListCardBoxClick(item.id)">
            <div class="articleListCardImg" :style="{ backgroundImage: 'url(' + item.img + ')' }"></div>
            <div class="articleListCardSpan">
                <div class="articleListCardTitle">{{ item.title }}</div>
                <div class="articleListCardData">
                    <div class="articleListCardItem">
                        <svg t="1700204012481" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="11426" width="15" height="15">
                            <path
                                d="M739.196 198c-7.092 14.786-22.202 24.996-39.696 24.996-17.494 0-32.604-10.21-39.696-24.996H351.196c-7.092 14.786-22.202 24.996-39.696 24.996-17.494 0-32.604-10.21-39.696-24.996H133c-24.3 0-44 19.7-44 44v109.64a44.123 44.123 0 0 1 10.179-1.14L933 353.89V242c0-24.3-19.7-44-44-44H739.196z m4.304-88H889c72.902 0 132 59.098 132 132v594c0 72.902-59.098 132-132 132H133C60.098 968 1 908.902 1 836V242c0-72.902 59.098-132 132-132h134.5V45c0-24.3 19.7-44 44-44s44 19.7 44 44v65h300V45c0-24.3 19.7-44 44-44s44 19.7 44 44v65zM89 437.358V836c0 24.3 19.7 44 44 44h756c24.3 0 44-19.7 44-44V441.891L98.821 438.5A44.142 44.142 0 0 1 89 437.358zM274 721.5c-24.3 0-44-19.7-44-44s19.7-44 44-44h471.114c24.3 0 44 19.7 44 44s-19.7 44-44 44H274z"
                                fill="#ffffff" p-id="11427"></path>
                        </svg>
                        <span>{{ item.date }}</span>
                    </div>
                    <div class="articleListCardItem">
                        <svg t="1700205663159" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="2420" width="18" height="18">
                            <path
                                d="M896 128a42.7 42.7 0 0 1 42.7 42.7v682.7a42.7 42.7 0 0 1-42.7 42.7H128a42.7 42.7 0 0 1-42.7-42.7V170.7A42.7 42.7 0 0 1 128 128h768z m-42.7 85.3H170.7v597.3h682.7V213.3zM401 341.3l136.5 341.3h-91.9l-17.1-42.7H288.1L271 682.6h-91.8l136.5-341.3H401z m409.7 0v341.3h-128a128 128 0 0 1 0-256h42.6v-85.3h85.3zM725.4 512h-42.7a42.7 42.7 0 0 0-5 85l5 0.3h42.7V512z m-367-47.6l-36.2 90.3h72.2l-36.1-90.2z"
                                p-id="2421" fill="#ffffff"></path>
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
    <loadingDynamicEffect v-show="!renderBoolean" />
</template>
<script>
import loadingDynamicEffect from '../../loadingDynamicEffect.vue';
import { useCounterStore } from '../../../store/axiosStore.js';
export default {
    data() {
        return {
            renderBoolean: false,
            articleListData: Object,
        }
    }, created() {
        useCounterStore().apiRequest(this.api.url + this.api.articlePage)
            .then(data => {
                if (data.status == 200) {
                    this.articleListData = data.data;
                    this.renderBoolean = true;
                } else {
                    this.$root.myMethod({
                        message: '服务器错误',
                        Color: 'messageY',
                    });
                }
            })
            .catch(error => {
                this.$root.myMethod({
                    message: '服务器连接失败',
                    Color: 'messageR',
                });
            });
    }, components: {
        loadingDynamicEffect,
    },
    methods: {
        articleListCardBoxClick(event) {
            this.$router.push('/articlePage/' + event);
        }
    },
    inject: ['api'],
}
</script>
<style scoped>
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
    background-position: center center;
    position: relative;

    overflow: hidden;
    /* 控制内容溢出的部分被遮住 */
    transition: box-shadow 0.25s, transform 0.1s;
}

.articleListCardImg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: 100%;
    background-position: center;
    background-repeat: no-repeat;
    z-index: -1;
    transition: background-size 0.5s, filter 0.4s;
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
    background-size: 108%;
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