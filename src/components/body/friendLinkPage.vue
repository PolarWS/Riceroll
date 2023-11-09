<template>
    <div id="pressed">
        <div class="cardBox" v-for="item in itemData.cardList" @click="linkClick(item.url)">
            <div class="cardImg">
                <img :src="(item.src)" />
                <div class="state" :class="statePing(item.delay)"></div>
            </div>
            <div class="cardContent">
                <div class="title">{{ item.title }}</div>
                <span class="content">{{ item.content }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import { useCounterStore } from '../../store/friendLink.js';
export default {
    data() {
        return {

        }
    }, methods: {
        linkClick(url) {
            window.open(url);
        },
        statePing(delay) {
            if (delay < 50) {
                return "stateG";
            } else if (delay < 200) {
                return "stateY";
            } else if (delay < 998) {
                return "stateO";
            } else {
                return "stateR";
            }
        }
    }, mounted() {
        console.log(useCounterStore().urlPing("http://127.0.0.1:5000/"));
    },
    props: {
        itemData: Object,
    }
}
</script>
<style scoped>
.content {
    width: 9rem;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: 2;
}

.title {
    font-size: 1.35rem;
    font-weight: 520;
    margin-top: 0;
    margin-bottom: 0.5rem;
    width: 9rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.state {
    width: 0.85rem;
    height: 0.85rem;
    border-radius: 50%;
    border: 0.25rem solid #fff;
    position: absolute;
    margin-top: 5rem;
    /* 处于底部 */
}

.stateR {
    background-color: #FF5F5F;
}

.stateO {
    background-color: #F8A978;
}

.stateY {
    background-color: #FFD65F;
}

.stateG {
    background-color: #8AFF5F;
}

.content {
    color: #8A8E90;
}

#pressed {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin: 1.5rem;
}

@media (max-width: 80rem) {
    #pressed {
        grid-template-columns: 1fr;
    }

    .content,
    .title {
        width: 10rem;
    }
}


.cardBox {
    display: grid;
    border-radius: 0.55rem;
    height: 9.5rem;
    grid-template-columns: 2fr 3fr;
    justify-content: center;
    border: 2px solid #F4F4F4;
    cursor: pointer;

    transition: box-shadow 0.25s;
}

.cardBox:hover {
    box-shadow: 0 0 0.75rem 0.02rem #eeeeee;
}

.cardBox img {
    width: 6rem;
    height: 6rem;
    border-radius: 50%;
}

.cardContent {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
}

.cardImg {
    display: flex;
    align-items: center;
    justify-content: right;
}
</style>
