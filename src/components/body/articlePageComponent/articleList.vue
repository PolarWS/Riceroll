<template>
    <div class="articleListCard" v-for="(item, index) in this.articleListData">
        <div class="articleListCardBox">
            <div class="articleListCardImg" :style="{ backgroundImage: 'url(' + item.img + ')' }"></div>
            <div class="articleListCardTitle">
                <div id="title">{{ item.title }}</div>
                <span class="date">{{ item.date }}</span>
                <span class="date" v-for="label in item.label">#{{ label }}</span>
                <div id="content">
                    <span>{{ item.content }}</span>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { useCounterStore } from '../../../store/axiosStore.js';
export default {
    data() {
        return {
            articleListData: Object,
        }
    }, created() {
        useCounterStore().apiRequest(this.api.url + this.api.articlePage).then(data => {
            if (data.status == 200) {
                this.articleListData = data.data;
            }
        });
    },
    inject: ['api'],
}
</script>
<style scoped>
#title {
    font-size: 1.65rem;
    margin-bottom: 0.3rem;
    color: var(--color-theme-white);

    width: 100%;
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.date {
    margin-right: 0.75rem;
    color: var(--color-theme-grayscale1);
    line-height: 1rem;
    transition: line-height 0.15s;
}

.articleListCardBox:hover .date {
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


    transition: box-shadow 0.25s;
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

.articleListCardBox:hover .articleListCardTitle {
    background-color: var(--color-theme-black2);
    margin-top: 10.5rem;
    height: 7.5rem;
}

.articleListCardBox:hover .articleListCardImg {
    filter: blur(2px);
    transform: scale(1.05);
}

.articleListCardTitle {
    margin-top: 12rem;
    height: 6rem;
    padding: 1rem 0 0 1.5rem;
    border-radius: 0 0 0.75rem 0.75rem;
    background-color: var(--color-theme-black1);
    right: 0;

    transition: margin-top 0.2s, height 0.2s, background-color 0.2s;
}

.articleListCardBox:hover #content {
    line-height: 1rem;
}

#content {
    width: 100%;
    line-height: 4.5rem;
    transition: line-height 0.3s;
    color: var(--color-theme-grayscale1);
}

#content span {
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

@media screen and (max-width: 600px) {
    #title {
        font-size: 1.5rem;
    }

    .articleListCard {
        height: 14rem;
    }

    .articleListCardTitle {
        margin-top: 8.5rem;
        height: 5.5rem;
    }

    .articleListCardBox {
        height: 14rem;
    }

    .articleListCardBox:hover .articleListCardTitle {
        margin-top: 6.5rem;
        height: 7.5rem;
    }
}
</style>