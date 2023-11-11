<template>
    <div class="articleListCard" v-for="(item, index) in this.articleListData">
        <div class="articleListCardBox">
            <div class="articleListCardImg" :style="{ backgroundImage: 'url(' + item.img + ')' }"></div>
            <div class="articleListCardImg"></div>
            <div class="articleListCardTitle">
                <div id="title">{{ item.title }}</div>
                <span class="date">{{ item.date }}</span>
                <span class="date" v-for="label in item.label">#{{ label }}</span>
                <div id="content">
                    <span class="date">{{ item.content }}</span>
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
    color: white;

    width: 35rem;
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.date {
    margin-right: 0.75rem;
    color: rgb(235, 235, 235);
}

.articleListCard {
    height: 16rem;
    display: grid;
    grid-template-columns: 1fr;
    padding: 1.5rem 5% 0 5%;

}

.articleListCardBox {
    cursor: pointer;
    box-shadow: 0 0 0.5rem #eeeeee;
    height: 16rem;
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

    transition: transform 0.4s;
    /* transform: scale(1.2); */
}

.articleListCardBox:hover {
    box-shadow: 0 0 0.75rem 0.5rem #e5e5e5;
}

.articleListCardBox:hover .articleListCardTitle {
    background-color: rgba(0, 0, 0, 0.38);
    margin-top: 8.75rem;
    height: 6.25rem;
}

.articleListCardBox:hover .articleListCardImg {
    transform: scale(1.05);
}

.articleListCardTitle {
    margin-top: 10rem;
    height: 5rem;
    padding: 1rem 0 0 1.5rem;
    border-radius: 0 0 0.75rem 0.75rem;
    background-color: rgba(0, 0, 0, 0.25);
    right: 0;

    transition: margin-top 0.2s, height 0.2s, background-color 0.2s;
}

.articleListCardBox:hover #content {
    line-height: 1.25rem;
}

#content {
    width: 35rem;
    line-height: 4.5rem;
    transition: line-height 0.3s;
}

#content span {
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
</style>